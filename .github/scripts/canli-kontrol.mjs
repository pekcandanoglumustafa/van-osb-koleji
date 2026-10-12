// Canli siteyi gercek tarayiciyla acar; kirik gorsel / eski Zyro baglantisi varsa hata verir.
// Kullanim: node .github/scripts/canli-kontrol.mjs https://ozelvanosbkoleji.com
import { chromium } from 'playwright';
import fs from 'node:fs';

const BASE = (process.argv[2] || 'https://ozelvanosbkoleji.com').replace(/\/$/, '');
const pages = fs.readdirSync('.').filter(f => f.endsWith('.html')).sort()
  .map(f => (f === 'index.html' ? '/' : '/' + f.replace(/\.html$/, '')));
fs.mkdirSync('canli-kontrol', { recursive: true });

const browser = await chromium.launch();
const problems = [];
let imgTotal = 0;
for (const path of pages) {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const bad = new Set();
  page.on('response', r => {
    if (r.request().resourceType() === 'image' && r.status() >= 400) bad.add(`${r.status()} ${r.url()}`);
  });
  page.on('requestfailed', r => { if (r.resourceType() === 'image') bad.add(`FAIL ${r.url()}`); });
  let status = 0;
  try {
    const resp = await page.goto(BASE + path + '?kontrol=' + Date.now(), { waitUntil: 'load', timeout: 60000 });
    status = resp ? resp.status() : 0;
    await page.addStyleTag({ content: '.reveal{opacity:1!important;transform:none!important}' });
    // tembel (lazy) gorselleri hemen yukle ve hepsinin bitmesini bekle
    await page.evaluate(async () => {
      document.querySelectorAll('img[loading="lazy"]').forEach(i => { i.loading = 'eager'; });
      await Promise.race([
        Promise.all([...document.images].map(i => i.complete ? null : new Promise(r => { i.onload = i.onerror = r; }))),
        new Promise(r => setTimeout(r, 20000)),
      ]);
    });
    await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {});
    const info = await page.evaluate(() => ({
      imgs: document.images.length,
      broken: [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.currentSrc || i.src),
      zyro: /zyrosite|weserv/.test(document.documentElement.outerHTML),
      logo: !!document.querySelector('#hdr .brand img, #hdr .brand .brand-mark'),
    }));
    imgTotal += info.imgs;
    info.broken.forEach(u => bad.add('BROKEN ' + u));
    if (info.zyro) bad.add('eski Zyro/weserv baglantisi hala sayfada');
    if (!info.logo) bad.add('logo alani yok');
    if (['/', '/bolumler', '/galeri', '/ogretmen-kadrosu', '/yonetim-kadrosu'].includes(path)) {
      await page.screenshot({ path: `canli-kontrol/${path === '/' ? 'index' : path.slice(1)}.png`, fullPage: true });
    }
  } catch (e) {
    bad.add('sayfa acilamadi: ' + e.message.split('\n')[0]);
  }
  if (status >= 400) bad.add(`sayfa HTTP ${status}`);
  if (bad.size) problems.push({ path, bad: [...bad] });
  console.log(`${bad.size ? 'HATA' : 'OK  '} ${path} (${status})${bad.size ? ' -> ' + [...bad].join(' | ') : ''}`);
  await page.close();
}
await browser.close();

const summary = `${pages.length} sayfa, ${imgTotal} gorsel kontrol edildi; ${problems.length} sayfada sorun var.`;
console.log(`::notice title=Canli site ozeti::${summary}`);
for (const p of problems.slice(0, 40)) {
  console.log(`::error title=${p.path}::${p.bad.slice(0, 6).join(' | ').replace(/[\r\n]/g, ' ')}`);
}
process.exit(problems.length ? 1 : 0);
