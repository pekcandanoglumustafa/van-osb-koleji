#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

LOGO = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=375,fit=crop/YD0Eeq404vF5okpN/osb-1-XcW1Lh6MLoA7l2Lk.png"

# ---- NAV STRUCTURE ----
NAV = [
    {"label": "Anasayfa", "href": "index.html", "key": "home"},
    {"label": "Okulumuz", "href": "okulumuz.html", "key": "okulumuz", "children": [
        ("Tarihçe", "tarihce.html"),
        ("Misyon & Vizyon", "misyon-vizyon.html"),
        ("Yönetim Kadromuz", "yonetim-kadrosu.html"),
        ("Kurum Kültürümüz", "kurum-kulturu.html"),
        ("Kurumsal Değerlerimiz", "kurumsal-degerler.html"),
        ("Fiziksel & Teknik Donanım", "fiziksel-donanim.html"),
        ("Öğretmen & Personel Kadrosu", "ogretmen-kadrosu.html"),
        ("Basında Biz", "basinda-biz.html"),
        ("İletişim", "iletisim.html"),
    ]},
    {"label": "Bölümler", "href": "bolumler.html", "key": "bolumler", "children": [
        ("Bilişim Teknolojileri", "bilisim-teknolojileri.html"),
        ("Elektrik-Elektronik Teknolojisi", "elektrik-elektronik.html"),
        ("Kimya Teknolojisi", "kimya-teknolojisi.html"),
        ("Gıda Teknolojisi", "gida-teknolojisi.html"),
    ]},
    {"label": "Eğitim & Akademik", "href": "egitim-akademik.html", "key": "egitim", "children": [
        ("Hedeflerimiz", "hedeflerimiz.html"),
        ("Başarılarımız", "basarilarimiz.html"),
        ("Rehberlik Servisi", "rehberlik-servisi.html"),
        ("Zümre Çalışmaları", "zumre-calismalari.html"),
        ("Akademik Takvim", "akademik-takvim.html"),
    ]},
    {"label": "Projeler", "href": "projelerimiz.html", "key": "projeler", "children": [
        ("TÜBİTAK – Erasmus – AB", "tubitak-erasmus-ab.html"),
        ("Sosyal Sorumluluk", "sosyal-sorumluluk.html"),
        ("Staj ve İşletme Eğitimi", "staj-isletme-egitimi.html"),
        ("AR-GE Çalışmaları", "ar-ge-calismalari.html"),
    ]},
    {"label": "Galeri", "href": "galeri.html", "key": "galeri", "children": [
        ("Etkinliklerimiz", "etkinliklerimiz.html"),
        ("Okulumuzdan Kareler", "okulumuzdan-kareler.html"),
    ]},
    {"label": "Duyurular", "href": "duyurular.html", "key": "duyurular", "children": [
        ("Duyuru", "duyuru.html"),
        ("Dökümanlar", "dokumanlar.html"),
        ("Haftalık Yemek Listesi", "haftalik-yemek-listesi.html"),
    ]},
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
    '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&'
    'family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />')

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHECK = '<svg viewBox="0 0 24 24" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>'

def esc(s):
    return html.escape(s, quote=False)

def head(title, desc=""):
    return (f'<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8" />'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
            f'<title>{esc(title)}</title><meta name="description" content="{esc(desc)}" />'
            f'{FONTS}<link rel="stylesheet" href="style.css" /></head><body>')

def header(active):
    out = ['<header id="hdr"><div class="wrap nav">']
    out.append(f'<a href="index.html" class="brand"><img src="{LOGO}" alt="Van OSB Koleji logo" />'
               '<span class="brand-txt"><b>VAN OSB KOLEJİ</b><span>MESLEKİ &amp; TEKNİK</span></span></a>')
    out.append('<nav class="menu">')
    for item in NAV:
        cls = " active" if item["key"] == active else ""
        if item.get("children"):
            out.append(f'<div class="has-drop"><a href="{item["href"]}" class="top{cls}">{esc(item["label"])} {CHEV}</a>')
            out.append('<div class="drop">')
            for label, href in item["children"]:
                out.append(f'<a href="{href}">{esc(label)}</a>')
            out.append('</div></div>')
        else:
            out.append(f'<a href="{item["href"]}" class="top{cls}">{esc(item["label"])}</a>')
    out.append('</nav>')
    out.append('<button class="burger" id="burger" aria-label="Menüyü aç"><span></span><span></span><span></span></button>')
    out.append('</div></header>')
    # mobile menu
    out.append('<div class="mobile-menu" id="mm"><button class="mm-close" id="mmClose" aria-label="Kapat">&times;</button>')
    for item in NAV:
        if item.get("children"):
            out.append(f'<div class="mm-group"><button class="mm-top">{esc(item["label"])} {CHEV}</button><div class="mm-sub">')
            out.append(f'<a href="{item["href"]}">{esc(item["label"])} — Genel</a>')
            for label, href in item["children"]:
                out.append(f'<a href="{href}">{esc(label)}</a>')
            out.append('</div></div>')
        else:
            out.append(f'<a class="mm-solo" href="{item["href"]}">{esc(item["label"])}</a>')
    out.append('</div>')
    return "".join(out)

def footer():
    cols = ""
    for item in NAV:
        if not item.get("children"):
            continue
        links = f'<a href="{item["href"]}">Genel Bakış</a>'
        for label, href in item["children"][:5]:
            links += f'<a href="{href}">{esc(label)}</a>'
        cols += f'<div class="foot-col"><h4>{esc(item["label"])}</h4>{links}</div>'
    return (f'<footer><div class="wrap"><div class="foot-grid">'
            f'<div class="foot-brand"><a href="index.html" class="brand"><img src="{LOGO}" alt="logo" style="height:44px"/>'
            f'<span class="brand-txt"><b style="color:#fff">VAN OSB KOLEJİ</b><span>MESLEKİ &amp; TEKNİK</span></span></a>'
            f'<p>Doğu Anadolu\'da mesleki eğitimin yükselen değeri. Üretimle eğitimi birleştiren öncü kurum.</p>'
            f'<p style="margin-top:12px"><a href="https://ozelvanosbkoleji.com" style="color:#A7B8CB">ozelvanosbkoleji.com</a></p></div>'
            f'{cols}</div>'
            f'<div class="foot-bottom"><span>© 2025 ÖZEL VAN OSB MESLEKİ VE TEKNİK ANADOLU LİSESİ</span>'
            f'<span>VAN OSB · TÜRKİYE</span></div></div></footer>')

FOOT_SCRIPTS = '<script src="app.js"></script></body></html>'

def phero(data):
    img = data.get("hero_img", "")
    crumb = f'<a href="index.html">Anasayfa</a>'
    sec = data.get("section")
    if sec:
        crumb += f' / {esc(sec)}'
    crumb += f' / {esc(data.get("menu_title", data["title"]))}'
    title = esc(data["title"]).replace(" ", "<br/>", 1) if len(data["title"]) > 22 else esc(data["title"])
    return (f'<section class="phero"><div class="phero-bg"><img src="{img}" alt=""/></div>'
            f'<div class="grid-overlay"></div><div class="wrap">'
            f'<span class="eyebrow">{esc(data.get("eyebrow",""))}</span>'
            f'<h1>{title}</h1><div class="crumb">{crumb}</div></div></section>')

def render_blocks(blocks):
    out = ['<section class="sec"><div class="wrap"><div class="prose">']
    i = 0
    n = len(blocks)
    while i < n:
        b = blocks[i]
        t = b.get("type")
        if t == "h2":
            out.append(f'<h2 class="pr-h2">{esc(b["text"])}</h2>')
        elif t == "h3":
            out.append(f'<h3 class="pr-h3">{esc(b["text"])}</h3>')
        elif t == "p":
            out.append(f'<p>{esc(b["text"])}</p>')
        elif t == "lead":
            out.append(f'<p class="pr-lead">{esc(b["text"])}</p>')
        elif t == "note":
            out.append(f'<div class="pr-note">{esc(b["text"])}</div>')
        elif t == "empty":
            out.append(f'<div class="empty-state"><div class="empty-ic">{CHECK}</div><p>{esc(b["text"])}</p></div>')
        elif t == "vacancies":
            label = b.get("label", "")
            cards = ""
            for _ in range(int(b.get("count", 1))):
                cards += ('<div class="staff-card vacant"><div class="staff-photo noimg vac"><span>—</span></div>'
                          f'<div class="staff-info"><b>Boş</b><span>{esc(label)}</span></div></div>')
            out.append(f'<div class="staff-grid vac-grid">{cards}</div>')
        elif t == "list":
            title = f'<h3 class="pr-h3">{esc(b["title"])}</h3>' if b.get("title") else ""
            items = "".join(f'<li>{CHECK}<span>{esc(x)}</span></li>' for x in b["items"])
            out.append(f'{title}<ul class="pr-list">{items}</ul>')
        elif t == "iconlist":
            title = f'<h3 class="pr-h3">{esc(b["title"])}</h3>' if b.get("title") else ""
            items = "".join(f'<li>{CHECK}<span>{esc(x)}</span></li>' for x in b["items"])
            out.append(f'{title}<ul class="pr-list two-col">{items}</ul>')
        elif t == "tags":
            items = "".join(f'<span>{esc(x)}</span>' for x in b["items"])
            out.append(f'<div class="pr-tags">{items}</div>')
        elif t == "image":
            out.append(f'<figure class="pr-img"><img loading="lazy" src="{b["src"]}" alt=""/></figure>')
        elif t == "cards":
            cards = ""
            for c in b["items"]:
                cards += (f'<div class="pr-card"><div class="pr-card-n">{esc(c.get("n",""))}</div>'
                          f'<h4>{esc(c["h"])}</h4><p>{esc(c["p"])}</p></div>')
            out.append(f'<div class="pr-cards">{cards}</div>')
        elif t == "faq":
            items = ""
            for f in b["items"]:
                items += (f'<details class="faq"><summary>{esc(f["q"])} {CHEV}</summary>'
                          f'<div class="faq-a">{esc(f["a"])}</div></details>')
            out.append(f'<div class="faq-wrap">{items}</div>')
        elif t == "tree":
            steps = "".join(f'<li><span class="tstep">{esc(x)}</span></li>' for x in b["items"])
            out.append(f'<ol class="pr-tree">{steps}</ol>')
        elif t == "flow":
            steps = ""
            for idx, x in enumerate(b["items"], 1):
                steps += f'<li><span class="fnum">{idx:02d}</span><span>{esc(x)}</span></li>'
            out.append(f'<ol class="pr-flow">{steps}</ol>')
        elif t == "gallery":
            imgs = "".join(f'<a href="{u}" target="_blank" rel="noopener"><img loading="lazy" src="{u}" alt=""/></a>' for u in b["items"])
            out.append(f'<div class="pr-gallery">{imgs}</div>')
        elif t == "press":
            cards = ""
            for it in b["items"]:
                date = f'<span class="pnews-date">{esc(it["date"])}</span>' if it.get("date") else ""
                cards += (f'<a class="pnews" href="{it["url"]}" target="_blank" rel="noopener">'
                          f'<div class="pnews-top"><span class="pnews-src">{esc(it["source"])}</span>{date}</div>'
                          f'<h3>{esc(it["title"])}</h3>'
                          f'<span class="pnews-go">Habere git {ARROW}</span></a>')
            out.append(f'<div class="pnews-grid">{cards}</div>')
        i += 1
    out.append('</div></div></section>')
    return "".join(out)

def render_staff(data):
    out = ['<section class="sec"><div class="wrap"><div class="prose">']
    if data.get("intro"):
        out.append(f'<p class="pr-lead">{esc(data["intro"])}</p>')
    for g in data["staff_groups"]:
        out.append(f'<h2 class="pr-h2">{esc(g["title"])}</h2><div class="staff-grid">')
        for p in g["people"]:
            img = p.get("img") or ""
            if img:
                photo = f'<div class="staff-photo"><img loading="lazy" src="{img}" alt="{esc(p["name"])}"/></div>'
            else:
                initials = "".join(w[0] for w in p["name"].split()[:2]).upper()
                photo = f'<div class="staff-photo noimg"><span>{esc(initials)}</span></div>'
            out.append(f'<div class="staff-card">{photo}<div class="staff-info"><b>{esc(p["name"])}</b><span>{esc(p["role"])}</span></div></div>')
        out.append('</div>')
    out.append('</div></div></section>')
    return "".join(out)

CTA = ('<section class="cta-band"><div class="grid-overlay"></div><div class="wrap"><div class="cta-inner reveal">'
       '<span class="eyebrow">Kayıt &amp; İletişim</span>'
       '<h2>Ailemize <span class="amber">katılın</span></h2>'
       '<p>Kampüsümüzü görmek ve kayıt süreci hakkında bilgi almak için bize ulaşın.</p>'
       f'<a href="iletisim.html" class="btn btn-primary">İletişime Geç {ARROW}</a></div></div></section>')

def content_page(data, active):
    body = phero(data)
    if "staff_groups" in data:
        body += render_staff(data)
    else:
        # optional stats strip
        if data.get("stats"):
            cells = ""
            for i, s in enumerate(data["stats"], 1):
                u = f'<span class="u">{esc(s["u"])}</span>' if s.get("u") else ""
                cells += (f'<div class="stat"><span class="code">A-{i:02d}</span>'
                          f'<div class="num">{esc(s["num"])}{u}</div><div class="lbl">{esc(s["lbl"])}</div></div>')
            body += f'<section class="stats"><div class="wrap"><div class="stats-grid">{cells}</div></div></section>'
        body += render_blocks(data["blocks"])
    body += CTA
    title = f'{data["title"]} — Van OSB Koleji'
    return head(title) + header(active) + body + footer() + FOOT_SCRIPTS

# --- section key mapping for active state ---
SECTION_KEY = {"Okulumuz": "okulumuz", "Bölümler": "bolumler", "Eğitim ve Akademik": "egitim",
               "Projeler": "projeler", "Galeri": "galeri", "Duyurular": "duyurular"}

def overview_page(item, intro, hero):
    key = item["key"]
    body = []
    body.append(f'<section class="phero"><div class="phero-bg"><img src="{hero}" alt=""/></div>'
                f'<div class="grid-overlay"></div><div class="wrap">'
                f'<span class="eyebrow">{esc(item["label"])}</span><h1>{esc(item["label"])}</h1>'
                f'<div class="crumb"><a href="index.html">Anasayfa</a> / {esc(item["label"])}</div></div></section>')
    body.append(f'<section class="sec"><div class="wrap"><div class="sec-head reveal">'
                f'<span class="eyebrow dark">Genel Bakış</span><p style="margin-top:16px">{esc(intro)}</p></div>')
    body.append('<div class="ov-grid">')
    for idx, (label, href) in enumerate(item["children"], 1):
        body.append(f'<a href="{href}" class="ov-card reveal"><span class="ov-n">{idx:02d}</span>'
                    f'<h3>{esc(label)}</h3><span class="ov-go">İncele {ARROW}</span></a>')
    body.append('</div></div></section>')
    return head(f'{item["label"]} — Van OSB Koleji') + header(key) + "".join(body) + CTA + footer() + FOOT_SCRIPTS

OVERVIEW_INTRO = {
    "okulumuz": ("Tarihçemizden misyon ve vizyonumuza, yönetim kadromuzdan fiziki donanımımıza kadar okulumuzu tüm yönleriyle tanıyın.",
                 "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/resadegm-sergadegsadeg-H25wZBkkN9tIK3Id.jpg"),
    "bolumler": ("Bilişim, Elektrik-Elektronik, Kimya ve Gıda teknolojisi alanlarında sektöre entegre, uygulama ağırlıklı eğitim.",
                 "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/lab3-Awv8glR3l0S1xnwq.jpg"),
    "egitim": ("Hedeflerimiz, başarılarımız, rehberlik hizmetlerimiz ve akademik çalışma modelimiz.",
               "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/labsiyah-YD0EQRWPP7TZwXgB.jpg"),
    "projeler": ("TÜBİTAK, Erasmus ve AB projelerinden sosyal sorumluluğa, stajdan Ar-Ge çalışmalarına projelerimiz.",
                 "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/elektrik-mxB2oPReagIyabpO.jpeg"),
    "duyurular": ("Güncel duyurular, indirilebilir dökümanlar ve haftalık yemek listesi.",
                  "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/osbbinasi-AQEePlgwBWIgZbMA.webp"),
}

def get_item(key):
    for it in NAV:
        if it["key"] == key:
            return it
    return None

DEPTS = [
    ("BT · 01", "Bilişim Teknolojileri", "Yazılım, ağ sistemleri ve donanım üzerine uygulamalı eğitim.", "bilisim-teknolojileri.html",
     "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=768,fit=crop/YD0Eeq404vF5okpN/lab3-Awv8glR3l0S1xnwq.jpg"),
    ("EE · 02", "Elektrik-Elektronik Teknolojisi", "Endüstriyel elektrik, otomasyon ve elektronik sistemler.", "elektrik-elektronik.html",
     "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=768,fit=crop/YD0Eeq404vF5okpN/elektrik-mxB2oPReagIyabpO.jpeg"),
    ("KT · 03", "Kimya Teknolojisi", "Laboratuvar analizleri, proses kimyası ve kalite kontrol.", "kimya-teknolojisi.html",
     "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=768,fit=crop/YD0Eeq404vF5okpN/labsiyah-YD0EQRWPP7TZwXgB.jpg"),
    ("GT · 04", "Gıda Teknolojisi", "Gıda üretimi, güvenliği ve analiz süreçleri.", "gida-teknolojisi.html",
     "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=768,fit=crop/YD0Eeq404vF5okpN/whatsapp-image-2025-11-18-at-15.06.40-UyqITqKxlGCZNpUU.jpeg"),
]

def dept_cards():
    out = ['<div class="dept-grid">']
    for code, title, desc, href, img in DEPTS:
        out.append(f'<a href="{href}" class="dept reveal"><div class="dept-img"><img loading="lazy" src="{img}" alt="{esc(title)}"/></div>'
                   f'<span class="code">{esc(code)}</span><div class="dept-body"><h3>{esc(title)}</h3><p>{esc(desc)}</p>'
                   f'<span class="arrow"><span>Detay</span> {ARROW}</span></div></a>')
    out.append('</div>')
    return "".join(out)

def home_page():
    hero_bg = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/resadegm-sergadegsadeg-H25wZBkkN9tIK3Id.jpg"
    b = []
    b.append(f'<section class="hero" id="top"><div class="hero-bg"><img src="{hero_bg}" alt="Van OSB Koleji" /></div>'
             '<div class="grid-overlay"></div>'
             '<div class="hero-tick tr mono">39°N · VAN OSB<br/>KURULUŞ 2018</div>'
             '<div class="hero-tick br mono">DOĞU ANADOLU\'DA MESLEKİ EĞİTİMİN YÜKSELEN DEĞERİ</div>'
             '<div class="wrap"><div class="hero-inner reveal">'
             '<span class="eyebrow">Özel Van OSB Mesleki ve Teknik Anadolu Lisesi</span>'
             '<h1>Üretimle<br/>Buluşan <span class="amber">Eğitim</span></h1>'
             '<p class="lead">Van Organize Sanayi Bölgesi\'nin tam kalbinde; tam donanımlı atölyeler, güçlü akademik kadro ve '
             'sektörle iç içe bir eğitim modeliyle geleceğin mesleklerine hazırlıyoruz.</p>'
             f'<div class="hero-actions"><a href="bolumler.html" class="btn btn-primary">Bölümlerimizi Keşfet {ARROW}</a>'
             '<a href="iletisim.html" class="btn btn-ghost">Kayıt İçin İletişim</a></div></div></div></section>')
    # stats
    stats = [("16.000","m²","Açık Kampüs Alanı"),("7.800","m²","Kapalı Eğitim Alanı"),("4","","Teknik Meslek Alanı"),("2018","","Kuruluş Yılı")]
    cells = ""
    for i,(num,u,lbl) in enumerate(stats,1):
        uu = f'<span class="u">{u}</span>' if u else ""
        cells += f'<div class="stat reveal"><span class="code">A-{i:02d}</span><div class="num">{num}{uu}</div><div class="lbl">{lbl}</div></div>'
    b.append(f'<section class="stats"><div class="wrap"><div class="stats-grid">{cells}</div></div></section>')
    # about
    b.append('<section class="sec about"><div class="wrap"><div class="about-grid">'
             '<div class="about-copy reveal"><span class="eyebrow dark">Hakkımızda</span>'
             '<h2 style="font-size:clamp(2rem,4.4vw,3.2rem);margin:18px 0 26px">Sanayinin içinde, geleceğin mesleklerine hazır</h2>'
             '<p>Van OSB Mesleki ve Teknik Koleji, <strong>2018 yılında</strong> Van Organize Sanayi Bölgesi içinde; bölgenin güçlü '
             'sanayici iş insanlarının ortak vizyonu ve mesleki eğitime duyduğu inançla kuruldu.</p>'
             '<p>Okulumuzda <strong>Bilişim, Elektrik-Elektronik, Kimya ve Gıda Teknolojisi</strong> alanlarında sektöre entegre, '
             'uygulama ağırlıklı bir eğitim modeli uygulanıyor.</p>'
             '<p>OSB ile iç içe konumumuz sayesinde öğrencilerimiz <strong>staj, proje, üretim ve istihdam</strong> süreçlerinde '
             'önemli bir avantaja sahip.</p>'
             f'<a href="okulumuz.html" class="btn btn-primary" style="margin-top:10px">Okulumuzu Tanıyın {ARROW}</a></div>'
             '<div class="about-media reveal"><div class="frame"></div><div class="main-img">'
             '<img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1024,h=1282,fit=crop/YD0Eeq404vF5okpN/ogrenci2-m7VDQRa7D1uq0vRD.jpg" alt="Öğrenciler" /></div>'
             '<div class="badge"><b>%100</b><span>Uygulama Odaklı<br/>Eğitim Modeli</span></div></div></div></div></section>')
    # departments
    b.append('<section class="sec depts on-dark"><div class="wrap"><div class="sec-head reveal">'
             '<span class="eyebrow">Bölümlerimiz</span><h2>Dört alanda sektöre entegre eğitim</h2>'
             '<p>Her bölüm, tam donanımlı atölyeleri ve sanayi iş birlikleriyle öğrencilerini üretimin içine katar.</p></div>'
             + dept_cards() + '</div></section>')
    # why
    feats = [
        ("01","OSB Entegrasyonu","Sanayinin tam içindeyiz. Öğrenciler staj, proje ve üretimi gerçek işletmelerde deneyimler."),
        ("02","Güçlü Akademik Kadro","Deneyimli öğretmenler ve rehberlik servisiyle akademik başarıyı ve gelişimi destekliyoruz."),
        ("03","İstihdam Avantajı","Sektör bağları sayesinde mezunlar iş hayatına daha hızlı ve donanımlı adım atar."),
        ("04","TÜBİTAK & Erasmus","TÜBİTAK, Erasmus ve AB projeleriyle ulusal ve uluslararası ölçekte üretme fırsatı."),
        ("05","Modern Altyapı","Etkileşimli derslikler, laboratuvarlar, spor alanları, konferans salonu ve teknolojik ortamlar."),
        ("06","Değerlere Dayalı Kültür","Ahlaki değerleri önceleyen, üretmeyi öğreten ve öğrencisini hayata hazırlayan bir kültür."),
    ]
    fcards = ""
    for n,h,p in feats:
        fcards += f'<div class="feat reveal"><div class="n">{n}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
    b.append('<section class="sec why"><div class="wrap"><div class="sec-head reveal">'
             '<span class="eyebrow dark">Neden Van OSB Koleji</span><h2>Eğitimi üretimle birleştiren öncü kurum</h2>'
             '<p>Organize Sanayi Bölgesi ile iç içe konumumuz, öğrencilerimize akranlarının sahip olmadığı bir avantaj sağlar.</p></div>'
             f'<div class="why-grid">{fcards}</div></div></section>')
    b.append(CTA)
    return head("Özel Van OSB Mesleki ve Teknik Anadolu Lisesi — Üretimle Buluşan Eğitim",
                "Van Organize Sanayi Bölgesi içinde, üretim odaklı atölyeleri ve güçlü akademik kadrosuyla nitelikli mesleki eğitim.") \
        + header("home") + "".join(b) + footer() + FOOT_SCRIPTS

def bolumler_page():
    it = get_item("bolumler")
    body = (f'<section class="phero"><div class="phero-bg"><img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/lab3-Awv8glR3l0S1xnwq.jpg" alt=""/></div>'
            '<div class="grid-overlay"></div><div class="wrap"><span class="eyebrow">Bölümlerimiz</span>'
            '<h1>Dört Teknik<br/>Alan</h1><div class="crumb"><a href="index.html">Anasayfa</a> / Bölümler</div></div></section>'
            '<section class="sec depts on-dark"><div class="wrap"><div class="sec-head reveal">'
            '<span class="eyebrow">Bölümlerimiz</span><h2>Sektöre entegre, uygulama ağırlıklı</h2>'
            '<p>Her bölüm, tam donanımlı atölyeleri ve sanayi iş birlikleriyle öğrencilerini üretimin içine katar.</p></div>'
            + dept_cards() + '</div></section>')
    return head("Bölümlerimiz — Van OSB Koleji") + header("bolumler") + body + CTA + footer() + FOOT_SCRIPTS

def galeri_page():
    imgs = [
        "whatsapp-image-2025-11-18-at-15.04.43-trO1cqp13L7Ecfuq.jpeg",
        "elektrik-mxB2oPReagIyabpO.jpeg","labsiyah-YD0EQRWPP7TZwXgB.jpg",
        "whatsapp-image-2025-11-18-at-15.06.40-UyqITqKxlGCZNpUU.jpeg",
        "lab3-Awv8glR3l0S1xnwq.jpg","ogrenci4-Yle4gwRoPLcZ9Gny.jpg",
        "osbbinasi-AQEePlgwBWIgZbMA.webp","whatsapp-image-2025-11-18-at-15.03.11-9TYjnn4Lc1o1INCl.jpeg",
        "ogrenci2-m7VDQRa7D1uq0vRD.jpg","resadegm-sergadegsadeg-H25wZBkkN9tIK3Id.jpg",
    ]
    base = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=768,fit=crop/YD0Eeq404vF5okpN/"
    grid = "".join(f'<a href="{base}{u}" target="_blank" rel="noopener"><img loading="lazy" src="{base}{u}" alt=""/></a>' for u in imgs)
    subcards = ('<div class="ov-grid" style="margin-top:40px">'
                f'<a href="etkinliklerimiz.html" class="ov-card reveal"><span class="ov-n">01</span><h3>Etkinliklerimiz</h3><span class="ov-go">İncele {ARROW}</span></a>'
                f'<a href="okulumuzdan-kareler.html" class="ov-card reveal"><span class="ov-n">02</span><h3>Okulumuzdan Kareler</h3><span class="ov-go">İncele {ARROW}</span></a>'
                '</div>')
    body = (f'<section class="phero"><div class="phero-bg"><img src="{base}elektrik-mxB2oPReagIyabpO.jpeg" alt=""/></div>'
            '<div class="grid-overlay"></div><div class="wrap"><span class="eyebrow">Galeri</span>'
            '<h1>Okulumuzdan<br/>Kareler</h1><div class="crumb"><a href="index.html">Anasayfa</a> / Galeri</div></div></section>'
            f'<section class="sec gallery"><div class="wrap"><div class="pr-gallery gal-lg reveal">{grid}</div>{subcards}</div></section>')
    return head("Galeri — Van OSB Koleji") + header("galeri") + body + CTA + footer() + FOOT_SCRIPTS

def iletisim_page():
    body = (f'<section class="phero"><div class="phero-bg"><img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/YD0Eeq404vF5okpN/osbbinasi-AQEePlgwBWIgZbMA.webp" alt=""/></div>'
            '<div class="grid-overlay"></div><div class="wrap"><span class="eyebrow">Kayıt &amp; İletişim</span>'
            '<h1>Bize<br/>Ulaşın</h1><div class="crumb"><a href="index.html">Anasayfa</a> / İletişim</div></div></section>'
            '<section class="sec"><div class="wrap"><div class="contact-grid">'
            '<div class="reveal"><span class="eyebrow dark">İletişim Bilgileri</span>'
            '<h2 style="font-size:clamp(1.7rem,3.6vw,2.4rem);margin:16px 0 26px">Kayıt için hazır mısınız?</h2>'
            '<div class="info-card"><div class="ic"><svg viewBox="0 0 24 24" stroke-width="2" fill="none"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>'
            '<div><h4>Adres</h4><p>Van Organize Sanayi Bölgesi<br/>Van / Türkiye</p></div></div>'
            '<div class="info-card"><div class="ic"><svg viewBox="0 0 24 24" stroke-width="2" fill="none"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3-8.6A2 2 0 014.1 2h3a2 2 0 012 1.7c.1.9.4 1.8.7 2.6a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.5-1.2a2 2 0 012.1-.4c.8.3 1.7.6 2.6.7a2 2 0 011.7 2z"/></svg></div>'
            '<div><h4>Telefon</h4><p><a href="tel:+905302440565">0 (530) 244 05 65</a></p></div></div>'
            '<div class="info-card"><div class="ic"><svg viewBox="0 0 24 24" stroke-width="2" fill="none"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg></div>'
            '<div><h4>E-posta</h4><p><a href="mailto:info@ozelvanosbkoleji.com">info@ozelvanosbkoleji.com</a></p></div></div>'
            '<div class="info-card"><div class="ic"><svg viewBox="0 0 24 24" stroke-width="2" fill="none"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></div>'
            '<div><h4>Sosyal Medya</h4><p>Güncel etkinlikler ve duyurular için bizi takip edin.</p></div></div></div>'
            '<div class="reveal"><div class="form"><span class="eyebrow dark" style="margin-bottom:20px;display:inline-flex">Başvuru Formu</span>'
            '<label for="ad">Ad Soyad</label><input id="ad" type="text" placeholder="Adınız ve soyadınız" />'
            '<label for="tel">Telefon</label><input id="tel" type="tel" placeholder="0 (5xx) xxx xx xx" />'
            '<label for="mail">E-posta</label><input id="mail" type="email" placeholder="ornek@eposta.com" />'
            '<label for="msg">Mesajınız</label><textarea id="msg" rows="4" placeholder="Hangi bölümle ilgileniyorsunuz?"></textarea>'
            '<button class="btn btn-primary" style="width:100%;justify-content:center" '
            'onclick="alert(\'Formu canlıya bağlamak için bir form servisi (Web3Forms/Formspree) eklenecek.\')">Başvuruyu Gönder</button></div></div></div>'
            '<iframe class="map-embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
            'src="https://www.google.com/maps?q=Van+Organize+Sanayi+B%C3%B6lgesi&output=embed"></iframe></div></section>')
    return head("İletişim — Van OSB Koleji") + header("okulumuz") + body + footer() + FOOT_SCRIPTS

def not_found():
    return (head("Sayfa Bulunamadı — Van OSB Koleji") + header("") +
            '<section class="hero" style="min-height:100vh"><div class="grid-overlay"></div><div class="wrap"><div class="hero-inner">'
            '<span class="eyebrow">Hata 404</span><h1 style="font-size:clamp(3rem,10vw,7rem)">Sayfa<br/><span class="amber">Bulunamadı</span></h1>'
            '<p class="lead">Aradığınız sayfa taşınmış veya kaldırılmış olabilir.</p>'
            f'<div class="hero-actions"><a href="index.html" class="btn btn-primary">Anasayfaya Dön {ARROW}</a></div></div></div></section>'
            + footer() + FOOT_SCRIPTS)

# ---------- BUILD ----------
def main():
    # content pages from data
    files = sorted(os.listdir(DATA))
    slug_to_active = {}
    for it in NAV:
        for _, href in it.get("children", []):
            slug_to_active[href[:-5]] = it["key"]
    for fn in files:
        if not fn.endswith(".json"):
            continue
        data = json.load(open(os.path.join(DATA, fn), encoding="utf-8"))
        slug = data["slug"]
        active = slug_to_active.get(slug, SECTION_KEY.get(data.get("section"), ""))
        htmlpage = content_page(data, active)
        open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8").write(htmlpage)

    # overview landing pages
    for key in ["okulumuz", "egitim", "projeler", "duyurular"]:
        it = get_item(key)
        intro, hero = OVERVIEW_INTRO[key]
        open(os.path.join(ROOT, it["href"]), "w", encoding="utf-8").write(overview_page(it, intro, hero))

    # special pages
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(home_page())
    open(os.path.join(ROOT, "bolumler.html"), "w", encoding="utf-8").write(bolumler_page())
    open(os.path.join(ROOT, "galeri.html"), "w", encoding="utf-8").write(galeri_page())
    open(os.path.join(ROOT, "iletisim.html"), "w", encoding="utf-8").write(iletisim_page())
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(not_found())

    print("all pages generated")

if __name__ == "__main__":
    main()
