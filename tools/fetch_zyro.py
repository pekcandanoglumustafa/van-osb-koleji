#!/usr/bin/env python3
"""Eski Zyro sitesindeki gorselleri kurtarir ve images/site/ altina kaydeder.

Her dosya icin sirayla su kaynaklar denenir:
  1. assets.zyrosite.com (orijinal ve boyutlandirilmis adresler)
  2. images.weserv.nl / wsrv.nl uzerinden ayni adresler
  3. Internet Arsivi (web.archive.org) kopyalari
Gecerli (gercekten resim olan) en buyuk dosya kaydedilir.
Sonuc raporu images/site/_kaynak.json dosyasina yazilir.

Kullanim: python3 tools/fetch_zyro.py tools/zyro-urls.txt images/site
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
SITE = "YD0Eeq404vF5okpN"


def kind(data):
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[4:12] in (b"ftypavif", b"ftypheic"):
        return "avif"
    return None


def get(url, referer=None):
    headers = {"User-Agent": UA, "Accept": "image/webp,image/png,image/jpeg,image/*;q=0.8,*/*;q=0.5"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
            return r.status, data
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001
        return str(e)[:80], b""


def base_name(fn):
    stem, ext = os.path.splitext(fn)
    stem = re.sub(r"-[A-Za-z0-9]{16}$", "", stem)
    return stem.lower()


def candidates(fn, seen_urls):
    raw = f"https://assets.zyrosite.com/{SITE}/{fn}"
    big = f"https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/{SITE}/{fn}"
    zyro = [raw, big] + sorted(seen_urls, key=lambda u: -int((re.search(r"w=(\d+)", u) or [0, 0])[1]))
    out = []
    for u in zyro:
        out.append(("zyro", u, "https://ozelvanosbkoleji.com/"))
        out.append(("zyro-noref", u, None))
    for u in zyro:
        q = urllib.parse.quote(u, safe="")
        out.append(("weserv", f"https://images.weserv.nl/?url={q}", None))
        out.append(("wsrv", f"https://wsrv.nl/?url={q}", None))
    for u in zyro:
        out.append(("wayback", f"https://web.archive.org/web/2025id_/{u}", None))
    return out


def wayback_cdx(fn):
    """Arsivde bu dosya adini iceren herhangi bir kopya var mi?"""
    q = urllib.parse.urlencode({
        "url": "assets.zyrosite.com/*",
        "filter": ["statuscode:200", f"original:.*{re.escape(fn)}.*"],
        "output": "json", "limit": "20", "fl": "timestamp,original,length",
    }, doseq=True)
    st, data = get("https://web.archive.org/cdx/search/cdx?" + q)
    if st != 200 or not data:
        return []
    try:
        rows = json.loads(data)[1:]
    except Exception:  # noqa: BLE001
        return []
    rows.sort(key=lambda r: -int(r[2] or 0))
    return [("wayback-cdx", f"https://web.archive.org/web/{t}id_/{o}", None) for t, o, _ in rows[:5]]


def main():
    url_file, dest = sys.argv[1], sys.argv[2]
    os.makedirs(dest, exist_ok=True)
    urls = [u.strip() for u in open(url_file, encoding="utf-8") if u.strip()]
    by_file = {}
    for u in urls:
        by_file.setdefault(u.split("/")[-1], set()).add(u)

    def one(item):
        fn, seen = item
        best = None
        tried = []
        for i, (src, url, ref) in enumerate(candidates(fn, seen)):
            st, data = get(url, ref)
            k = kind(data) if data else None
            tried.append(f"{src} {st} {len(data)}B {k or '-'}")
            if k and len(data) > 1500 and (best is None or len(data) > len(best[1])):
                best = (src, data, k, url)
            # orijinal (en buyuk) zyro kopyasi bulunduysa digerlerini denemeye gerek yok
            if best and best[0].startswith("zyro") and i >= 1:
                break
            if best and best[0] in ("weserv", "wsrv") and src == "wsrv":
                break
        if best is None:
            for src, url, ref in wayback_cdx(fn):
                st, data = get(url, ref)
                k = kind(data) if data else None
                tried.append(f"{src} {st} {len(data)}B {k or '-'}")
                if k and len(data) > 1500:
                    best = (src, data, k, url)
                    break
        name = base_name(fn)
        if best:
            src, data, k, url = best
            path = os.path.join(dest, f"{name}.{k}")
            with open(path, "wb") as f:
                f.write(data)
            print(f"OK   {fn} <- {src} ({len(data)//1024} KB)", flush=True)
            return fn, {"ok": True, "file": path, "source": src, "url": url, "bytes": len(data)}
        print(f"FAIL {fn}: {'; '.join(tried[:8])}", flush=True)
        return fn, {"ok": False, "tried": tried}

    with ThreadPoolExecutor(max_workers=12) as ex:
        report = dict(ex.map(one, sorted(by_file.items())))

    with open(os.path.join(dest, "_kaynak.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    ok = sum(1 for r in report.values() if r["ok"])
    print(f"\n{ok}/{len(report)} gorsel kurtarildi")


if __name__ == "__main__":
    main()
