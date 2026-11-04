# Generator stron Leśna Polana: python _src/build.py
import os, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'img')
KW = 'https://be-v2.kwhotel.com/pl/983dfe367e34387f0131b2655f2673be/0'
TEL = '+48883044142'; TEL_T = '+48 883 044 142'; MAIL = 'recepcja@lesna-polana.eu'
MAPS = 'https://maps.app.goo.gl/4xrkmw174LbVGUfX6'
FB = 'https://www.facebook.com/lesnapolanakrynica/'; IG = 'https://www.instagram.com/lesna_polana_krynica/'
V = '4'

def warianty(n):
    out = []
    for w in (640, 740, 1200, 1920):
        p = os.path.join(IMG, f'{n}-{w}.webp')
        if os.path.exists(p):
            out.append((w, Image.open(p).size))
    return out

def img(n, alt, sizes='100vw', cls='', lazy=True, glowny=None):
    v = warianty(n)
    if not v:
        raise SystemExit('brak obrazu ' + n)
    src_w = glowny if glowny else (1200 if any(w == 1200 for w, _ in v) else v[-1][0])
    src_w = min([w for w, _ in v], key=lambda w: abs(w - src_w))
    size = dict(v)[src_w]
    srcset = ', '.join(f'img/{n}-{w}.webp {w}w' for w, _ in v)
    a = f' class="{cls}"' if cls else ''
    l = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="img/{n}-{src_w}.webp" srcset="{srcset}" sizes="{sizes}" width="{size[0]}" height="{size[1]}" alt="{html.escape(alt)}"{a}{l}>'

def duzy(n):
    v = warianty(n)
    return f'img/{n}-{v[-1][0]}.webp'

I_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 3.5h3.2l1.6 4.3-2.1 1.4a11 11 0 0 0 7.1 7.1l1.4-2.1 4.3 1.6V19a1.6 1.6 0 0 1-1.7 1.6A16.6 16.6 0 0 1 3.4 5.2 1.6 1.6 0 0 1 5 3.5z"/></svg>'
I_KAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="1.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>'

def pieczec(id_, tlo='#1F3B2C', przezr=1):
    return f'''<svg viewBox="0 0 200 200" role="img" aria-label="100 lat Leśnej Polany, 1927-2027"><defs><path id="{id_}g" d="M34,100 a66,66 0 1,1 132,0"/><path id="{id_}d" d="M22,100 a78,78 0 0,0 156,0"/></defs>
<circle cx="100" cy="100" r="97" fill="{tlo}" fill-opacity="{przezr}" stroke="#E0B85A" stroke-width="1.6"/><circle cx="100" cy="100" r="90" fill="none" stroke="#E0B85A" stroke-width=".7"/><circle cx="100" cy="100" r="56" fill="none" stroke="#E0B85A" stroke-width=".7"/>
<text fill="#E0B85A" font-family="Lora, Georgia, serif" font-weight="600" font-size="14.5" letter-spacing="2.6"><textPath href="#{id_}g" startOffset="50%" text-anchor="middle">LEŚNA POLANA</textPath></text>
<text fill="#E0B85A" font-family="Lora, Georgia, serif" font-weight="600" font-size="14.5" letter-spacing="2.4"><textPath href="#{id_}d" startOffset="50%" text-anchor="middle">1927 - 2027</textPath></text>
<circle cx="27" cy="100" r="2.4" fill="#E0B85A"/><circle cx="173" cy="100" r="2.4" fill="#E0B85A"/>
<text x="100" y="109" text-anchor="middle" fill="#fff" font-family="Lora, Georgia, serif" font-weight="600" font-size="44">100</text>
<text x="100" y="130" text-anchor="middle" fill="#E0B85A" font-family="Lora, Georgia, serif" font-weight="500" font-size="14" letter-spacing="3">LAT</text></svg>'''

MENU = [('pokoje.html', 'Pokoje i ceny'), ('pobyty.html', 'Pobyty'), ('galeria.html', 'Galeria'), ('historia.html', 'Historia'), ('kontakt.html', 'Kontakt')]

def kw(tekst='Zarezerwuj pobyt', cls='btn', extra=''):
    return f'<a class="{cls}" href="{KW}" target="_blank" rel="noopener" data-kw{extra}>{tekst}</a>'

def naglowek(akt):
    m = ''.join(f'<a href="{h}"{" aria-current=page" if h == akt else ""}>{t}</a>' for h, t in MENU)
    return f'''<header class="top"><div class="wrap top-in">
<a class="marka" href="./" aria-label="Willa Leśna Polana - strona główna"><img src="img/logo-160.webp" width="160" height="157" alt=""><span><b>Willa Leśna Polana</b><small>Krynica-Zdrój</small></span></a>
<nav class="menu" aria-label="Menu główne">{m}</nav>
<div class="top-akcje"><a class="tel-top" href="tel:{TEL}">{I_TEL}<span>{TEL_T}</span></a>{kw('Zarezerwuj', 'btn btn-top')}
<a class="tel-ikona" href="tel:{TEL}" aria-label="Zadzwoń: {TEL_T}">{I_TEL}</a>
<button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="panel"><span></span></button></div>
</div></header>
<div class="panel" id="panel"><nav aria-label="Menu mobilne"><a href="./"{" aria-current=page" if akt == "./" else ""}>Strona główna</a>{m}</nav>
<div class="panel-dol">{kw('Zarezerwuj pobyt')}<a class="btn obrys" href="tel:{TEL}">{I_TEL}Zadzwoń {TEL_T}</a><p>ul. prof. H. Świdzińskiego 37, 33-380 Krynica-Zdrój<br><a class="link" href="mailto:{MAIL}">{MAIL}</a></p></div></div>'''

def stopka():
    return f'''<footer class="stopka"><div class="wrap">
<div class="stopka-g">
<div class="stopka-o"><div class="stopka-marka"><img src="img/logo-160.webp" width="160" height="157" alt="" loading="lazy"><div><b>Willa Leśna Polana</b><p>Since 1927. Wypoczynek, rekolekcje i pobyty grupowe na słonecznym stoku Jasiennika.</p></div></div></div>
<div><h3>Kontakt</h3><ul><li>ul. prof. H. Świdzińskiego 37<br>33-380 Krynica-Zdrój</li><li><a href="tel:{TEL}">{TEL_T}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{MAPS}" target="_blank" rel="noopener">Nawiguj do Leśnej Polany</a></li></ul></div>
<div><h3>Strony</h3><ul><li><a href="pokoje.html">Pokoje i ceny</a></li><li><a href="pobyty.html">Pobyty i oferty</a></li><li><a href="galeria.html">Galeria</a></li><li><a href="historia.html">Historia willi</a></li><li><a href="kontakt.html">Kontakt i dojazd</a></li></ul></div>
</div>
<div class="stopka-dol"><span>© Willa Leśna Polana w Krynicy-Zdroju</span><nav aria-label="Dodatkowe"><a href="regulamin.html">Regulamin</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><a href="{IG}" target="_blank" rel="noopener">Instagram</a></nav></div>
</div></footer>
<div class="mob" id="mob"><a class="btn obrys" href="tel:{TEL}">{I_TEL}Zadzwoń</a>{kw('Zarezerwuj pobyt')}</div>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Powiększone zdjęcie"><span class="lb-licz"></span><figure><img alt=""><figcaption></figcaption></figure>
<button class="lb-x" type="button" aria-label="Zamknij"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 5l14 14M19 5L5 19"/></svg></button>
<button class="lb-p" type="button" aria-label="Poprzednie"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M15 4l-8 8 8 8"/></svg></button>
<button class="lb-n" type="button" aria-label="Następne"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 4l8 8-8 8"/></svg></button></div>
<script src="app.js?v={V}" defer></script>'''

def strona(plik, tytul, opis, akt, tresc):
    doc = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{tytul}</title>
<meta name="description" content="{html.escape(opis)}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#1F3B2C">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/lora-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/ss3-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css?v={V}">
</head>
<body>
<a class="sr" href="#tresc">Przejdź do treści</a>
{naglowek(akt)}
<main id="tresc">
{tresc}
</main>
{stopka()}
</body>
</html>
'''
    with open(os.path.join(ROOT, plik), 'w', encoding='utf-8', newline='\n') as f:
        f.write(doc)

def ph_hero(foto, alt, h1, opis, okr, pos='50% 50%'):
    return f'''<section class="ph-hero">{img(foto, alt, lazy=False).replace('<img ', f'<img style="object-position:{pos}" ')}<div class="wrap"><p class="okruszki"><a href="./">Strona główna</a> / {okr}</p><h1>{h1}</h1><p>{opis}</p></div></section>'''

def cta_pas(foto='taras', h='Zapraszamy do Leśnej Polany', p='Wolne terminy i ceny na wybrane dni sprawdzisz od razu w systemie rezerwacji. Pobyty grupowe i rekolekcje ustalamy telefonicznie lub mailowo.'):
    return f'''<section class="cta-pas">{img(foto, '', sizes='100vw')}<div class="wrap"><h2>{h}</h2><p>{p}</p><div class="hero-cta">{kw('Zarezerwuj pobyt', 'btn jasny')}<a class="btn obrys-b" href="tel:{TEL}">{I_TEL}{TEL_T}</a></div></div></section>'''

# ---------- dane ----------
POKOJE = [
    dict(id='jednoosobowy', n='Pokój jednoosobowy', os='1 osoba', foto=['pokoj-1os', 'okno', 'lazienka'], cena=130, opis='Spokojny pokój dla jednej osoby, z biurkiem i garderobą. Dobry wybór na wyjazd leczniczy lub rekolekcje.', extra=[]),
    dict(id='dwuosobowy', n='Pokój dwuosobowy', os='2 osoby', foto=['pokoj-2os', 'pokoj-2os-b', 'lazienka-b'], cena=260, opis='Jasny pokój z naturalną drewnianą podłogą i łazienką z prysznicem. Najczęściej wybierany na wczasy i weekendy we dwoje.', extra=[]),
    dict(id='trzyosobowy', n='Pokój trzyosobowy', os='3 osoby', foto=['pokoj-3os', 'pokoj-3os-b', 'lazienka-c'], cena=370, opis='Pokoje na poddaszu z łukowymi oknami. Wygodne dla rodziny z dzieckiem albo trójki przyjaciół.', extra=[]),
    dict(id='rodzinny', n='Pokój rodzinny', os='4 osoby', foto=['pokoj-rodzinny', 'pokoj-rodzinny-b', 'pokoj-2os-c'], cena=490, opis='Przestronny pokój z dodatkową rozkładaną sofą, dla rodzin i małych grup.', extra=['rozkładana sofa']),
    dict(id='studio', n='Studio dwupokojowe', os='do 6 osób', foto=['studio'], cena=510, opis='Dwa pokoje i jedna łazienka. Wygoda dla rodziny, która chce mieć osobną sypialnię.', extra=['dwa pokoje']),
]
WYP = ['łazienka z prysznicem', 'suszarka do włosów', 'biurko', 'garderoba', 'Wi-Fi', 'drewniana podłoga']

SEZONY = [
    ('15.09.2025', '19.12.2025', [100, 155, 240, 275, 345, 465, 485]),
    ('20.12.2025', '01.03.2026', [150, 180, 315, 340, 420, 550, 590]),
    ('02.03.2026', '26.04.2026', [120, 160, 250, 300, 360, 480, 500]),
    ('27.04.2026', '21.06.2026', [140, 170, 270, 320, 380, 500, 540]),
    ('22.06.2026', '06.09.2026', [150, 180, 315, 340, 420, 550, 590]),
    ('07.09.2026', '20.12.2026', [130, 160, 260, 310, 370, 490, 510]),
]
KOL = ['1 os. basic', '1 os.', '2 os. basic', '2 os.', '3 os.', '4 os.', 'Studio']

OPINIE = [
    ('Edyta Jendrusz', 'Byliśmy tydzień w Leśnej Polanie, pokoje i łazienka bardzo ładne i czyste, śniadania bardzo dobre, owoce, ciasto. Na tarasie można sobie wypić kawę i podziwiać widoki, cisza i spokój. Piękna kaplica, jest to miejsce dla ciała i duszy. Panie bardzo miłe, na pewno tam wrócimy. Polecam Willę Leśna Polana.'),
    ('Grzegorz Odolczyk', 'Pensjonat genialny. Cisza i spokój. Super właścicielka. Bardzo miła obsługa. Bezpieczny parking na terenie. W pokojach czyściutko i ciepło. Śniadania pyszne i obfite w formie bufetu. Cena pobytu jedna z niższych w Krynicy i na pewno adekwatna do jakości. Gorąco polecam. Kiedy ponownie będę w Krynicy, chętnie znów tu zamieszkam.'),
    ('Edyta Dudek', 'Polecam to miejsce. Byłam w marcu. Wszystko super. Uprzejmi pracownicy i pani na recepcji bardzo miła. Pokoje ładne i zadbane. Miejsce przyjazne dla dzieci. Czułam się jak w domu. Sam budynek z zewnątrz i w środku robi wrażenie.'),
]

def zl(x):
    return f'{x}&nbsp;zł'

# ---------- strona glowna ----------
def glowna():
    pokoje = ''.join(f'''<a class="pokoj" href="pokoje.html#{p['id']}"><div class="ph">{img(p['foto'][0], p['n'], sizes='(max-width:760px) 92vw, (max-width:1180px) 45vw, 20vw')}</div><h3>{p['n']}</h3><p>{p['os']}{', rozkładana sofa' if p['id']=='rodzinny' else ''}{', dwa pokoje' if p['id']=='studio' else ''}</p><p class="cena">od {zl(p['cena'])} za dobę</p></a>''' for p in POKOJE)
    kafle = [
        ('pobyty.html#wczasy', 'taras', 'Wczasy i weekendy', 'Taras z widokiem, las za oknem i śniadania w formie bufetu.'),
        ('pobyty.html#zdrowie', 'grota', 'Wyjazdy dla zdrowia', 'Grota solna w cenie pobytu, sauna, hydromasaż i wody Krynicy.'),
        ('pobyty.html#swieta', 'jadalnia', 'Święta w górach', 'Wielkanoc i Boże Narodzenie przy wspólnym stole, bez pośpiechu.'),
        ('pobyty.html#rekolekcje', 'oratorium', 'Rekolekcje, oazy, pielgrzymki', 'Kaplica pw. św. Jana Pawła II na miejscu, w ciszy nad strumykiem.'),
        ('pobyty.html#konferencje', 'recepcja', 'Konferencje i szkolenia', 'Klimatyzowana sala z projektorem, ekranem i nagłośnieniem.'),
        ('pobyty.html#przyjecia', 'jadalnia-b', 'Przyjęcia okolicznościowe', 'Rodzinne uroczystości w stylowych wnętrzach willi.'),
    ]
    kaf = ''.join(f'<a class="kafel" href="{h}">{img(f, "", sizes="(max-width:760px) 92vw, (max-width:1024px) 46vw, 31vw")}<div class="kafel-t"><h3>{t}</h3><p>{o}</p></div></a>' for h, f, t, o in kafle)
    op = ''.join(f'<figure class="opinia"><div class="gwiazdy" aria-label="Opinia z Google">★★★★★</div><blockquote>„{t}”</blockquote><figcaption><b>{n}</b>Opinia z Google</figcaption></figure>' for n, t in OPINIE)
    t = f'''
<section class="hero" id="hero">
<figure class="hero-foto">{img('hero', 'Willa Leśna Polana na stoku Jasiennika w Krynicy-Zdroju', lazy=False, glowny=1920)}</figure>
<div class="wrap hero-in">
<h1>Willa Leśna Polana <span class="nw">w Krynicy-Zdroju</span></h1>
<p class="lead">Od 1927 roku na słonecznym stoku Jasiennika, tuż przy lesie. Cisza, śniadania w formie bufetu i grota solna na miejscu.</p>
<div class="hero-cta" id="hero-cta">{kw('Zarezerwuj pobyt')}<a class="btn obrys-b" href="pokoje.html">Pokoje i ceny</a><a class="link-strz link-m" href="pokoje.html">Pokoje i ceny</a></div>
<a class="hero-jubi" href="historia.html">{pieczec('hp')}<span><b>1927-2027. Sto lat Leśnej Polany</b>W 2027 roku willa obchodzi jubileusz. Poznaj jej historię.</span></a>
</div>
</section>

<section class="termin" aria-labelledby="termin-h"><div class="wrap">
<form id="termin" action="{KW}" method="get" target="_blank" rel="noopener" novalidate>
<h2 id="termin-h">Sprawdź wolne pokoje</h2>
<div class="pole"><label for="t-od">Przyjazd</label><input type="date" id="t-od" name="checkIn" required></div>
<div class="pole"><label for="t-do">Wyjazd</label><input type="date" id="t-do" name="checkOut" required></div>
<div class="pole pole-g"><label for="t-os">Goście</label><input type="hidden" name="occupancy" id="t-occ" value='[{{"count":2}}]'><select id="t-os"><option value="1">1 osoba</option><option value="2" selected>2 osoby</option><option value="3">3 osoby</option><option value="4">4 osoby</option><option value="5">5 osób</option><option value="6">6 osób</option></select></div>
<button class="btn" type="submit">{I_KAL}Sprawdź dostępność</button>
<p class="termin-info" aria-live="polite">Rezerwujesz bezpośrednio u nas, w systemie KW Hotel. Doba hotelowa od 14:00.</p>
</form></div></section>

<section class="sec"><div class="wrap wstep">
<div class="wstep-txt">
<h2>Odpocznij w Leśnej Polanie</h2>
<p class="lead">Willa stoi na słonecznym stoku góry Jasiennik, na skraju lasu, kilka minut od krynickiego deptaka.</p>
<p>Przyjmujemy gości przez cały rok: na wczasy i weekendy, wyjazdy lecznicze i świąteczne, rekolekcje, pielgrzymki, konferencje i przyjęcia. Pokoje mają drewniane podłogi, łazienki i garderoby, a rano czeka śniadanie w formie bufetu.</p>
<ul class="udog"><li>Śniadania bufetowe</li><li>Grota solna w cenie</li><li>Kaplica</li><li>Taras z widokiem</li><li>Bezpłatny parking</li><li>Wi-Fi</li></ul>
</div>
<div class="wstep-foto">
<figure class="f1">{img('taras-b', 'Taras Leśnej Polany ze stolikami', sizes='(max-width:1024px) 55vw, 32vw')}<figcaption>Taras przy willi</figcaption></figure>
<figure class="f2">{img('okno', 'Widok z okna pokoju na ogród i las', sizes='(max-width:1024px) 40vw, 24vw')}<figcaption>Widok z pokoju na ogród</figcaption></figure>
</div>
</div></section>

<section class="sec alt"><div class="wrap">
<div class="sec-top"><div><h2>Pokoje</h2><p>Pokoje od jednej do sześciu osób. Każdy z łazienką, suszarką, biurkiem, garderobą i Wi-Fi.</p></div><a class="link-strz" href="pokoje.html">Wszystkie pokoje i cennik</a></div>
<div class="pokoje-rz">{pokoje}</div>
<p class="przypis">Ceny za pokój za dobę w sezonie 7.09-20.12.2026, bez wyżywienia. Dzieci do 3 lat bezpłatnie, do 12 lat 20% rabatu.</p>
</div></section>

<section class="sec jubi" id="jubileusz"><div class="wrap jubi-in">
<div class="jubi-txt">
<div class="jubi-glowa">{pieczec('jb')}<h2>100 lat Leśnej Polany</h2></div>
<p class="lead">W 2027 roku willa obchodzi stulecie. Since 1927 to dla nas nie hasło, tylko adres z historią.</p>
<ul class="jubi-fakty">
<li><b>Początek XX w.</b><span>Willa powstaje według projektu czeskiego architekta Ruliszka.</span></li>
<li><b>Gość willi</b><span>W Leśnej Polanie gościł światowej sławy tenor Jan Kiepura.</span></li>
<li><b>Ostatnie lata</b><span>Generalny remont i wyższy standard wypoczynku, przy zachowaniu charakteru willi.</span></li>
<li><b>2025</b><span>Złoty Laur Zaufania, I miejsce w powiecie nowosądeckim.</span></li>
</ul>
<a class="link-strz" href="historia.html">Historia willi</a>
</div>
<figure class="jubi-foto">{img('willa-front', 'Zabytkowa część willi z mansardowym dachem', sizes='(max-width:1024px) 92vw, 46vw')}<figcaption>Najstarsza część willi z mansardowym dachem</figcaption></figure>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-top"><div><h2>Pobyty w Leśnej Polanie</h2><p>Przygotowujemy pobyty dla gości indywidualnych i grup zorganizowanych, a w ferie, wakacje i święta specjalne oferty.</p></div><a class="link-strz" href="pobyty.html">Wszystkie oferty</a></div>
<div class="kafle rzad-m">{kaf}</div>
</div></section>

<section class="sec alt"><div class="wrap relaks">
<div>
<h2>Grota solna, sauna i kaplica</h2>
<p class="lead">Na miejscu zadbasz o zdrowie i o spokój ducha, bez wychodzenia z willi.</p>
<p>Grota solna i kaplica są dostępne dla gości w cenie pobytu. Saunę, hydromasaż i masaż klasyczny zamówisz w recepcji.</p>
<ul class="cennik-l">
<li><span>Grota solna, parking, Wi-Fi, kaplica</span><span>w cenie</span></li>
<li><span>Sauna, 60 minut</span><span>35 zł / os.</span></li>
<li><span>Hydromasaż, zabieg</span><span>50 zł / os.</span></li>
<li><span>Masaż klasyczny</span><span>ok. 150 zł / os.</span></li>
</ul>
</div>
<div class="relaks-foto">
<figure class="duze">{img('grota', 'Grota solna w Leśnej Polanie', sizes='(max-width:1024px) 92vw, 44vw')}</figure>
<figure>{img('sauna', 'Sauna', sizes='(max-width:1024px) 45vw, 22vw')}<figcaption>Sauna</figcaption></figure>
<figure>{img('oratorium', 'Kaplica z witrażem', sizes='(max-width:1024px) 45vw, 22vw')}<figcaption>Kaplica pw. św. Jana Pawła II</figcaption></figure>
</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-top"><div><h2>Co mówią nasi goście</h2><p>Opinie z Google.</p></div></div>
<div class="opinie rzad-m">{op}</div>
<div class="nagrody">
<figure>{img('laur-certyfikat', 'Certyfikat Złoty Laur Zaufania 2025 dla Willi Leśna Polana', sizes='360px', glowny=640)}</figure>
<div><h2>Złoty Laur Zaufania 2025</h2>
<p class="lead">W plebiscycie K&amp;K Promotion Leśna Polana zajęła I miejsce w powiecie nowosądeckim. Wyróżnienie przyznają klienci.</p>
<ul class="nagr-lista">
<li><img src="img/aw-orly.webp" width="56" height="56" alt="" loading="lazy"><span><b>Orły Hotelarstwa 2025</b>Laureat konkursu</span></li>
<li><img src="img/aw-booking2020.webp" width="56" height="56" alt="" loading="lazy"><span><b>Booking.com Traveller Review Awards</b>2020 z oceną 9,2 oraz 2026</span></li>
<li><img src="img/aw-hotelsocial.webp" width="56" height="56" alt="" loading="lazy"><span><b>Hotel.social Certificate of Excellence 2024</b>Ocena gości 9.2 / 10</span></li>
</ul></div>
</div>
</div></section>

<section class="sec alt"><div class="wrap">
<div class="polozenie">
<figure>{img('polozenie', 'Willa Leśna Polana wśród lasów nad Krynicą-Zdrojem', sizes='(max-width:1024px) 92vw, 54vw')}</figure>
<div><h2>Krynica-Zdrój na wyciągnięcie ręki</h2>
<p>Górskie powietrze, wody mineralne, pijalnie i szlaki Popradzkiego Parku Krajobrazowego. Zimą stacje narciarskie w Słotwinach i na Jaworzynie, latem wędrówki i Festiwal im. Jana Kiepury.</p>
<p>Do Pijalni Głównej jest od nas ok. 1 km.</p>
<a class="link-strz" href="kontakt.html#dojazd">Dojazd i mapa</a></div>
</div>
</div></section>

{cta_pas()}
'''
    strona('index.html', 'Willa Leśna Polana - Krynica-Zdrój, since 1927', 'Willa Leśna Polana w Krynicy-Zdroju: pokoje 1-6 osobowe, śniadania, grota solna, kaplica, rekolekcje i pobyty grupowe. 100 lat w 2027 roku.', './', t)

# ---------- pokoje ----------
def pokoje():
    bl = ''
    for i, p in enumerate(POKOJE):
        f = p['foto']
        if len(f) == 1:
            fot = f'<div class="pk-foto jedno"><a href="{duzy(f[0])}" data-lb="pk" data-cap="{p["n"]}">{img(f[0], p["n"], sizes="(max-width:1024px) 92vw, 55vw")}</a></div>'
        else:
            fot = f'<div class="pk-foto"><a href="{duzy(f[0])}" data-lb="pk" data-cap="{p["n"]}">{img(f[0], p["n"], sizes="(max-width:760px) 92vw, (max-width:1024px) 62vw, 38vw")}</a><div class="boczne">' + ''.join(f'<a href="{duzy(x)}" data-lb="pk" data-cap="{p["n"]}">{img(x, p["n"], sizes="(max-width:760px) 46vw, (max-width:1024px) 30vw, 18vw")}</a>' for x in f[1:]) + '</div></div>'
        wyp = ''.join(f'<li>{w}</li>' for w in WYP + p['extra'])
        bl += f'''<article class="pk{' odwr' if i % 2 else ''}" id="{p['id']}">{fot}<div><h2>{p['n']}</h2><p class="osob">{p['os']}. {p['opis']}</p><ul>{wyp}</ul><div class="pk-cena"><span>od</span><b>{zl(p['cena'])}</b><span>za dobę</span></div><div class="pk-akcje">{kw('Zarezerwuj')}<a class="link-strz" href="#cennik">Cennik sezonowy</a></div></div></article>'''
    th = ''.join(f'<th scope="col">{k}</th>' for k in KOL)
    rows = ''.join(f'<tr data-od="{a}" data-do="{b}"><th scope="row">{a[:5]} - {b}</th>' + ''.join(f'<td>{zl(c)}</td>' for c in cc) + '</tr>' for a, b, cc in SEZONY)
    sez = ''.join(f'<div class="sezon" data-od="{a}" data-do="{b}"><h3>{a[:5]} - {b}</h3><dl>' + ''.join(f'<dt>{k}</dt><dd>{zl(c)}</dd>' for k, c in zip(KOL, cc)) + '</dl></div>' for a, b, cc in SEZONY)
    t = f'''{ph_hero('pokoj-rodzinny', 'Pokój rodzinny w Leśnej Polanie', 'Pokoje i ceny', 'Pokoje jedno-, dwu-, trzy- i czteroosobowe oraz studio dwupokojowe. Wszystkie z łazienką, garderobą i drewnianą podłogą.', 'Pokoje i ceny', '50% 60%')}
<section class="sec"><div class="wrap">{bl}</div></section>
<section class="sec alt" id="cennik"><div class="wrap">
<div class="sec-top"><div><h2>Cennik</h2><p>Ceny za pokój za dobę, bez wyżywienia. Podlegają rabatom zależnym od liczby osób i długości pobytu i dotyczą pobytów indywidualnych.</p></div>{kw('Sprawdź cenę na swój termin', 'btn obrys')}</div>
<div class="tab-wrap"><table class="cennik"><thead><tr><th scope="col">Sezon</th>{th}</tr></thead><tbody>{rows}</tbody></table></div>
<div class="sezony">{sez}</div>
<div class="info-g">
<div><h3>Wyżywienie</h3><ul class="cennik-l"><li><span>Śniadanie (bufet)</span><span>40 zł</span></li><li><span>Śniadanie, dzieci</span><span>25 zł</span></li><li><span>Obiadokolacja</span><span>50 zł</span></li><li><span>Obiadokolacja, dzieci</span><span>35 zł</span></li></ul><p style="margin-top:14px">Śniadania 8:00-10:00. Obiadokolacje zgłaszamy w recepcji do 10:00 tego samego dnia.</p></div>
<div><h3>Relaks</h3><ul class="cennik-l"><li><span>Sauna, 60 minut</span><span>35 zł / os.</span></li><li><span>Hydromasaż, zabieg</span><span>50 zł / os.</span></li><li><span>Masaż klasyczny</span><span>ok. 150 zł / os.</span></li><li><span>Grota solna, kaplica, parking, Wi-Fi</span><span>w cenie</span></li></ul></div>
<div><h3>Dobrze wiedzieć</h3><ul><li>Doba hotelowa od 14:00 do 10:00.</li><li>Dzieci do 3 lat śpiące z rodzicami bezpłatnie, dzieci do 12 lat 20% rabatu.</li><li>Okresy Bożego Narodzenia, Sylwestra, Wielkanocy i długich weekendów wyceniamy osobno.</li><li>Pobyty grupowe powyżej 20 osób wyceniamy indywidualnie.</li></ul></div>
</div>
</div></section>
{cta_pas('panorama-b', 'Wybierz termin i pokój', 'System pokaże wolne pokoje i cenę na wybrane dni. W razie pytań recepcja chętnie pomoże.')}'''
    strona('pokoje.html', 'Pokoje i ceny - Willa Leśna Polana, Krynica-Zdrój', 'Pokoje 1-4 osobowe i studio w Willi Leśna Polana w Krynicy-Zdroju. Cennik sezonowy, wyżywienie, sauna i grota solna.', 'pokoje.html', t)

# ---------- pobyty ----------
def pobyty():
    t = f'''{ph_hero('panorama', 'Leśna Polana latem', 'Pobyty i oferty', 'Wczasy, święta, wyjazdy dla zdrowia, rekolekcje i pielgrzymki, konferencje i przyjęcia. Przez cały rok.', 'Pobyty', '50% 55%')}
<section class="sec"><div class="wrap">
<nav class="of-nav" aria-label="Rodzaje pobytów"><a href="#wczasy">Wczasy i weekendy</a><a href="#zdrowie">Dla zdrowia</a><a href="#swieta">Święta</a><a href="#rekolekcje">Rekolekcje i pielgrzymki</a><a href="#konferencje">Konferencje</a><a href="#przyjecia">Przyjęcia</a></nav>

<article class="of" id="wczasy"><figure>{img('taras-c', 'Taras z widokiem na Krynicę', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Wczasy i weekendy</h2>
<p>Kilka dni ciszy przy lesie i spacerem do deptaka. Na tarasie kawa z widokiem, rano śniadanie w formie bufetu, wieczorem ciepła obiadokolacja. W ferie, wakacje i święta przygotowujemy specjalne oferty pobytowe.</p>
<div class="pakiet"><h3>Pakiet dla narciarzy</h3><p>5 noclegów i 5 śniadań, Wi-Fi, TV, monitorowany parking i grota solna. Obiadokolacje za dopłatą 50 zł, sauna 35 zł. Oferta obowiązywała w sezonie 2025, od 1 lutego do końca pokrywy śnieżnej.</p><div class="pk-cena"><b>900&nbsp;zł</b><span>osoba dorosła, 800 zł dzieci do 12 lat</span></div></div>
{kw('Zarezerwuj pobyt')}
</div></article>

<article class="of odwr" id="zdrowie"><figure>{img('grota', 'Grota solna', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Wyjazdy dla zdrowia</h2>
<p>Krynica-Zdrój to uzdrowisko z górskim powietrzem, leczniczymi wodami mineralnymi i sanatoriami. W willi do dyspozycji gości jest grota solna, w cenie pobytu, oraz sauna, hydromasaż i masaż klasyczny.</p>
<ul class="cennik-l"><li><span>Grota solna</span><span>w cenie</span></li><li><span>Sauna, 60 minut</span><span>35 zł / os.</span></li><li><span>Hydromasaż, zabieg</span><span>50 zł / os.</span></li><li><span>Masaż klasyczny</span><span>ok. 150 zł / os.</span></li></ul>
<p style="margin-top:18px">Cisza nocna od 22:00 do 7:00, pokoje jednoosobowe i bezpłatny parking na terenie.</p>
{kw('Zarezerwuj pobyt')}
</div></article>

<article class="of" id="swieta"><figure>{img('jadalnia', 'Jadalnia willi', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Święta w Leśnej Polanie</h2>
<p>Bez pośpiechu i bez nadmiaru. Z miejscem na oddech, spacer, ciszę i bycie razem, wśród drzew i śpiewu ptaków.</p>
<div class="pakiet"><h3>Pakiet Wielkanoc 2026</h3><p>Śniadania, w tym 2 uroczyste śniadania wielkanocne z tradycyjnymi potrawami: żurek, kiełbaska, jajka, babki, ciasta i sałatki. Ciepłe, domowe obiadokolacje.</p><div class="pk-cena"><b>950&nbsp;zł</b><span>za osobę, pobyt 3-dniowy</span></div></div>
<p>Tak wyglądała ostatnia Wielkanoc w Leśnej Polanie. Pakiety na Boże Narodzenie, Sylwestra i Wielkanoc 2027 ogłaszamy z wyprzedzeniem, zapytaj o najbliższe święta.</p>
<a class="btn obrys" href="tel:{TEL}">{I_TEL}Zapytaj o pakiet świąteczny</a>
</div></article>

<article class="of odwr" id="rekolekcje"><figure>{img('oratorium', 'Kaplica pw. św. Jana Pawła II z witrażem', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Rekolekcje, oazy i pielgrzymki</h2>
<p>Góry od zawsze sprzyjają modlitwie i refleksji. Willa leży widokowo na słonecznym stoku Jasiennika, w pobliżu lasu, i tchnie spokojem i radosną ciszą. Jesteśmy otwarci na każdą propozycję zorganizowania oazy czy rekolekcji.</p>
<ul>
<li>Kaplica pw. św. Jana Pawła II, miejsce modlitwy, medytacji i Mszy św.</li>
<li>Pokoje 1-, 2- i 3-osobowe z łazienkami</li>
<li>Klimatyzowana sala konferencyjna z multimediami</li>
<li>Kawiarenka z napojami ciepłymi i chłodnymi</li>
<li>Całodzienne wyżywienie, grota solna, Wi-Fi, bezpłatny parking</li>
<li>Wycieczki z przewodnikiem szlakami Beskidu Sądeckiego i ognisko</li>
</ul>
<a class="btn" href="mailto:{MAIL}?subject=Rekolekcje%20w%20Le%C5%9Bnej%20Polanie">Zapytaj o termin dla grupy</a>
</div></article>

<article class="of" id="konferencje"><figure>{img('recepcja', 'Recepcja i hol willi', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Konferencje i szkolenia</h2>
<p>Klimatyzowana sala konferencyjna jest wyposażona w ekran, projektor, flipchart, nagłośnienie i internet Wi-Fi. Do tego noclegi, całodzienne wyżywienie i kawiarenka, a po zajęciach las, szlaki i grota solna.</p>
<p>Pobyty grupowe powyżej 20 osób wyceniamy indywidualnie.</p>
<a class="btn" href="mailto:{MAIL}?subject=Konferencja%20w%20Le%C5%9Bnej%20Polanie">Poproś o ofertę</a>
</div></article>

<article class="of odwr" id="przyjecia"><figure>{img('jadalnia-b', 'Stylowa sala z okrągłym stołem', sizes='(max-width:1024px) 92vw, 46vw')}</figure><div>
<h2>Przyjęcia okolicznościowe</h2>
<p>Chrzciny, komunie, jubileusze i rodzinne spotkania w stylowych wnętrzach willi, z noclegiem dla gości z daleka. Menu i szczegóły ustalamy indywidualnie.</p>
<a class="btn obrys" href="tel:{TEL}">{I_TEL}{TEL_T}</a>
</div></article>
</div></section>

<section class="sec alt"><div class="wrap">
<div class="sec-top"><div><h2>Gościliśmy</h2><p>Wydarzenia, które odbyły się w Leśnej Polanie.</p></div></div>
<ul class="wydarzenia">
<li><time>14-16 kwietnia 2025</time><span><b>Lectio divina z Nikodemem.</b> Rekolekcje w Wielkim Tygodniu, prowadzący ks. Krzysztof Wons SDS.</span></li>
<li><time>19-24 sierpnia 2024</time><span><b>Wprowadzenie do życia liturgicznego Kościoła.</b> Kurs wakacyjny, prowadzący ks. Sławomir Jeziorski.</span></li>
<li><time>30 lipca - 4 sierpnia 2024</time><span><b>Życiodajnia, kontemplacja w ciszy.</b> Prowadzący o. Wojciech Drążek, Ruch Odnowy Kontemplacyjnej.</span></li>
</ul>
</div></section>
{cta_pas('panorama-b', 'Zaplanujmy Twój pobyt', 'Napisz lub zadzwoń, a przygotujemy ofertę dla Ciebie lub Twojej grupy.')}'''
    strona('pobyty.html', 'Pobyty i oferty - Willa Leśna Polana, Krynica-Zdrój', 'Wczasy, święta, wyjazdy lecznicze, rekolekcje, pielgrzymki, konferencje i przyjęcia w Willi Leśna Polana w Krynicy-Zdroju.', 'pobyty.html', t)

# ---------- galeria ----------
GAL = [
    ('Willa i otoczenie', [('hero', 'Willa Leśna Polana', 'szer'), ('willa-front', 'Najstarsza część willi', ''), ('schody', 'Schody do willi', 'pion'), ('brama', 'Brama wjazdowa', ''), ('taras', 'Taras z widokiem', ''), ('panorama', 'Willa na stoku Jasiennika', ''), ('elewacja', 'Elewacja i taras', ''), ('taras-b', 'Taras przy willi', ''), ('kaplica', 'Ogród przy strumieniu', ''), ('wejscie', 'Wejście i parking', ''), ('dach', 'Widok z balkonu', '')]),
    ('Pokoje', [('pokoj-rodzinny', 'Pokój rodzinny', 'szer'), ('pokoj-2os', 'Pokój dwuosobowy', ''), ('pokoj-3os', 'Pokój trzyosobowy', ''), ('pokoj-1os', 'Pokój jednoosobowy', ''), ('pokoj-2os-b', 'Pokój dwuosobowy', ''), ('pokoj-rodzinny-b', 'Pokój rodzinny z sofą', ''), ('pokoj-3os-b', 'Pokój na poddaszu', ''), ('lazienka', 'Łazienka', ''), ('lazienka-b', 'Łazienka', '')]),
    ('Wnętrza', [('recepcja', 'Recepcja', 'szer'), ('jadalnia', 'Jadalnia', ''), ('jadalnia-b', 'Sala z okrągłym stołem', ''), ('hol', 'Hol', ''), ('korytarz', 'Salonik na piętrze', '')]),
    ('Relaks i kaplica', [('oratorium', 'Kaplica pw. św. Jana Pawła II', 'szer'), ('grota', 'Grota solna', ''), ('sauna', 'Sauna', ''), ('oratorium-b', 'Wejście do kaplicy', ''), ('hydromasaz', 'Strefa hydromasażu', '')]),
]
def galeria():
    s = ''
    for tyt, el in GAL:
        g = ''.join(f'<a class="{c}" href="{duzy(n)}" data-lb="gal" data-cap="{a}">{img(n, a, sizes="(max-width:760px) 46vw, (max-width:1024px) 31vw, 24vw" if not c else "(max-width:760px) 92vw, 50vw")}</a>' for n, a, c in el)
        s += f'<section class="gal-sekcja"><h2>{tyt}</h2><div class="galeria">{g}</div></section>'
    t = f'''{ph_hero('panorama-b', 'Willa Leśna Polana', 'Galeria', 'Willa, pokoje, wnętrza, grota solna i kaplica. Kliknij zdjęcie, aby je powiększyć.', 'Galeria', '50% 60%')}
<section class="sec"><div class="wrap">{s}</div></section>
{cta_pas()}'''
    strona('galeria.html', 'Galeria - Willa Leśna Polana, Krynica-Zdrój', 'Zdjęcia Willi Leśna Polana w Krynicy-Zdroju: pokoje, wnętrza, grota solna, kaplica, taras i ogród.', 'galeria.html', t)

# ---------- historia ----------
def historia():
    t = f'''{ph_hero('willa-front', 'Najstarsza część Willi Leśna Polana', 'Historia willi', 'Leśna Polana przyjmuje gości od 1927 roku. W 2027 roku obchodzimy stulecie.', 'Historia', '50% 40%')}
<section class="sec"><div class="wrap hist">
<div>
<h2>Kilka słów o Leśnej Polanie</h2>
<p class="lead">Urokliwa willa na zboczu góry Jasiennik, przy ulicy prof. Henryka Świdzińskiego 37, w spokojnym i malowniczym otoczeniu.</p>
<p>Nasz ośrodek ma bogatą historię. Powstał na początku XX wieku według projektu czeskiego architekta Ruliszka i miał zaszczyt gościć światowej sławy tenora Jana Kiepurę, którego imię nosi dziś krynicki festiwal.</p>
<p>W ostatnich latach Leśna Polana przeszła generalny remont, który pozwolił podnieść standard wypoczynku, a przy tym zachować to, co w willi najcenniejsze: mansardowy dach, łukowe okna, ciszę lasu i domową atmosferę.</p>
<p>Działamy przez cały rok, goszcząc turystów indywidualnych i grupy zorganizowane. Organizujemy również spotkania duchowe.</p>
</div>
<figure>{img('elewacja', 'Willa Leśna Polana od strony tarasu', sizes='(max-width:1024px) 92vw, 46vw')}<figcaption>Willa od strony tarasu, po generalnym remoncie</figcaption></figure>
</div></section>

<section class="sec jubi"><div class="wrap jubi-duzy">
{pieczec('hj')}
<div class="jubi-txt"><h2>1927-2027. Stulecie Leśnej Polany</h2>
<p class="lead">Sto lat gości, rozmów na tarasie i ciszy nad strumieniem. Rok jubileuszowy chcemy przeżyć razem z tymi, którzy do nas wracają.</p>
<p>O wydarzeniach i ofertach jubileuszowych będziemy informować na tej stronie oraz na Facebooku i Instagramie.</p>
<a class="link-strz" href="{FB}" target="_blank" rel="noopener">Leśna Polana na Facebooku</a></div>
</div></section>

<section class="sec alt"><div class="wrap">
<div class="sec-top"><div><h2>Z archiwum willi</h2><p>Tu znajdą się zdjęcia Leśnej Polany z dawnych lat. Jeśli masz w domowym albumie fotografie willi, będziemy wdzięczni za kontakt.</p></div><a class="link-strz" href="mailto:{MAIL}?subject=Archiwalne%20zdj%C4%99cia%20Le%C5%9Bnej%20Polany">Podziel się zdjęciem</a></div>
<div class="archiwum">
<div class="arch-ramka"><p><span>Willa w latach 30.</span>miejsce na zdjęcie archiwalne</p></div>
<div class="arch-ramka"><p><span>Goście i wydarzenia</span>miejsce na zdjęcie archiwalne</p></div>
<div class="arch-ramka"><p><span>Przed remontem</span>miejsce na zdjęcie archiwalne</p></div>
</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="nagrody" style="margin-top:0;padding-top:0;border-top:0">
<figure>{img('laur-certyfikat', 'Certyfikat Złoty Laur Zaufania 2025', sizes='360px', glowny=640)}</figure>
<div><h2>Wyróżnienia</h2>
<p class="lead">Złoty Laur Zaufania 2025, I miejsce w powiecie nowosądeckim, za zaangażowanie, profesjonalizm i wysiłek włożony w rozwój firmy.</p>
<ul class="nagr-lista">
<li><img src="img/aw-orly.webp" width="56" height="56" alt="" loading="lazy"><span><b>Orły Hotelarstwa 2025</b>Laureat konkursu</span></li>
<li><img src="img/aw-booking2020.webp" width="56" height="56" alt="" loading="lazy"><span><b>Booking.com Traveller Review Awards</b>2020 z oceną 9,2 oraz 2026</span></li>
<li><img src="img/aw-hotelsocial.webp" width="56" height="56" alt="" loading="lazy"><span><b>Hotel.social Certificate of Excellence 2024</b>Ocena gości 9.2 / 10</span></li>
</ul></div>
</div>
</div></section>
{cta_pas('panorama')}'''
    strona('historia.html', 'Historia - 100 lat Willi Leśna Polana, Krynica-Zdrój', 'Willa Leśna Polana w Krynicy-Zdroju od 1927 roku. Projekt czeskiego architekta, gościł tu Jan Kiepura. Stulecie w 2027 roku.', 'historia.html', t)

# ---------- kontakt ----------
def kontakt():
    t = f'''{ph_hero('brama', 'Brama wjazdowa Leśnej Polany', 'Kontakt i dojazd', 'Recepcja odpowiada na telefony i maile. Rezerwacje indywidualne przyjmujemy też online.', 'Kontakt', '30% 60%')}
<section class="sec"><div class="wrap kontakt-g">
<div class="k-dane">
<div class="k-blok"><h3>Telefon</h3><p><a class="duzy" href="tel:{TEL}">{TEL_T}</a></p></div>
<div class="k-blok"><h3>E-mail</h3><p><a class="link" href="mailto:{MAIL}">{MAIL}</a></p></div>
<div class="k-blok"><h3>Adres</h3><p>Willa Leśna Polana<br>ul. prof. Henryka Świdzińskiego 37<br>33-380 Krynica-Zdrój</p></div>
<div class="k-blok"><h3>Doba hotelowa</h3><p>Zameldowanie od 14:00, wymeldowanie do 10:00</p></div>
<div class="k-blok"><h3>Rezerwacja online</h3><p style="margin-bottom:12px">Wolne pokoje i ceny na wybrany termin.</p>{kw('Zarezerwuj pobyt')}</div>
</div>
<div>
<div class="mapa" id="mapa">{img('polozenie', '', sizes='(max-width:1024px) 92vw, 50vw')}<div class="mapa-in"><p>Mapa OpenStreetMap wczyta się po kliknięciu.</p><button class="btn jasny" type="button" id="mapa-btn">Pokaż mapę</button><a class="link" style="color:#fff" href="{MAPS}" target="_blank" rel="noopener">Nawiguj w Google Maps</a></div></div>
<p class="przypis">Wjazd od ulicy prof. Świdzińskiego, bezpłatny parking na terenie willi.</p>
</div>
</div></section>

<section class="sec alt" id="dojazd"><div class="wrap">
<div class="sec-top"><div><h2>Dojazd</h2></div><a class="link-strz" href="{MAPS}" target="_blank" rel="noopener">Wyznacz trasę</a></div>
<div class="dojazd">
<div><h3>Samochodem</h3><p>Do Krynicy-Zdroju przez Nowy Sącz. W nawigacji wpisz: Krynica-Zdrój, ul. prof. Świdzińskiego 37. Parkujesz bezpłatnie na terenie willi.</p></div>
<div><h3>Pociągiem lub autobusem</h3><p>Krynica-Zdrój ma stację kolejową i dworzec autobusowy. Na życzenie podpowiemy, jak najwygodniej dotrzeć do willi.</p></div>
<div><h3>Na miejscu</h3><p>Do Pijalni Głównej i deptaka jest ok. 1 km. Blisko szlaki Popradzkiego Parku Krajobrazowego, Jaworzyna i Słotwiny.</p></div>
</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-top"><div><h2>Dane do przelewu</h2><p>Zaliczki i płatności za pobyt.</p></div></div>
<div class="dojazd przelew">
<div><h3>Odbiorca</h3><p>Marbet PPHU Maria Grzesiakowska<br>ul. H. Świdzińskiego 37, 33-380 Krynica-Zdrój<br>NIP 8721627354</p></div>
<div><h3>Rachunek</h3><p>ING Bank Śląski<br>87 1050 1836 1000 0092 1199 5270</p></div>
<div><h3>Przelew z zagranicy</h3><p>IBAN PL87 1050 1836 1000 0092 1199 5270<br>BIC INGBPLPW</p></div>
</div>
</div></section>
{cta_pas('taras-b')}'''
    strona('kontakt.html', 'Kontakt i dojazd - Willa Leśna Polana, Krynica-Zdrój', 'Willa Leśna Polana, ul. prof. H. Świdzińskiego 37, Krynica-Zdrój. Tel. +48 883 044 142, recepcja@lesna-polana.eu.', 'kontakt.html', t)

# ---------- regulamin ----------
def regulamin():
    pkt = [
        'Doba hotelowa trwa od godziny 14:00 do godziny 11:00.',
        'Przy rezerwacji należy określić przybliżony czas pobytu w hotelu.',
        'Życzenie przedłużenia pobytu, poza okres wskazany w dniu przybycia, gość hotelowy powinien zgłosić w recepcji do godziny 10:00 dnia, w którym upływa termin najmu pokoju. Hotel uwzględnia życzenia przedłużenia pobytu w miarę posiadanych możliwości.',
        'Posiłki wydawane są w godzinach: śniadania 8:00-10:00, obiadokolacje 16:00-18:00. Podczas pobytów pakietowych: obiady 13:00-14:30, kolacje 18:00-19:00.',
        'Obiady, obiadokolacje oraz kolacje należy zgłaszać w dniu wydawania posiłków do godziny 10:00. Zgłoszenia przyjmuje recepcja.',
        'Hotel świadczy usługi zgodnie ze swoją kategorią i standardem. W przypadku zastrzeżeń dotyczących jakości usług prosimy o jak najszybsze zgłaszanie ich do recepcji, co umożliwi nam niezwłoczną reakcję.',
        'Hotel ma obowiązek zapewnić:<ul><li>warunki pełnego i nieskrępowanego wypoczynku gościa,</li><li>bezpieczeństwo pobytu, w tym zachowanie tajemnicy informacji o gościu,</li><li>profesjonalną i uprzejmą obsługę,</li><li>sprzątanie pokoju i wykonywanie niezbędnej naprawy urządzeń podczas nieobecności gościa, a w przypadku jego obecności tylko wówczas, gdy wyrazi zgodę i życzenie,</li><li>w miarę posiadanych możliwości inny pokój lub w inny sposób złagodzić niedogodności, gdy występujące w pokoju usterki nie będą mogły być usunięte.</li></ul>',
        'Na życzenie gościa hotel świadczy nieodpłatnie następujące usługi:<ul><li>udzielanie informacji związanych z pobytem i podróżą,</li><li>budzenie o wyznaczonej godzinie,</li><li>przechowywanie pieniędzy i przedmiotów wartościowych w czasie pobytu gościa w hotelu,</li><li>przechowywanie bagażu gości zameldowanych w hotelu.</li></ul>',
        'Zgubienie lub uszkodzenie karty wejściowej do pokoju skutkuje dodatkową opłatą w wysokości 50 zł. Za zgubienie lub zniszczenie ręcznika dodatkowa opłata wynosi: ręcznik mały 25 zł, ręcznik duży 35 zł.',
        'Gość powinien zawiadomić recepcję hotelową o wystąpieniu szkody niezwłocznie po jej stwierdzeniu.',
        'Odpowiedzialność hotelu z tytułu utraty lub uszkodzenia pieniędzy, papierów wartościowych, kosztowności albo przedmiotów mających wartość naukową lub artystyczną jest ograniczona, jeżeli przedmioty te nie zostaną oddane do depozytu w recepcji.',
        'Hotel nie ponosi odpowiedzialności za uszkodzenie lub utratę samochodu lub innego pojazdu należącego do gościa.',
        'Gość hotelowy ponosi odpowiedzialność materialną za wszelkiego rodzaju uszkodzenia lub zniszczenia przedmiotów wyposażenia i urządzeń technicznych hotelu powstałe z jego winy lub z winy odwiedzających go osób. Hotel nie ponosi odpowiedzialności za nieszczęśliwe wypadki dzieci, które pozostawione zostały bez opieki przez osoby opiekujące się nimi.',
        'Każdorazowo opuszczając pokój gość powinien sprawdzić zamknięcie drzwi, a klucz pozostawić w recepcji.',
        'Gość hotelowy nie może przekazywać pokoju osobom trzecim, nawet jeśli nie upłynął okres, za który uiścił należną za pobyt opłatę.',
        'Osoby niezameldowane w hotelu mogą przebywać w pokoju hotelowym od godziny 7:00 do godziny 22:00.',
        'W hotelu obowiązuje zachowanie ciszy od godziny 22:00 do godziny 7:00.',
        'Ze względu na bezpieczeństwo przeciwpożarowe zabronione jest używanie w pokojach urządzeń niestanowiących wyposażenia pokoju hotelowego oraz palenie tytoniu. Wywołanie alarmu p.poż. skutkuje dodatkową opłatą w wysokości 300 zł.',
        'Hotel może odmówić przyjęcia gościa, który podczas poprzedniego pobytu rażąco naruszył regulamin hotelowy, wyrządzając szkodę w mieniu hotelowym lub gości albo szkodę na osobie gości, pracowników hotelu albo innych osób przebywających w hotelu.',
        'Przedmioty osobistego użytku pozostawione przez wyjeżdżającego gościa w pokoju hotelowym będą odesłane na adres wskazany przez gościa. W przypadku nieotrzymania takiej dyspozycji hotel przechowa te przedmioty przez 3 miesiące.',
    ]
    li = ''.join(f'<li>{p}</li>' for p in pkt)
    t = f'''{ph_hero('korytarz', 'Wnętrze willi', 'Regulamin', 'Zasady, które służą spokojowi i bezpieczeństwu wszystkich naszych gości.', 'Regulamin', '50% 50%')}
<section class="sec"><div class="wrap tekst"><p class="lead">Dyrekcja hotelu będzie Państwu bardzo wdzięczna za współpracę w przestrzeganiu niniejszego regulaminu. Pokój w hotelu wynajmowany jest na doby.</p><ol>{li}</ol><p>Właściciel oraz Dyrekcja Hotelu życzą Państwu miłego pobytu.</p></div></section>'''
    strona('regulamin.html', 'Regulamin - Willa Leśna Polana, Krynica-Zdrój', 'Regulamin hotelowy Willi Leśna Polana w Krynicy-Zdroju.', 'regulamin.html', t)

glowna(); pokoje(); pobyty(); galeria(); historia(); kontakt(); regulamin()
print('ok')
