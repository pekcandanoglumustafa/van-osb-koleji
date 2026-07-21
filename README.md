# Van OSB Mesleki ve Teknik Koleji — Web Sitesi

Statik, çok sayfalı web sitesi. Kurulum gerektirmez (build yok), doğrudan Vercel'e yüklenir.

## Sayfalar
- `index.html` — Anasayfa
- `okulumuz.html` — Tarihçe, misyon-vizyon, değerler, donanım
- `bolumler.html` — 4 bölüm detayı (Bilişim, Elektrik-Elektronik, Kimya, Gıda)
- `galeri.html` — Fotoğraf galerisi
- `iletisim.html` — İletişim + başvuru formu + harita
- `404.html` — Hata sayfası

## Vercel'e Deploy (2 yol)

### Yol 1 — En hızlı (sürükle-bırak)
1. https://vercel.com adresine gir, giriş yap.
2. "Add New… → Project" yerine, "Deploy" ekranında bu klasörün **içeriğini** (index.html dahil tüm dosyalar) sürükle bırak.
3. Bitince Vercel bir `.vercel.app` adresi verir.

### Yol 2 — GitHub + Vercel (senin normal akışın)
1. Bu klasörü bir GitHub reposuna push et:
   ```
   git init
   git add .
   git commit -m "Van OSB Koleji sitesi"
   git branch -M main
   git remote add origin https://github.com/KULLANICI/van-osb-koleji.git
   git push -u origin main
   ```
2. Vercel → "Add New… → Project" → repoyu seç → "Deploy".
3. Framework: **Other** (build ayarı gerekmez, statik).

### Kendi alan adın (ozelvanosbkoleji.com)
Vercel → Project → Settings → Domains → alan adını ekle, DNS kayıtlarını yönlendir.

## Yapılacaklar (senin düzenlemen için)
- İletişim bilgileri: `iletisim.html` ve `footer.js` içindeki telefon / e-posta / adres placeholder'ları.
- Başvuru formunu canlıya bağlamak için Formspree veya Web3Forms (ücretsiz) ekleyebiliriz.
- Görseller şu an mevcut sitenin CDN'inden (zyrosite) çekiliyor; istersen kendi klasörüne indirip yerelleştiririz.
