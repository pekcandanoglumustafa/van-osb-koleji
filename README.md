# Van OSB Mesleki ve Teknik Koleji — Web Sitesi

Statik, çok sayfalı web sitesi (build gerektirmez). Eski ozelvanosbkoleji.com sitesinin tüm sayfaları yeni tasarımla taşınmıştır.

## Yapı
- `index.html` — Anasayfa
- `okulumuz.html` (genel) → tarihce, misyon-vizyon, yonetim-kadrosu, kurum-kulturu, kurumsal-degerler, fiziksel-donanim, ogretmen-kadrosu, iletisim
- `bolumler.html` (genel) → bilisim-teknolojileri, elektrik-elektronik, kimya-teknolojisi, gida-teknolojisi
- `egitim-akademik.html` (genel) → hedeflerimiz, basarilarimiz, rehberlik-servisi, zumre-calismalari, akademik-takvim
- `projelerimiz.html` (genel) → tubitak-erasmus-ab, sosyal-sorumluluk, staj-isletme-egitimi, ar-ge-calismalari
- `galeri.html` (genel) → etkinliklerimiz, okulumuzdan-kareler
- `duyurular.html` (genel) → duyuru, dokumanlar, haftalik-yemek-listesi
- `iletisim.html`, `404.html`
- `style.css`, `app.js` — paylaşılan stil ve script
- `data/*.json` — sayfa içerikleri (kaynak)
- `build.py` — tüm HTML'i data/ ve şablondan üreten jeneratör

## İçeriği güncellemek
1. İlgili `data/<sayfa>.json` dosyasını düzenle.
2. `python3 build.py` çalıştır → HTML yeniden üretilir.
3. GitHub'a push et → Vercel otomatik deploy eder.

## Vercel
GitHub reposu Vercel'e bağlı olduğu için `main`'e her push otomatik yayınlanır.
Framework: **Other** (saf statik). `vercel.json` ile temiz URL'ler aktif.

## Yapılacaklar
- İletişim telefon/e-posta placeholder'ları (`build.py` içindeki `iletisim_page`).
- Başvuru formunu Web3Forms/Formspree ile canlıya bağlama.
- Öğretmen kadrosunda fotoğrafı olmayan birkaç kişi (İngilizce/Din Kültürü öğretmenleri) baş harflerle gösteriliyor; fotoğraf eklenebilir.
