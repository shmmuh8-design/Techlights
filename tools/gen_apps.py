# يولّد صفحة لكل تطبيق: techlights.app/<id>/
# التشغيل: python3 tools/gen_apps.py
import os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GH = 'https://shmmuh8-design.github.io/'

APPS = [
  dict(id='manakh', repo='manakh-app', store='https://apps.apple.com/app/id6823329197', web='',
       color='#28408a', name=['مناخ', 'Manakh'], one=['الطقس والفلك والأنواء', 'Weather, astronomy & Anwaa'],
       desc=['طقس ولايتك لحظة بلحظة، مواقيت الصلاة والقبلة، الأنواء والتقويم الفلكي، المد والجزر، ورادار الأقمار الصناعية.',
             'Live weather for your wilayat, prayer times and qibla, the traditional Anwaa calendar, tides, and a live satellite radar.'],
       feats=[['🌤️', 'طقس ولايتك بالساعة ولأيام', 'Hourly and daily weather for your wilayat'],
              ['🕌', 'مواقيت الصلاة واتجاه القبلة', 'Prayer times and qibla direction'],
              ['🌙', 'الأنواء والطوالع والتقويم الفلكي', 'Anwaa seasons and astronomical calendar'],
              ['🌊', 'المد والجزر والرياح للبحّارة', 'Tides and wind for sailors and fishermen'],
              ['🛰️', 'رادار الأقمار الصناعية فوقك الحين', 'Live radar of satellites overhead'],
              ['🔔', 'تنبيهات الطقس والصلاة', 'Weather and prayer notifications']]),
  dict(id='suqya', repo='Suqya', store='https://apps.apple.com/app/id6824513927', web=GH + 'Suqya/',
       color='#0f5f6e', name=['سُقيا', 'Suqya'], one=['صهريج ماي لين باب بيتك', 'Water tanker to your door'],
       desc=['اختار ولايتك وحجم الصهريج، وشوف أقرب الصهاريج وأسعارها، واطلب باتصال أو واتساب.',
             'Pick your wilayat and tank size, compare nearby water tankers and their prices, and order by call or WhatsApp.'],
       feats=[['📍', 'الصهاريج حسب ولايتك', 'Tankers by wilayat'],
              ['💧', 'أحجام وأسعار واضحة', 'Clear sizes and prices'],
              ['💬', 'اطلب بالاتصال أو الواتساب', 'Order by call or WhatsApp'],
              ['🚚', 'سجّل صهريجك كمورّد', 'List your tanker as a supplier']]),
  dict(id='khidmati', repo='Khidmati', store='', web=GH + 'Khidmati/',
       color='#1d56c9', name=['خدماتي', 'Khidmati'], one=['صيانة المنازل', 'Home maintenance'],
       desc=['مؤسسات وفنيين للتكييف والكهرباء والسباكة والنجارة وغيرها، في كل الولايات، وتتواصل معهم مباشرة.',
             'Companies and technicians for AC, electrical, plumbing, carpentry and more across Oman. Contact them directly.'],
       feats=[['❄️', 'مكيفات وكهرباء وسباكة', 'AC, electrical and plumbing'],
              ['🏢', 'مؤسسات مرخّصة بسجل تجاري', 'Licensed companies with a CR'],
              ['⭐', 'تقييمات من الزبائن', 'Customer ratings'],
              ['📞', 'تواصل مباشر بدون وسيط', 'Direct contact, no middleman']]),
  dict(id='rukhsati', repo='rukhsati', store='', web=GH + 'rukhsati/',
       color='#2b3945', name=['رخصتي', 'Rukhsati'], one=['تعليم السياقة', 'Driving lessons'],
       desc=['معلّمين ومعلّمات سياقة في ولايتك، أسعار واضحة، وطلب حصص بالواتساب، أو سجّل طلبك وخلّهم يتواصلون معك.',
             'Driving instructors in your wilayat with clear prices. Request lessons on WhatsApp, or post a request and let them contact you.'],
       feats=[['📍', 'معلّمين حسب ولايتك', 'Instructors by wilayat'],
              ['⚙️', 'عادي أو أوتوماتيك', 'Manual or automatic'],
              ['💰', 'قارن أسعار الحصص', 'Compare lesson prices'],
              ['🎓', 'سجّل طلبك كمتعلّم', 'Post a request as a learner']]),
  dict(id='mandoos', repo='mandoos', store='https://apps.apple.com/app/id6826308408', web=GH + 'mandoos/',
       color='#7a3412', name=['المندوس', 'Al Mandoos'], one=['سوق التراث والمقتنيات', 'Heritage & antiques market'],
       desc=['بيع وشراء التراث العُماني والمقتنيات القديمة: خناجر، فضيات، مناديس وتحف، بين البائع والمشتري مباشرة.',
             'Buy and sell Omani heritage and collectibles: khanjars, silver, chests and antiques, directly between buyer and seller.'],
       feats=[['🗡️', 'خناجر وسيوف', 'Khanjars and swords'],
              ['💍', 'فضيات وحُلي', 'Silver and jewellery'],
              ['📸', 'أعلن عن قطعتك مجانًا', 'List your item for free'],
              ['💬', 'تواصل مباشر مع البائع', 'Contact the seller directly']]),
]

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.3 1.2 9.7.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.1-.8s1.9.8 3.2.8c1.3 0 2.1-1.2 2.9-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.4-.9-2.4-3.8zM14 5.6c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.1-.6 2.8-1.4z"/></svg>'

def bi(ar, en, tag='span', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} data-ar="{html.escape(ar)}" data-en="{html.escape(en)}">{html.escape(ar)}</{tag}>'

def page(a):
    base = GH + a['repo'] + '/'
    others = [o for o in APPS if o['id'] != a['id']]
    store = (f'<a class="btn store" href="{a["store"]}" target="_blank" rel="noopener">{APPLE}{bi("حمّله من App Store", "Download on the App Store")}</a>'
             if a['store'] else f'<span class="btn store off">{APPLE}{bi("قريبًا في App Store", "Coming soon to the App Store")}</span>')
    web = f'<a class="btn ghost" href="{a["web"]}" target="_blank" rel="noopener">{bi("جرّبه على الويب", "Try it on the web")}</a>' if a['web'] else ''
    feats = ''.join(f'<div class="f"><i>{e}</i>{bi(ar, en, "b")}</div>' for e, ar, en in a['feats'])
    more = ''.join(f'<a class="o" href="../{o["id"]}/"><img src="../icons/{o["id"]}.png" alt="" loading="lazy">{bi(o["name"][0], o["name"][1])}</a>' for o in others)
    return f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{a["name"][0]} · أضواء التقنية</title>
<meta name="description" content="{html.escape(a["desc"][0])}">
<meta name="theme-color" content="#07060f">
<link rel="icon" href="../icons/{a["id"]}.png">
<link rel="apple-touch-icon" href="../icons/{a["id"]}.png">
<meta property="og:title" content="{a["name"][0]} — {html.escape(a["one"][0])}">
<meta property="og:description" content="{html.escape(a["desc"][0])}">
<meta property="og:image" content="https://techlights.app/icons/{a["id"]}.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@500;700;800&display=swap">
<style>
:root{{--bg:#07060f;--card:#14122a;--line:rgba(255,255,255,.09);--fg:#f3f1ff;--muted:#a7a3c7;--p:#7c5cff;--p2:#b06bff;--app:{a["color"]}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font-family:Cairo,system-ui,sans-serif;line-height:1.6;overflow-x:hidden}}
body.en{{font-family:Inter,Cairo,system-ui,sans-serif}}
a{{color:inherit;text-decoration:none}}
.wrap{{width:min(880px,100%);margin:auto;padding:0 16px}}
.sky{{position:fixed;inset:0;z-index:-1;background:radial-gradient(70% 45% at 50% 0%,color-mix(in srgb,var(--app) 70%,transparent),transparent 75%),radial-gradient(50% 40% at 100% 30%,rgba(176,107,255,.18),transparent 70%),var(--bg)}}
nav{{position:sticky;top:0;z-index:5;backdrop-filter:blur(14px);background:rgba(7,6,15,.6);border-bottom:1px solid var(--line);padding-top:env(safe-area-inset-top)}}
nav .wrap{{display:flex;align-items:center;gap:12px;height:62px}}
.brand{{display:flex;align-items:center;gap:9px;font-weight:900;white-space:nowrap}}
.brand img{{width:34px;height:34px}}
.lang{{margin-inline-start:auto;border:0;background:linear-gradient(135deg,var(--p),var(--p2));color:#fff;border-radius:999px;padding:7px 15px;font:800 .85rem Inter,Cairo;cursor:pointer}}
.hero{{text-align:center;padding:48px 0 26px}}
.hero .ic{{width:128px;height:128px;border-radius:30px;box-shadow:0 24px 60px rgba(0,0,0,.55),0 0 0 1px var(--line)}}
h1{{font-size:clamp(2.4rem,9vw,3.6rem);line-height:1.15;margin:18px 0 4px;font-weight:900}}
.one{{color:#d9d4ff;font-size:1.25rem;font-weight:700;margin:0}}
.desc{{color:var(--muted);font-size:1.08rem;max-width:36em;margin:14px auto 0}}
.cta{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:26px}}
.btn{{display:inline-flex;align-items:center;gap:10px;border-radius:14px;padding:13px 22px;font-weight:800;border:1px solid var(--line)}}
.btn svg{{width:22px;height:22px}}
.btn.store{{background:#fff;color:#0b0a16;border:0}}
.btn.store.off{{background:rgba(255,255,255,.1);color:var(--muted)}}
.btn.ghost{{background:rgba(255,255,255,.05)}}
.feats{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:34px 0}}
@media (max-width:560px){{.feats{{grid-template-columns:1fr}}}}
.f{{display:flex;align-items:center;gap:14px;background:linear-gradient(180deg,var(--card),#100e22);border:1px solid var(--line);border-radius:18px;padding:16px 18px}}
.f i{{font-style:normal;font-size:1.6rem;width:48px;height:48px;flex:none;display:grid;place-items:center;border-radius:14px;background:color-mix(in srgb,var(--app) 55%,#14122a)}}
.f b{{font-size:1.02rem}}
.links{{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin:8px 0 40px}}
.links a{{border:1px solid var(--line);background:rgba(255,255,255,.04);border-radius:999px;padding:8px 16px;font-weight:700;font-size:.92rem;color:#d6ccff}}
h2{{font-size:1.4rem;margin:0 0 14px;font-weight:900}}
.more{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:40px}}
@media (max-width:560px){{.more{{grid-template-columns:repeat(2,1fr)}}}}
.o{{display:flex;align-items:center;gap:10px;border:1px solid var(--line);border-radius:16px;padding:10px;background:rgba(255,255,255,.03);font-weight:800}}
.o img{{width:40px;height:40px;border-radius:11px}}
footer{{color:var(--muted);text-align:center;padding:10px 0 calc(30px + env(safe-area-inset-bottom));font-size:.9rem;border-top:1px solid var(--line)}}
footer a{{color:#d6ccff}}
</style>
</head>
<body>
<div class="sky" aria-hidden="true"></div>
<nav><div class="wrap">
  <a class="brand" href="../"><img src="../logo.svg" alt="">{bi("أضواء التقنية", "TechLights")}</a>
  <button class="lang" id="lang" type="button">English</button>
</div></nav>
<main class="wrap">
  <section class="hero">
    <img class="ic" src="../icons/{a["id"]}.png" alt="">
    {bi(a["name"][0], a["name"][1], "h1")}
    {bi(a["one"][0], a["one"][1], "p", "one")}
    {bi(a["desc"][0], a["desc"][1], "p", "desc")}
    <div class="cta">{store}{web}</div>
  </section>
  <section class="feats">{feats}</section>
  <div class="links">
    <a href="{base}privacy.html" target="_blank" rel="noopener">{bi("🔒 سياسة الخصوصية", "🔒 Privacy policy")}</a>
    <a href="mailto:design.omani1@gmail.com">✉️ design.omani1@gmail.com</a>
    <a href="https://wa.me/96894005400" target="_blank" rel="noopener">{bi("💬 واتساب الدعم", "💬 WhatsApp support")}</a>
  </div>
  {bi("تطبيقات ثانية من أضواء التقنية", "More apps from TechLights", "h2")}
  <section class="more">{more}</section>
</main>
<footer>© 2026 <a href="../">{bi("أضواء التقنية · مسقط، سلطنة عُمان", "TechLights · Muscat, Oman")}</a></footer>
<script>
const NAME = {json.dumps(a["name"], ensure_ascii=False)};
let EN = /^en/i.test(navigator.language || '') && !/^ar/i.test(navigator.language || '');
try{{ const s = localStorage.getItem('tl-lang'); if(s) EN = s === 'en'; }}catch(e){{}}
function applyLang(){{
  document.documentElement.lang = EN ? 'en' : 'ar'; document.documentElement.dir = EN ? 'ltr' : 'rtl'; document.body.classList.toggle('en', EN);
  document.querySelectorAll('[data-ar]').forEach(n => n.textContent = EN ? n.dataset.en : n.dataset.ar);
  document.getElementById('lang').textContent = EN ? 'العربية' : 'English';
  document.title = NAME[EN ? 1 : 0] + (EN ? ' · TechLights' : ' · أضواء التقنية');
}}
document.getElementById('lang').onclick = () => {{ EN = !EN; try{{ localStorage.setItem('tl-lang', EN ? 'en' : 'ar'); }}catch(e){{}} applyLang(); }};
applyLang();
</script>
</body>
</html>
'''

for a in APPS:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(a))
print('ok', [a['id'] for a in APPS])
