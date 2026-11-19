"""Generates the Polish static pages in ../site from shared header/footer partials."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
WRITTEN = set()

NAV = [("index.html","Główna"),("knowledge-hub.html","Artykuły"),("jobs.html","Formy pracy"),
       ("services.html","Poradniki"),("about.html","O nas"),("contact.html","Kontakt")]

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="oklch(37% .075 178)"/><path d="M6 16.500L16 7l10 9.500" stroke="oklch(97.6% .009 88)" stroke-width="2.400" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.500 15v9h13v-9" fill="oklch(97.6% .009 88)"/><circle cx="16" cy="19.500" r="2.400" fill="oklch(60% .19 32)"/></svg>'
EMAIL = "kontakt@worknest.pl"

def icon(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
IC = {
 "clock":icon('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "home":icon('<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>'),
 "split":icon('<path d="M4 6h16M4 12h10M4 18h16"/>'),
 "shield":icon('<path d="M12 3l8 3v6c0 5-3.400 8-8 10-4.600-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>'),
 "doc":icon('<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
 "pen":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "brief":icon('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3"/>'),
 "chat":icon('<path d="M4 5h16v11H9l-5 4z"/>'),
}

def page(fname, title, desc, body, extra_head=""):
    WRITTEN.add(fname)
    nav = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    body_class = ' class="home"' if fname=="index.html" else ""
    html = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1f5a4f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/styles.css?v=3">
{extra_head}</head>
<body{body_class}>
<a class="skip" href="#main">Przejdź do treści</a>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html">{LOGO}Work<em>Nest</em> PL</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list" aria-label="Otwórz menu"><span class="bars" aria-hidden="true"></span></button>
<ul id="nav-list">{nav}</ul>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}Work<em>Nest</em> PL</a>
<p style="margin-top:1rem;max-width:36ch">Niezależne artykuły o rynku pracy w Polsce: umowy, branże, praca zdalna i dorabianie.</p></div>
<div><h4>Na stronie</h4><ul><li><a href="services.html">Poradniki</a></li><li><a href="jobs.html">Formy pracy</a></li><li><a href="knowledge-hub.html">Artykuły</a></li><li><a href="glossary.html">Słownik</a></li><li><a href="faq.html">Pytania</a></li></ul></div>
<div><h4>Redakcja</h4><ul><li><a href="about.html">O nas</a></li><li><a href="contact.html">Kontakt</a></li><li><a href="privacy.html">Prywatność</a></li><li><a href="disclaimer.html">Zastrzeżenie</a></li></ul></div>
</div>
<div class="legal"><p>WorkNest PL to serwis informacyjny. Nie jesteśmy agencją zatrudnienia, nie publikujemy ofert i nie pośredniczymy w rekrutacji. Nie jesteśmy powiązani z urzędami ani z portalami ogłoszeniowymi. Teksty to informacje ogólne, nie porada prawna, podatkowa ani kadrowa. Szczegóły potwierdź w Państwowej Inspekcji Pracy, ZUS albo Krajowej Administracji Skarbowej. Oszustwo zgłoś na cert.pl. W nagłym przypadku dzwoń na 112. Informacja o rynku pracy: Zielona Linia <strong>19524</strong>.</p>
<p>&copy; 2026 WorkNest PL &middot; publikacja internetowa &middot; Warszawa &middot; {EMAIL}</p></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

def head(eyebrow, h1, lede=""):
    return f'<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{"<p class=lede>"+lede+"</p>" if lede else ""}</div></div>'

IC.update({
 "book":icon('<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 21V5"/>'),
 "laptop":icon('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>'),
 "globe":icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "wallet":icon('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
 "pen2":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "check":icon('<path d="M5 12l4 4 10-10"/>'),
 "x":icon('<path d="M6 6l12 12M18 6L6 18"/>'),
})

IMG={
"artykul-branze.html":("sectors-hiring.svg","Wieża w stylu pałacu kultury, tramwaj i rosnący wykres branż"),
"artykul-zawody.html":("in-demand-roles.jpg","Ikony opieki, technologii i analizy na podium zawodów"),
"artykul-dorabianie.html":("second-income.svg","Osoba przy laptopie i dwie wstęgi monet wpadające do portfela"),
"artykul-trend-zdalna.html":("remote-growth.svg","Laptop połączony z domami i panoramą miasta"),
"artykul-szkolenia.html":("upskilling.jpg","Osoba wchodząca po książkach w stronę drzwi"),
"artykul-dane-rynku.html":("labour-data.jpg","Otwarty raport z wykresami i lupą"),
"artykul-koszty.html":("rising-costs.svg","Kalkulator, klucze, zakupy i laptop"),
"artykul-opieka.html":("childcare-caregiving.jpg","Opiekun i dziecko przy laptopie, obok plecak i zegar"),
"artykul-powrot.html":("restart.jpg","Osoba robiąca pierwszy krok na ścieżce"),
"artykul-formy.html":("work-modes.jpg","Zegar, dom, laptop i dokument połączone linią"),
"artykul-oszustwa.html":("job-scams.jpg","Lupa nad ogłoszeniem, lista kontrolna i tarcza"),
"artykul-wniosek.html":("flexible-work-request.jpg","Kalendarz, laptop i dymek rozmowy o pracy zdalnej"),
"artykul-zus.html":("pasek-wyplaty.jpg","Pasek z wypłaty, skarbonka i kalkulator"),
"artykul-ogloszenie.html":("read-job-ad.jpg","Ogłoszenie z zaznaczonymi fragmentami i lupą"),
"artykul-cv.html":("remote-cv.jpg","Laptop z CV, słuchawki i kubek na biurku w domu"),
}
def thumb(href,lazy=True):
    if href not in IMG: return ""
    f,alt=IMG[href]
    return f'<a class="thumb" href="{href}" tabindex="-1" aria-hidden="true"><img src="img/{f}" alt="" width="1280" height="720"{" loading=\"lazy\"" if lazy else ""}></a>'

EXC={
"artykul-branze.html":"Opieka, produkcja, budownictwo, logistyka i centra usług wracają w raportach. Województwo zmienia obraz...",
"artykul-zawody.html":"Nazwy stanowisk się zmieniają. Umiejętności, o które pytają pracodawcy, układają się w kilka grup...",
"artykul-dorabianie.html":"Coraz więcej osób dokłada niepełny etat albo zlecenie do głównej pracy...",
"artykul-trend-zdalna.html":"Praca zdalna przeszła z przywileju do rozmowy, którą da się oprzeć na Kodeksie pracy...",
"artykul-szkolenia.html":"Kurs ma sens wtedy, gdy umiesz wskazać ogłoszenia, w których ta umiejętność już jest...",
"artykul-dane-rynku.html":"Bezrobocie rejestrowane i badanie aktywności mierzą różne rzeczy. Obraz jest w zestawieniu...",
"artykul-koszty.html":"Jeśli pod koniec miesiąca zostaje mniej niż rok temu, nie jesteś w tym sam...",
"artykul-opieka.html":"Pytanie często nie brzmi, czy chcesz pracować, tylko czy godziny spinają się ze szkołą i żłobkiem...",
"artykul-powrot.html":"Luka w CV jest częsta. Krótkie, spokojne zdanie zwykle wystarcza...",
"artykul-cv.html":"Przy pracy zdalnej nikt nie patrzy ci przez ramię. CV ma pokazać, że pracujesz samodzielnie...",
"artykul-wniosek.html":"Wniosek traktuj jak propozycję: co chcesz zmienić, od kiedy i jak praca zostanie zrobiona...",
"artykul-zus.html":"Na pasku wypłaty widać brutto, składki i zaliczkę na PIT. To najszybszy sprawdzian umowy...",
"artykul-formy.html":"Ogłoszenia mieszają trzy rzeczy: wymiar czasu, miejsce pracy i rodzaj umowy...",
"artykul-ogloszenie.html":"Dwa ogłoszenia mogą brzmieć tak samo, a oznaczać inną ochronę i inną wypłatę na rękę...",
"artykul-oszustwa.html":"Oszuści lubią pracę zdalną i „bez doświadczenia”, bo obietnica łatwej dniówki jest kusząca...",
}
def card(href,label,t,d,m="5 min"):
    return f'<article class="post reveal">{thumb(href)}<div class="meta"><span class="cat">{label}</span><span>{m}</span></div><h3><a href="{href}">{t}</a></h3><p>{EXC.get(href,d)}</p></article>'
def tile_s(href,t,d): return f'<a class="mini reveal" href="{href}"><b>{t}</b><span>{d}</span></a>'

page("index.html","Rynek pracy w Polsce: etat, praca z domu, zlecenie | WorkNest PL",
"Niezależne artykuły o polskim rynku pracy: branże, umowy, praca zdalna i dorabianie. Bez obietnic zarobku i bez ofert pracy.",f'''
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<span class="eyebrow">Kariera i rynek pracy w Polsce</span>
<h1>Co się zmienia na rynku pracy. <span>I co z tego wynika dla ciebie.</span></h1>
<p class="lede">Branże, w których naprawdę szukają ludzi, umowy z ogłoszeń oraz dorabianie: niepełny etat, praca z domu, zlecenie albo własna działalność. Piszemy po polsku, na podstawie przepisów i danych urzędowych. Wynagrodzenie zależy od roli i godzin. Nikt go tutaj nie obiecuje.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Czytaj artykuły</a><a class="btn btn-ghost" href="#dorabianie">Po co dorabiać</a></div>
</div>
<a class="lead-card" href="artykul-branze.html"><img src="img/sectors-hiring.svg" alt="" width="1280" height="720"><span class="lead-copy"><span class="cat">Temat numeru &middot; Branże</span><h2>Gdzie w Polsce naprawdę przybywa pracy</h2><span class="go">Czytaj artykuł &rarr;</span></span></a>
</div></section>

<section class="index-sec"><div class="wrap">
<div class="head reveal"><span class="eyebrow">W skrócie</span><h2>Cztery rzeczy, które układają dziś karierę w Polsce.</h2></div>
<div>
<ol class="shifts">
<li class="reveal"><span class="no">01</span><h3>Branże</h3><p>Opieka, produkcja, budownictwo, logistyka i centra usług wracają w Barometrze Zawodów. Województwo zmienia obraz.</p></li>
<li class="reveal"><span class="no">02</span><h3>Umowa</h3><p>Etat, zlecenie i B2B to trzy różne rzeczy. Urlop, ZUS i podatek nie wynikają z nazwy stanowiska.</p></li>
<li class="reveal"><span class="no">03</span><h3>Zdalnie</h3><p>Praca zdalna jest w Kodeksie pracy. Okazjonalnie to najwyżej 24 dni w roku i tylko za zgodą pracodawcy.</p></li>
<li class="reveal"><span class="no">04</span><h3>Dorabianie</h3><p>Część etatu, zmiany po południu i zlecenia dokładają się do budżetu. To zwykła praca, nie droga na skróty.</p></li>
</ol>
<p class="src-note">Źródła: GUS, Barometr Zawodów, Ministerstwo Rodziny, Pracy i Polityki Społecznej. Płaca minimalna w 2026 r.: 4&nbsp;806&nbsp;zł brutto za pełen etat.</p>
</div></div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Najnowsze</span><h2>Ścieżki, zawody i umiejętności.</h2></div>
<div class="posts shelf">
{card("artykul-zawody.html","Zawody","Zawody, o które pytają pracodawcy","Opieka, dane, cyfrowe role, finanse i operacje.")}
{card("artykul-dorabianie.html","Dorabianie","Dlaczego tyle osób dokłada drugie zajęcie","Niepełny etat, praca z domu albo zlecenie obok etatu.")}
{card("artykul-szkolenia.html","Szkolenia","Szkolenia, które da się połączyć z pracą","KFS, urząd pracy i baza usług rozwojowych.")}
{card("artykul-trend-zdalna.html","Branże","Praca zdalna i hybryda po nowelizacji Kodeksu pracy","Co wolno wnioskować i czego wniosek nie gwarantuje.")}
{card("artykul-dane-rynku.html","Kariera","Jak czytać dane o rynku pracy","Bezrobocie, wolne miejsca i płace.","4 min")}
{card("artykul-koszty.html","Życie i pieniądze","Czynsz, rata i wypłata: kiedy dorabianie ma sens","Domowy budżet bez obietnicy łatwych pieniędzy.")}
</div>
<p class="after-tiles"><a href="knowledge-hub.html">Więcej artykułów &rarr;</a></p>
</div></section>

<section class="band" id="dorabianie"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Dorabianie</span><h2>Dlaczego część etatu i zlecenie wracają do domowych rachunków.</h2></div>
<div class="reveal"><p class="lede">Czynsz, rata kredytu, żłobek i bilet miesięczny potrafią zjeść wypłatę. W dużych miastach coraz więcej osób dokłada do etatu niepełny wymiar, pracę z domu albo zlecenie.</p>
<p>Praca z domu i hybryda zdejmują codzienny dojazd tramwajem albo samochodem. Zanim się zgodzisz, sprawdź rodzaj umowy, godziny i to, czy główny pracodawca pozwala dorabiać. Stawka z ogłoszenia nie jest obietnicą.</p>
<p><a href="artykul-dorabianie.html">Czytaj artykuł &rarr;</a></p></div>
</div></section>

<section class="directory"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Formy pracy</span><h2>Sześć sposobów, w jakie ludzie w Polsce pracują elastycznie.</h2></div>
<div class="minis">
{tile_s("praca-niepelny-etat.html","Niepełny etat","Na przykład 1/2 albo 3/4")}
{tile_s("praca-z-domu.html","Praca z domu","Ustalone godziny u siebie")}
{tile_s("praca-zdalna.html","Praca zdalna","Dom, hybryda, inne miejsce")}
{tile_s("praca-online.html","Praca online","Korepetycje, wsparcie, moderacja")}
{tile_s("praca-freelance.html","Zlecenie i B2B","Projekt albo faktura")}
{tile_s("dorabianie.html","Dorabianie","Porównanie dróg")}
</div></div></section>

<section class="rights"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Prawo i pieniądze</span><h2>Warto przeczytać.</h2></div>
<div class="posts trio">
{card("artykul-wniosek.html","Prawo","Wniosek o pracę zdalną, krok po kroku","Co wpisać i czego pracodawca może odmówić.")}
{card("artykul-zus.html","Prawo","ZUS, PIT i pasek z wypłaty","Co sprawdzić, zanim podpiszesz.","4 min")}
{card("artykul-cv.html","Kariera","CV do pracy zdalnej i z domu","Pokaż, że pracujesz bez nadzoru.","4 min")}
</div></div></section>

<section class="contact-sec" id="kontakt"><div class="wrap split">
<div><span class="eyebrow">Kontakt</span><h2>Pytanie albo pomysł na temat?</h2><p class="lede">Napisz. Czytamy wiadomości i z nich bierzemy kolejne tematy. Nie przysyłaj PESEL-u, zdjęcia dowodu ani danych do banku.</p></div>
<div><form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Imię</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">E-mail</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="msg">Wiadomość</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Wyślij</button></form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Dziękujemy za wiadomość.</h3><p>Powinien otworzyć się program pocztowy z gotową treścią. Zostaje nacisnąć wyślij.</p><p class="ok-sub">Jeśli nic się nie otworzyło, napisz na {EMAIL}.</p></div></div>
</div></section>
''')

GUIDE={k:f'<div class="btn-row"><a class="btn btn-primary" href="{v}">Czytaj cały poradnik</a></div>' for k,v in {
"niepelny":"praca-niepelny-etat.html","zdomu":"praca-z-domu.html","zdalna":"praca-zdalna.html",
"online":"praca-online.html","freelance":"praca-freelance.html"}.items()}
def jobsec(id_,alt,eyebrow,h2,intro,roles,suit,check):
    rl="".join(f"<li>{r}</li>" for r in roles)
    sl="".join(f"<li>{r}</li>" for r in suit)
    cl="".join(f"<li>{r}</li>" for r in check)
    return f'''<section id="{id_}"{' class="alt"' if alt else ''}><div class="wrap">
<div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lede">{intro}</p></div>
<div class="cols3"><div><h3>Typowe role</h3><ul>{rl}</ul></div><div><h3>Pasuje, jeśli</h3><ul>{sl}</ul></div><div><h3>Dopytaj, zanim podpiszesz</h3><ul>{cl}</ul></div></div>
{GUIDE.get(id_,"")}</div></section>'''

jobs_body=head("Formy pracy","Niepełny etat, praca z domu, zdalna, zlecenie i B2B.","Sześć układów, które widać w polskich ogłoszeniach: co oznaczają w praktyce i co sprawdzić przed zgodą.")
jobs_body+='''<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Na skróty</span><h2>Sześć form obok siebie.</h2><p class="lede">To skrót. Szczegóły zależą od pracodawcy, więc zawsze czytaj umowę.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Forma</th><th>Godziny</th><th>Gdzie</th><th>Status</th><th>ZUS i podatek</th></tr></thead><tbody>
<tr><td><a href="#niepelny">Niepełny etat</a></td><td>Ułamek pełnego etatu</td><td>Sklep, biuro albo dom</td><td>Pracownik</td><td>Pracodawca pobiera zaliczkę i zgłasza do ZUS</td></tr>
<tr><td><a href="#zdomu">Praca z domu</a></td><td>Ustalone godziny</td><td>Dom</td><td>Zwykle pracownik</td><td>Zwykle jak przy etacie</td></tr>
<tr><td><a href="#zdalna">Praca zdalna</a></td><td>Pełny albo niepełny etat</td><td>Uzgodnione miejsce</td><td>Pracownik albo B2B</td><td>Zależy od umowy</td></tr>
<tr><td><a href="#online">Praca online</a></td><td>Bloki godzin</td><td>Przez internet</td><td>Różnie</td><td>Zależy od umowy</td></tr>
<tr><td><a href="#freelance">Zlecenie i B2B</a></td><td>Ustalasz sam</td><td>Dowolnie</td><td>Zlecenie, dzieło albo działalność</td><td>Często sam pilnujesz PIT. ZUS zależy od tytułu</td></tr>
<tr><td><a href="#kontrakt">Kontrakt i praca tymczasowa</a></td><td>Na czas określony</td><td>Różnie</td><td>Pracownik, często przez agencję</td><td>Przy umowie o pracę: ZUS</td></tr>
</tbody></table></div><p class="notice">Od 1 stycznia 2026 r. płaca minimalna na pełen etat to 4&nbsp;806&nbsp;zł brutto, a na niepełnym etacie proporcjonalnie do wymiaru. Minimalna stawka godzinowa przy części umów zlecenia to 31,40&nbsp;zł brutto. Zarobek z ogłoszenia nie jest gwarantowany.</p></div></section>'''
jobs_body+=jobsec("niepelny",False,"Niepełny etat","Praca na część etatu","Umowa o pracę w wymiarze niższym niż pełen etat, na przykład 1/2 albo 3/4. Nadal jesteś pracownikiem: masz urlop, wypowiedzenie i składki, tylko liczone od tego wymiaru.",
 ["Obsługa sklepu i gastronomii","Asystent biura i recepcja","Korepetytor albo pomoc w szkole","Hostessa i promocje w galerii","Obsługa klienta na zmiany"],
 ["Uczysz się, opiekujesz się dzieckiem albo rodzicem","Chcesz dołożyć dochód do etatu","Wracasz do pracy stopniowo"],
 ["Wymiar etatu i grafik zmian","Brutto, netto i dzień wypłaty","Urlop proporcjonalny i L4","Okres próbny i wypowiedzenie"])
jobs_body+=jobsec("zdomu",True,"Praca z domu","Praca z domu na ustalonych godzinach","Rola z grafikiem, wykonywana u siebie. W ogłoszeniach często stoi „home office”. To nie musi być własna działalność.",
 ["Obsługa klienta na czacie, mailu albo telefonie","Wprowadzanie danych i praca biurowa","Pomoc biurowa na odległość","Prowadzenie profili w mediach społecznościowych","Transkrypcja i tłumaczenia"],
 ["Musisz być w domu przy dziecku albo rodzicu","Chcesz odciąć dojazd","Masz spokojny kąt i stabilny internet"],
 ["Etat, zlecenie czy B2B?","Kto daje laptop","Godziny kontaktu i czas reakcji","Jak mierzą pracę"])
jobs_body+=jobsec("zdalna",False,"Praca zdalna","Praca zdalna i hybrydowa","Miejsce pracy jest uzgodnione: dom, czasem inne miasto, czasem kilka dni w biurze. Część ról jest w polskich centrach usług, część w zespołach z innego kraju, ale w polskich godzinach.",
 ["Marketing i analityka","Projektowanie","Programowanie i testy","Koordynacja projektów","Księgowość oraz kadry i płace w centrum usług wspólnych"],
 ["Masz konkretną umiejętność","Pracujesz bez stania nad biurkiem","Dobrze piszesz, nie tylko mówisz"],
 ["Które godziny musisz być dostępny","Kto jest pracodawcą i w jakim kraju","Złote, euro czy inna waluta","Etat, zlecenie czy faktura"])
jobs_body+=jobsec("online",True,"Praca online","Praca wykonywana w całości przez internet","Korepetycje, moderacja, sprawdzanie informacji, obsługa sklepu. Uczciwa praca online jest płatna przez firmę, którą da się znaleźć, za opisany zakres. Nie za „zadania”, które najpierw trzeba opłacić.",
 ["Korepetycje online","Moderacja społeczności","Opisywanie i sprawdzanie danych","Obsługa zamówień w sklepie","Wsparcie wydarzeń online"],
 ["Chcesz krótkie bloki godzin","Lubisz pracę przy ekranie","Umiesz trzymać umówione terminy"],
 ["Kto płaci i kiedy","Czy proszą o opłatę na start, to sygnał ostrzegawczy","Czy pierwsze zadania są płatne","Co przy odwołaniu zajęć"])
jobs_body+=jobsec("freelance",False,"Zlecenie i B2B","Zlecenie, dzieło i własna działalność","Płatność za rezultat albo za staranne działanie, a nie za etat. Sam pilnujesz umowy, rachunku albo faktury i podatku. Składki zależą od tego, czy to zlecenie, dzieło, działalność nierejestrowana czy JDG.",
 ["Grafika i identyfikacja","Teksty i tłumaczenia","Montaż wideo i zdjęć","Księgowość małych firm","Strony i małe aplikacje"],
 ["Chcesz sam układać tydzień","Masz portfolio albo wąską umiejętność","Dasz radę w miesiącach, w których jest ciszej"],
 ["Zakres, termin i liczba poprawek","Zaliczka od klienta, nie opłata „za pracę”","Umowa na piśmie","PIT i limit działalności nierejestrowanej"])
jobs_body+=jobsec("kontrakt",True,"Kontrakt i praca tymczasowa","Umowa na czas określony i praca tymczasowa","Zastępstwo, sezon, projekt albo szczyt w magazynie. Przy pracy tymczasowej między tobą a firmą, w której pracujesz, stoi agencja. Agencja powinna być w KRAZ i nie pobiera od ciebie opłaty za znalezienie pracy.",
 ["Zastępstwo w biurze i operacjach","Sezon w handlu i logistyce","Koordynacja projektu","Wsparcie obsługi klienta w szczycie"],
 ["Chcesz datę końca z góry","Wracasz po przerwie","Chcesz sprawdzić firmę albo branżę"],
 ["Długość umowy i co dalej","Czy zatrudnia agencja, i czy jest w KRAZ","Urlop i rodzaj umowy","Czy da się przejść na stałe"])
jobs_body+='''<section id="dorabianie"><div class="wrap"><div class="head"><span class="eyebrow">Z domu</span><h2>Dorabianie: główne drogi.</h2><p class="lede">Osoby, które chcą dołożyć dochód bez rzucania obecnego życia, zwykle wybierają niepełny etat, pracę z domu, zlecenie albo krótką działalność. Każda droga jest opisana wyżej. Wynagrodzenie zależy od roli, umiejętności i godzin. Nie jest gwarantowane.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="dorabianie.html">Porównaj drogi</a><a class="btn btn-ghost" href="#niepelny">Niepełny etat</a><a class="btn btn-ghost" href="artykul-formy.html">Co znaczą te słowa</a></div></div></section>
<section class="alt" id="gdzie-szukac"><div class="wrap"><div class="head"><span class="eyebrow">Gdzie szukać</span><h2>Oferty sprawdzaj u źródła, nie w podejrzeniu z komunikatora.</h2><p class="lede">Nie publikujemy wakatów. Ludzie w Polsce szukają w tych miejscach. To nie są nasi partnerzy.</p></div>
<div class="types">
<div class="type"><span class="n">01</span><h3><a href="https://oferty.praca.gov.pl" rel="noopener">oferty.praca.gov.pl</a></h3><p>Publiczna baza ofert urzędów pracy. Obok niej działają prywatne serwisy, z których ludzie korzystają na co dzień: Pracuj.pl i OLX Praca.</p></div>
<div class="type"><span class="n">02</span><h3>Strona kariery firmy</h3><p>Wejdź na adres, który sam znalazłeś, nie na link z SMS-a. W IT ogłoszenia bywają też na No Fluff Jobs i Just Join IT.</p></div>
<div class="type"><span class="n">03</span><h3><a href="https://stor.praca.gov.pl/portal/#/kraz" rel="noopener">Krajowy Rejestr Agencji Zatrudnienia</a></h3><p>Zanim podasz dane agencji, sprawdź wpis w KRAZ. Legalna agencja nie bierze od ciebie pieniędzy za znalezienie pracy w Polsce.</p></div>
</div></div></section>'''
page("jobs.html","Formy pracy w Polsce: etat, zdalnie, zlecenie, B2B | WorkNest PL",
"Porównanie niepełnego etatu, pracy z domu, pracy zdalnej, zlecenia i B2B: godziny, składki i pytania przed podpisaniem umowy.",jobs_body)

page("services.html","Poradniki o pracy i kalkulator godzin | WorkNest PL","Darmowe poradniki i kalkulator godzin o niepełnym etacie, pracy z domu, pracy zdalnej i zleceniu. Bez rejestracji i bez obietnicy zarobku.",
head("Poradniki","Co tu publikujemy.","Artykuły, porównania i kalkulator. Bez rejestracji i bez opłat.")+f'''
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["laptop"]}</div><h3>Poradniki form pracy</h3><p>Role, przykładowy tydzień, start i to, co sprawdzić w umowie: etat, zdalnie, zlecenie, dzieło i B2B.</p><a class="more" href="jobs.html">Zobacz formy pracy &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["wallet"]}</div><h3>Kalkulator godzin</h3><p>Wpisz kwotę, którą chcesz dołożyć, i stawkę za godzinę. Pokażemy rząd wielkości godzin w tygodniu. To nie jest obietnica wypłaty.</p><a class="more" href="dorabianie.html">Policz &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Artykuły</h3><p>Umowy, ZUS, ogłoszenia, CV, koszty życia i oszustwa „pracy z domu”.</p><a class="more" href="knowledge-hub.html">Czytaj &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Słownik ogłoszeń</h3><p>Etat, zlecenie, B2B, hybryda, ryczałt, KRAZ. Po polsku, bez żargonu z tłumaczenia.</p><a class="more" href="glossary.html">Szukaj hasła &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["globe"]}</div><h3>Gdzie szukać</h3><p>Publiczna baza ofert, strony firm i rejestr agencji. Linki, nie pośrednictwo.</p><a class="more" href="jobs.html#gdzie-szukac">Zobacz źródła &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Sprawdzenie ogłoszenia</h3><p>Zaznacz sygnały ostrzegawcze. Nic nie jest wysyłane ani zapisywane.</p><a class="more" href="scam-check.html">Sprawdź ogłoszenie &rarr;</a></article>
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">Napisz</span><h2>Pytanie albo korekta?</h2><p>Daj znać, czego brakuje, albo wskaż zdanie, które trzeba poprawić.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Kontakt</a></div></div>
</div></section>''')

posts=[
("trends","Branże","artykul-branze.html","Gdzie w Polsce naprawdę przybywa pracy","Branże, które wracają w danych, i co z tego wynika przy wyborze kierunku.","5 min",True),
("roles","Zawody","artykul-zawody.html","Zawody, o które pytają pracodawcy","Opieka, dane, role cyfrowe, finanse i operacje.","5 min",False),
("second","Dorabianie","artykul-dorabianie.html","Dlaczego tyle osób dokłada drugie zajęcie","Etat na część, praca z domu i zlecenie obok głównej pracy.","5 min",False),
("trends","Branże","artykul-trend-zdalna.html","Praca zdalna i hybryda po nowelizacji Kodeksu pracy","Wniosek, 24 dni okazjonalnie i czego to nie gwarantuje.","4 min",False),
("edu","Szkolenia","artykul-szkolenia.html","Szkolenia, które da się połączyć z pracą","KFS, urząd pracy i baza usług rozwojowych.","5 min",False),
("career","Kariera","artykul-dane-rynku.html","Jak czytać dane o rynku pracy","Bezrobocie rejestrowane, badanie aktywności, wolne miejsca i płace.","4 min",False),
("second","Dorabianie","artykul-koszty.html","Czynsz, rata i wypłata","Kiedy dorabianie ma sens, a kiedy tylko dodaje zmęczenia.","5 min",False),
("second","Dorabianie","artykul-opieka.html","Praca obok szkoły, żłobka i opieki","Godziny, które spinają się z rodziną.","5 min",False),
("career","Kariera","artykul-powrot.html","Powrót do pracy po przerwie","Jak mówić o luce i od czego zacząć.","5 min",False),
("career","Kariera","artykul-cv.html","CV do pracy zdalnej i z domu","Pokaż, że pracujesz bez nadzoru.","4 min",False),
("rights","Prawo i pieniądze","artykul-wniosek.html","Wniosek o pracę zdalną, krok po kroku","Co wpisać i czego można się spodziewać.","5 min",False),
("rights","Prawo i pieniądze","artykul-zus.html","ZUS, PIT i pasek z wypłaty","Co sprawdzić przy etacie i przy zleceniu.","4 min",False),
("career","Kariera","artykul-formy.html","Etat, zdalnie, hybryda, zlecenie, B2B","Słowa z ogłoszenia oznaczają różne rzeczy.","5 min",False),
("career","Kariera","artykul-ogloszenie.html","Jak czytać ogłoszenie o pracę","Wymiar, umowa, brutto i drobny druk.","4 min",False),
("scam","Oszustwa","artykul-oszustwa.html","Fałszywa praca zdalna: siedem sygnałów","Jak rozpoznać ogłoszenie, które chce wpłaty.","6 min",False),
]
cards=""
for cat,label,href,t,d,m,feat in posts:
    body_=f'<div><div class="meta"><span class="cat">{label}</span><span>{m}</span></div><h3><a href="{href}">{t}</a></h3><p>{EXC.get(href,d)}</p>{"<a class=\"btn btn-warm\" href=\""+href+"\">Czytaj</a>" if feat else ""}</div>'
    cards+=f'<article class="post{" feature" if feat else ""}" data-cat="{cat}">{thumb(href, not feat)}{body_}</article>'
page("knowledge-hub.html","Artykuły o rynku pracy w Polsce | WorkNest PL","Artykuły o branżach, zawodach, szkoleniach, pracy zdalnej i dorabianiu w Polsce.",
head("Artykuły","Rynek pracy w Polsce, bez obietnic.","Branże, umowy, szkolenia i dorabianie. Przy liczbach podajemy źródło.")+f'''
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filtruj artykuły">
<button class="chip" data-filter="all" aria-pressed="true">Wszystkie</button>
<button class="chip" data-filter="trends" aria-pressed="false">Branże</button>
<button class="chip" data-filter="roles" aria-pressed="false">Zawody</button>
<button class="chip" data-filter="edu" aria-pressed="false">Szkolenia</button>
<button class="chip" data-filter="second" aria-pressed="false">Dorabianie</button>
<button class="chip" data-filter="career" aria-pressed="false">Kariera</button>
<button class="chip" data-filter="rights" aria-pressed="false">Prawo i pieniądze</button>
<button class="chip" data-filter="scam" aria-pressed="false">Oszustwa</button></div>
<div class="posts">{cards}</div></div></section>''')

TAKE={}
EXTRA={}
SOURCES={}
def article(fname,title,desc,cat,body):
    tk=TAKE.get(fname)
    box=("<div class=\"takeaways\"><h2>W skrócie</h2><ul>"+"".join(f"<li>{t}</li>" for t in tk)+"</ul></div>") if tk else ""
    body=body.replace("</p>","</p>"+box,1) if box else body
    ex=EXTRA.get(fname)
    if ex:
        body+="<h2>Pytania</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in ex[0])
        body+='<h2>Czytaj dalej</h2><ul>'+"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in ex[1])+'</ul>'
    src=SOURCES.get(fname)
    if src:
        body+='<h2>Źródła</h2><ul class="sources">'+"".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t,u in src)+'</ul>'
    body='<p class="byline">Ostatnia aktualizacja: listopad 2026</p>'+body
    hero=""
    if fname in IMG:
        f,alt=IMG[fname]
        hero=f'<div class="wrap article"><figure class="hero-img"><img src="img/{f}" alt="{alt}" width="1280" height="720"></figure></div>'
    page(fname,title+" | WorkNest PL",desc,f'''{head(cat,title)}
{hero}<section style="padding-top:2rem"><div class="wrap article">{body}
<p style="margin-top:2.5rem"><a href="knowledge-hub.html">&larr; Wróć do artykułów</a></p></div></section>''')

EXTRA.update({
"artykul-oszustwa.html":([("Odpisałem i podałem dane. Co teraz?","Przestań pisać i nie dopłacaj. Zrób zrzuty ekranu. Jeśli poszły pieniądze albo dostęp do banku, zadzwoń do banku i na Policję. Incydent zgłoś na incydent.cert.pl. PESEL możesz zastrzec w aplikacji mObywatel albo na gov.pl."),("Jak sprawdzić, że firma istnieje?","Znajdź ją w KRS albo CEIDG po nazwie, którą sam wpiszesz, nie po linku z wiadomości. Ofertę porównaj ze stroną kariery albo z oferty.praca.gov.pl. Agencję sprawdź w KRAZ.")],[("praca-niepelny-etat.html","Niepełny etat"),("praca-online.html","Praca online"),("scam-check.html","Lista sygnałów")]),
"artykul-formy.html":([("Czy niepełny etat to to samo co zlecenie?","Nie. Niepełny etat to umowa o pracę w niższym wymiarze. Zlecenie to umowa cywilnoprawna, z inną ochroną i innymi składkami."),("Czy praca może być jednocześnie zdalna i na pół etatu?","Tak. Wymiar czasu i miejsce to dwie osobne rzeczy.")],[("praca-niepelny-etat.html","Niepełny etat"),("praca-zdalna.html","Praca zdalna"),("praca-freelance.html","Zlecenie i B2B")]),
"artykul-koszty.html":([("Ile godzin potrzeba, żeby dorzucenie było odczuwalne?","Zależy od stawki i od kwoty. Policz w <a href='dorabianie.html'>kalkulatorze godzin</a>. Wynik to rząd wielkości, nie obietnica."),("Czy dorabianie jest opodatkowane?","Przychód z pracy, zlecenia i działalności co do zasady wykazujesz w PIT. Aktualne ulgi, w tym ulgę dla młodych, sprawdź na podatki.gov.pl.")],[("dorabianie.html","Porównanie dróg"),("praca-niepelny-etat.html","Niepełny etat"),("artykul-zus.html","ZUS i pasek z wypłaty")]),
"artykul-opieka.html":([("Są role w godzinach szkoły?","Część ogłoszeń na niepełny etat i pracę z domu mieści się między odprowadzeniem a odebraniem dziecka. Dopytaj o grafik, zanim podpiszesz."),("Czy mogę wnioskować o pracę zdalną u obecnego pracodawcy?","Tak, na zasadach z Kodeksu pracy. Wniosek nie jest zgodą z góry. Zobacz poradnik.")],[("artykul-wniosek.html","Wniosek o pracę zdalną"),("praca-z-domu.html","Praca z domu"),("praca-niepelny-etat.html","Niepełny etat")]),
"artykul-powrot.html":([("Jak długa luka jest „za długa”?","Nie ma jednego progu. Liczy się, co umiesz teraz i jak krótko opowiesz przerwę."),("Czy zacząć od części etatu?","Wiele osób tak robi: mniejszy wymiar albo umowa na czas określony daje świeże doświadczenie bez skoku na pełen etat od poniedziałku.")],[("praca-niepelny-etat.html","Niepełny etat"),("artykul-cv.html","CV do pracy zdalnej"),("artykul-ogloszenie.html","Jak czytać ogłoszenie")]),
})

TAKE.update({
"artykul-oszustwa.html":["Uczciwy pracodawca nie każe płacić, żeby zacząć pracę.","Oferta z WhatsAppa, Telegramu albo SMS-a, na którą sam nie aplikowałeś, to powód do ostrożności.","Firmę i agencję sprawdzasz sam: KRS lub CEIDG, strona kariery, KRAZ.","Nie podawaj PESEL-u, zdjęcia dowodu, kodu BLIK ani loginu do banku. Użyczenie konta to ryzyko przestępstwa, nie „przysługa”."],
"artykul-formy.html":["Wymiar czasu, miejsce i rodzaj umowy to trzy różne rzeczy.","Pełen etat to przeciętnie 40 godzin tygodniowo. Niepełny etat to ułamek, nie „poniżej 35 godzin”.","Zlecenie, dzieło i B2B nie dają automatycznie urlopu jak umowa o pracę.","Przed podpisem dopytaj o brutto, dzień wypłaty, ZUS i wypowiedzenie."],
"artykul-koszty.html":["Niepełny etat, praca z domu albo zlecenie to zwykłe sposoby dołożenia dochodu.","Porównaj kwotę na rękę z dojazdem, opieką i sprzętem.","Ustal, kiedy wpływa wypłata.","Jeśli budżet jest bardzo ciasny, sprawdź też świadczenia na gov.pl. To nie zastępuje umowy."],
"artykul-opieka.html":["Zacznij od godzin, które naprawdę masz.","O grafiku i pracy z domu rozmawiaj przed podpisem.","Od spodziewanej kwoty odejmij żłobek, dojazd i inne koszty pracy.","Decyzję da się zmienić, gdy dziecko idzie do szkoły albo gdy kończy się opieka."],
"artykul-powrot.html":["Przerwy w CV są częste i da się o nich powiedzieć w dwóch zdaniach.","Krótko i wprost wystarcza.","Część etatu albo umowa na czas określony bywa spokojniejszym startem.","Odśwież CV, jedną referencję i umiejętności, których naprawdę użyjesz."],
})

article("artykul-oszustwa.html","Fałszywa praca zdalna: siedem sygnałów","Jak rozpoznać fałszywą ofertę pracy zdalnej albo „pracy z domu” w Polsce.","Oszustwa",'''
<p class="lede">Oszuści lubią ogłoszenia o pracy zdalnej i o dorabianiu bez doświadczenia. Obietnica wysokiej dniówki za klikanie jest łatwiejsza do sprzedania niż etat w magazynie. Oto układy, które wracają.</p>
<h2>1. Nie aplikowałeś, a już masz „rekrutera”</h2><p>WhatsApp, Telegram, Messenger albo SMS z gotową stawką, choć nigdzie nie wysłałeś CV. Poważne firmy rzadko zaczynają od kwoty na czacie z nieznajomym.</p>
<h2>2. Dniówka nie pasuje do roboty</h2><p>„300 zł dziennie za lajkowanie, ocenianie albo pakowanie długopisów w domu” nie jest modelem, na którym stoją prawdziwe firmy. Im prostsze zadanie i im wyższa obietnica, tym wolniej działaj.</p>
<h2>3. Najpierw wpłata</h2><p>Kaucja, opłata za szkolenie, „zestaw startowy” albo doładowanie konta, żeby odblokować zadania, to sposób na wyciągnięcie pieniędzy. Legalna agencja zatrudnienia nie pobiera od ciebie opłaty za znalezienie pracy w Polsce.</p>
<h2>4. Rozmowa tylko na czacie</h2><p>Nie ma adresu w domenie firmy, nie ma rozmowy wideo, nie ma człowieka, którego znajdziesz na stronie. Nazwy nie ma w KRS ani w CEIDG.</p>
<h2>5. Pośpiech i tajemnica</h2><p>„Odpowiedz w godzinę”, „nie mów rodzinie”, „zostały dwa miejsca”. Chodzi o to, żebyś nie sprawdził nazwy w wyszukiwarce.</p>
<h2>6. Prośba o dane, których rekruter na starcie nie potrzebuje</h2><p>PESEL, zdjęcie dowodu, kod BLIK, login do banku albo kod z mObywatel. Konto „tylko do odbioru przelewów” bywa używane jako słup. To już nie jest niezręczna rekrutacja, to ryzyko przestępstwa.</p>
<h2>7. Oferty nie ma tam, gdzie firma naprawdę rekrutuje</h2><p>Porównaj rolę ze stroną kariery, którą sam otworzysz, albo z <a href="https://oferty.praca.gov.pl" rel="noopener">oferty.praca.gov.pl</a>. Agencję sprawdź w <a href="https://stor.praca.gov.pl/portal/#/kraz" rel="noopener">KRAZ</a>.</p>
<div class="callout"><p><strong>Jeśli już wszedłeś w rozmowę:</strong> przerwij wpłaty, zachowaj zrzuty, zadzwoń do banku. Przy stracie pieniędzy albo danych do konta powiadom Policję. Incydent zgłosisz na <a href="https://incydent.cert.pl" rel="noopener">incydent.cert.pl</a>. PESEL zastrzeżesz na gov.pl. Możesz też przejść <a href="scam-check.html">listę sygnałów</a>.</p></div>''')

article("artykul-formy.html","Etat, zdalnie, hybryda, zlecenie, B2B","Co znaczą słowa z polskich ogłoszeń o pracę: etat, home office, zlecenie, dzieło i B2B.","Podstawy",'''
<p class="lede">Ogłoszenia mieszają trzy osobne rzeczy: ile godzin pracujesz, gdzie pracujesz i na jakiej umowie. Dopóki ich nie rozdzielisz, „elastycznie” nic nie znaczy.</p>
<h2>Godziny: pełen etat i niepełny etat</h2><p>Pełen etat to przeciętnie 40 godzin w pięciodniowym tygodniu, zwykle 8 godzin na dobę. Niepełny etat to ułamek: 1/2, 3/4, 1/4. Płaca minimalna na niepełnym etacie spada proporcjonalnie. W 2026 r. pełen etat ma podłogę 4&nbsp;806&nbsp;zł brutto, więc 1/2 etatu to 2&nbsp;403&nbsp;zł brutto. To podłoga ustawowa, nie typowa oferta.</p>
<h2>Miejsce: biuro, hybryda, praca zdalna</h2><ul><li><strong>Praca zdalna:</strong> wykonujesz ją poza zakładem, w miejscu uzgodnionym z pracodawcą, także w domu. Zasady są w Kodeksie pracy.</li><li><strong>Home office:</strong> potoczne określenie pracy z domu. Dopytaj, czy to stała praca zdalna, hybryda, czy kilka dni okazjonalnie.</li><li><strong>Hybryda:</strong> część dni w biurze. Ustal, czy dni są sztywne i czy dojazd jest w twoim czasie.</li><li><strong>Okazjonalna praca zdalna:</strong> najwyżej 24 dni w roku kalendarzowym, tylko na twój wniosek. Pracodawca może odmówić.</li></ul>
<h2>Umowa: etat, zlecenie, dzieło, B2B</h2><p>Umowa o pracę daje urlop, okres wypowiedzenia, ochronę i składki po stronie pracodawcy. Umowa zlecenia to staranne działanie. Przy części zleceń obowiązuje minimalna stawka godzinowa: 31,40&nbsp;zł brutto w 2026 r. Uczeń albo student do 26. roku życia na zleceniu często nie ma składek ZUS. To wyjątek, nie reguła dla każdego poniżej 26 lat. Etat jest oskładkowany niezależnie od wieku.</p>
<p>Umowa o dzieło jest o rezultat. Zwykle nie rodzi składek ZUS, chyba że zawierasz ją z własnym pracodawcą. Przychód i tak bywa opodatkowany. B2B to faktura z działalności: sam płacisz ZUS przedsiębiorcy i podatek. Działalność nierejestrowana w 2026 r. mieści się w limicie przychodu 10&nbsp;813,50&nbsp;zł na kwartał. Po przekroczeniu trzeba zgłosić firmę w CEIDG.</p>
<div class="callout"><p>Pytania do każdego ogłoszenia: jaka to umowa? Jaki wymiar? Kwota jest brutto czy netto? Kto zgłasza ZUS? Jaki jest okres próbny i wypowiedzenie?</p></div>
<p>Nieznane słowo znajdziesz w <a href="glossary.html">słowniku</a>.</p>''')

article("artykul-koszty.html","Czynsz, rata i wypłata: kiedy dorabianie ma sens","Jak patrzeć na dorabianie, gdy domowy budżet w Polsce jest ciasny.","Życie i pieniądze",'''
<p class="lede">Jeśli pod koniec miesiąca zostaje mniej niż rok temu, nie jesteś w tym sam. Najem, rata kredytu, żywność, prąd i bilet miesięczny zjadają wypłatę w dużym mieście szybciej niż w arkuszu.</p>
<h2>Drugie zajęcie nie jest czarodziejską różdżką</h2><p>Czynszu często nie zmienisz z tygodnia na tydzień. Da się czasem zmienić dochód: niepełnym etatem, zmianami w handlu, pracą z domu albo zleceniem. To nadal praca. Męczy, zajmuje wieczory i bywa nieregularna.</p>
<h2>Dobierz formę do budżetu, nie do hasła</h2><ul><li><strong>Niepełny etat:</strong> przewidywalny grafik i umowa o pracę. Wypłata jest spokojniejsza, stawka za godzinę bywa niższa niż na zleceniu.</li><li><strong>Praca z domu albo hybryda:</strong> odpada bilet albo paliwo. Zostaje prąd, internet i ktoś, kto w tym czasie jest z dzieckiem.</li><li><strong>Zlecenie albo B2B:</strong> bywa wyższa kwota na fakturze i większa nierówność miesięcy. ZUS przedsiębiorcy i podatek liczą się wcześniej, nie „jakoś w kwietniu”.</li></ul>
<h2>Policz całość</h2><p>Od kwoty na rękę odejmij dojazd, obiad w galerii i opiekę. Dopytaj, którego dnia wpływa wypłata. „Do 40 zł za godzinę” to sufit z ogłoszenia, nie twoja stawka.</p>
<div class="callout"><p>Gdy pieniędzy brakuje na bieżące rachunki, sprawdź też świadczenia rodzinne i inne formy wsparcia na gov.pl, w tym 800+. To dodatek, nie umowa o pracę. Omijaj osoby, które obiecują szybki zysk za opłatę wstępną.</p></div>
<p>Formy pracy są w <a href="jobs.html">zestawieniu</a>.</p>''')

article("artykul-opieka.html","Praca obok szkoły, żłobka i opieki","Jak układać godziny pracy, gdy w domu jest dziecko albo osoba, którą się opiekuje.","Życie i pieniądze",'''
<p class="lede">Przy dziecku albo rodzicu pytanie często nie brzmi, czy chcesz pracować. Brzmi, czy grafik spina się z odbiorem ze szkoły, z żłobkiem i z wizytą u lekarza.</p>
<h2>Najpierw prawdziwe godziny</h2><p>Rozpisz tydzień razem z drogą: odprowadzenie, świetlica, obiad, twoja dojazdowa godzina. Rola, która mieści się w tych godzinach, bywa więcej warta niż wyższa stawka, której nie udźwigniesz.</p>
<h2>Dopytaj wcześnie</h2><ul><li>Grafik jest sztywny czy układasz zmiany?</li><li>Które dni mogą być z domu, a które w biurze?</li><li>Co się dzieje, gdy dziecko albo rodzic choruje?</li></ul>
<h2>Odejmij koszty opieki</h2><p>Publiczny żłobek i prywatny żłobek to dwa różne rachunki. Świadczenie 800+ jest wsparciem na dziecko, nie opłatą za miejsce w żłobku i nie wypłatą. Od spodziewanej kwoty odejmij opiekę i dojazd. Czasem mniej godzin w roli, która się spina, wychodzi lepiej niż „pełne popołudnia”.</p>
<h2>To nie jest porażka</h2><p>Część etatu albo przerwa na opiekę to decyzja, którą da się zmienić, gdy dziecko idzie do przedszkola albo gdy kończy się intensywna opieka.</p>
<p>Godziny i formy są w <a href="jobs.html">zestawieniu form pracy</a>.</p>''')

article("artykul-powrot.html","Powrót do pracy po przerwie","Jak wrócić do pracy w Polsce po opiece, zwolnieniu, chorobie albo nauce.","Życie i pieniądze",'''
<p class="lede">Luka w CV jest częsta: opieka, redukcja, zdrowie, studia albo zwykłe zatrzymanie się. Rekruterzy widzą ją częściej, niż się wydaje przy kuchennym stole.</p>
<h2>Powiedz w dwóch zdaniach</h2><p>Co się działo, czego się w tym czasie nauczyłeś albo co robiłeś, i czego szukasz teraz. Bez przemowy i bez przepraszania za cały akapit.</p>
<h2>Zacznij od mniejszego kroku</h2><p>Niepełny etat, zastępstwo albo umowa na czas określony odbudowują świeże doświadczenie bez wymogu, że od poniedziałku wracasz na pełen etat i na dwie zmiany.</p>
<h2>Odśwież to, co ktoś naprawdę przeczyta</h2><ul><li>CV: ostatnie umiejętności, kurs albo wolontariat, który da się pokazać.</li><li>Jedna krótka referencja od osoby, z którą pracowałeś.</li><li>Jeśli jesteś zarejestrowany w urzędzie pracy, zapytaj o szkolenie albo staż. Jeśli pracujesz, o dofinansowanie kursu może wnioskować pracodawca z Krajowego Funduszu Szkoleniowego.</li></ul>
<div class="callout"><p>Nie ma daty, do której „trzeba zdążyć”. Jest pierwszy konkretny krok, który mieści się w twoim tygodniu.</p></div>
<p>Spokojny start opisujemy w <a href="jobs.html">formach pracy</a>.</p>''')

flags=["Napisali pierwsi na WhatsAppie, Telegramie, Messengerze albo SMS-em, choć nie wysyłałem CV.",
"Obiecują wysoką dniówkę za lajkowanie, ocenianie, „zadania” albo pakowanie w domu.",
"Proszą o wpłatę, kaucję, opłatę za szkolenie albo doładowanie konta.",
"Nie ma strony firmy, adresu w jej domenie ani wpisu, który sam znajduję w KRS lub CEIDG.",
"Poganiają i każą nikomu nie mówić.",
"Proszą o PESEL, zdjęcie dowodu, kod BLIK, login do banku albo kod z mObywatel.",
"Rozmowa jest tylko na czacie albo proszą o użyczenie konta bankowego."]
lis="".join(f'<li><label><input type="checkbox"> <span>{f}</span></label></li>' for f in flags)
page("scam-check.html","Czy to ogłoszenie wygląda podejrzanie | WorkNest PL","Zaznacz sygnały w ofercie pracy. Podpowiedź zostaje w twojej przeglądarce.",
head("Oszustwa","Czy to ogłoszenie wygląda podejrzanie?","Zaznacz to, co pasuje. Nic nie jest zapisywane ani wysyłane.")+f'''
<section><div class="wrap split">
<div><ul class="check" id="scam-check">{lis}</ul>
<div class="result" id="scam-result" hidden role="status" aria-live="polite"><h3></h3><p></p></div></div>
<div><h2>Sprawdź sam, nie wierz linkowi z czatu.</h2><ol>
<li>Wpisz nazwę firmy w KRS albo CEIDG.</li>
<li>Porównaj rolę ze stroną kariery albo z oferty.praca.gov.pl.</li>
<li>Agencję znajdź w KRAZ, zanim wyślesz skan dowodu.</li>
<li>Incydent zgłoś na cert.pl. Przy stracie pieniędzy dzwoń do banku i na Policję.</li></ol>
<div class="callout"><p>Pieniądze albo dostęp do banku już poszły? Najpierw bank, potem Policja. Zgłoszenie incydentu: <a href="https://incydent.cert.pl" rel="noopener">incydent.cert.pl</a>. Numer 112 jest do nagłych przypadków.</p></div>
<p class="notice">Lista jest tylko podpowiedzią. Brak zaznaczeń nie znaczy, że oferta jest uczciwa.</p></div>
</div></section>''')

terms=[("Brutto","Kwota przed podatkiem i składkami, które prawo każe pobrać. To nie jest kwota, która wpływa na konto."),
("Netto","Kwota po zaliczce na podatek i po składkach należnych od ciebie. Przy B2B „na fakturze” netto znaczy co innego: kwota bez VAT, od której sam rozliczasz podatek i ZUS."),
("Wymiar etatu","Część pełnego czasu pracy. 1/2 etatu to połowa, nie „około 20 godzin, jak wyjdzie”."),
("Płaca minimalna","Ustawowa podłoga miesięczna przy umowie o pracę. W 2026 r. 4 806 zł brutto na pełen etat, proporcjonalnie mniej na niepełnym."),
("Stawka godzinowa","Przy części umów zlecenia jest osobna podłoga za godzinę. W 2026 r. to 31,40 zł brutto. Nie dotyczy każdej umowy."),
("Umowa o pracę","Etat. Urlop, okres wypowiedzenia, składki i ochrona z Kodeksu pracy."),
("Umowa zlecenia","Umowa cywilnoprawna o staranne działanie. Inna ochrona niż etat. Student albo uczeń do 26. roku życia często bez składek ZUS."),
("Umowa o dzieło","Umowa o rezultat. Zwykle bez ZUS, z wyjątkami, między innymi gdy zawierasz ją z własnym pracodawcą."),
("B2B","Współpraca na fakturze, zwykle z jednoosobowej działalności. Sam płacisz ZUS przedsiębiorcy i podatek."),
("Działalność nierejestrowana","Drobna działalność bez wpisu do CEIDG, w limicie przychodu. Od 2026 r. limit liczy się kwartalnie: 10 813,50 zł. Przychód i tak bywa do rozliczenia w PIT."),
("JDG","Jednoosobowa działalność gospodarcza, wpis w CEIDG."),
("Okres próbny","Początek zatrudnienia na osobnej umowie. Wypowiedzenie bywa wtedy krótsze. Sprawdź długość w umowie."),
("Okres wypowiedzenia","Czas od złożenia wypowiedzenia do końca umowy o pracę. Przy etacie zależy od stażu u tego pracodawcy."),
("Praca zdalna","Praca poza zakładem, w miejscu uzgodnionym z pracodawcą. Zasady, sprzęt albo ryczałt wynikają z Kodeksu pracy i z porozumienia."),
("Praca zdalna okazjonalna","Do 24 dni w roku kalendarzowym, na wniosek pracownika. Pracodawca może odmówić."),
("Hybryda","Część dni w biurze, część poza nim. Dopytaj, które dni są sztywne."),
("Home office","Potoczne „praca z domu”. W umowie sprawdź, czy to praca zdalna stała, hybrydowa czy okazjonalna."),
("Ryczałt za pracę zdalną","Zryczałtowana kwota na prąd, internet albo inne koszty. Wysokość wynika z ustaleń, nie z ogłoszenia reklamowego."),
("Pasek wypłaty","Zestawienie brutto, składek, zaliczki na PIT i kwoty do wypłaty. Poproś, jeśli go nie dostajesz."),
("Ulga dla młodych","Zwolnienie z PIT części przychodów z pracy i zlecenia do 26. roku życia, do ustawowego limitu. Nie obejmuje dowolnej działalności. Aktualny limit: podatki.gov.pl."),
("KRAZ","Krajowy Rejestr Agencji Zatrudnienia. Tu sprawdzisz, czy agencja ma wpis."),
("Praca tymczasowa","Pracujesz u pracodawcy użytkownika, a zatrudnia cię agencja. Agencja powinna być w KRAZ."),
("Zakaz konkurencji","Zapis, który ogranicza dorabianie albo pracę dla podobnej firmy. Przeczytaj go w głównej umowie, zanim weźmiesz drugie zajęcie."),
("Słup","Osoba, której konto służy do przepuszczania pieniędzy z oszustwa, czasem „tylko na chwilę”. To ryzyko odpowiedzialności karnej.")]
tl="".join(f'<div class="term"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in terms)
page("glossary.html","Słownik ogłoszeń o pracę | WorkNest PL","Co znaczą etat, zlecenie, B2B, hybryda, brutto i KRAZ w polskich ogłoszeniach.",
head("Słownik","Słowa z ogłoszeń, po ludzku.")+f'''
<section><div class="wrap" style="max-width:860px">
<label for="glossary-search" class="eyebrow">Szukaj</label>
<input id="glossary-search" class="search" type="search" placeholder="Na przykład ZUS albo hybryda" autocomplete="off">
<dl class="glossary">{tl}</dl><p id="glossary-empty" hidden>Nic nie pasuje. <a href="contact.html">Napisz, czego brakuje.</a></p></div></section>''')

faqs=[("Czy WorkNest PL publikuje oferty pracy?","Nie. Opisujemy formy pracy i przepisy w skrócie. Aktualne oferty są na oferty.praca.gov.pl, na stronach karier firm i w prywatnych serwisach ogłoszeniowych. Nie jesteśmy z nimi powiązani."),
("Czy korzystanie z serwisu coś kosztuje?","Nie. Teksty i kalkulator są bezpłatne, bez rejestracji. Nikomu nie płać za „przyjęcie do pracy”."),
("Jak szukać pracy na część etatu?","Filtruj wymiar etatu w publicznych ofertach i na stronach firm, które sam otworzysz. W poradniku o niepełnym etacie jest lista pytań przed podpisem."),
("Czy praca z domu w Polsce jest realna?","Tak. Obsługa klienta, administracja, księgowość i część ról specjalistycznych dzieje się z domu. Uczciwy pracodawca płaci za opisany zakres i nie każe wpłacać, żeby zacząć."),
("Jak dorabiać w domu bez obietnic z internetu?","Najczęściej przez zwykłą pracę: niepełny etat, zlecenie, korepetycje albo krótką działalność w limicie. Kwota zależy od roli, umiejętności i godzin. Nie jest gwarantowana."),
("Czym praca zdalna różni się od pracy z domu?","Praca z domu to potocznie praca u siebie. Praca zdalna w Kodeksie pracy może być też w innym uzgodnionym miejscu. Hybryda dokłada dni w biurze."),
("Czy ogłoszenia „praca online” są prawdziwe?","Część tak: korepetycje, moderacja, wsparcie sklepu. Sprawdź, kto płaci, bierz ustalenia na piśmie i nie płać za start."),
("Czy przy zleceniu jest ZUS i urlop?","Urlop jak przy etacie nie przysługuje z samej nazwy „zlecenie”. Składki zależą od tytułu. Uczeń albo student do 26. roku życia często ich nie ma. Szczegóły potwierdź w ZUS."),
("Czy mogę wnioskować o pracę zdalną?","Pracownik może złożyć wniosek. Zgoda nie jest automatyczna. Okazjonalnie limit wynosi 24 dni w roku. Część osób, między innymi w ciąży i opiekujących się małym dzieckiem, ma mocniejszą pozycję. Katalog i terminy sprawdź w Kodeksie pracy albo w PIP."),
("Jak sprawdzić agencję?","Wpis w Krajowym Rejestrze Agencji Zatrudnienia na stor.praca.gov.pl. Legalna agencja nie pobiera od osoby szukającej pracy opłaty za pośrednictwo w Polsce.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","Pytania o etat, pracę z domu i zlecenie | WorkNest PL","Krótkie odpowiedzi o niepełnym etacie, pracy zdalnej, zleceniu, B2B i dorabianiu w Polsce.",
head("Pytania","Krótkie odpowiedzi.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Nie ma twojego pytania? <a href="contact.html">Napisz</a>.</p></div></section>')

page("about.html","O nas | WorkNest PL","WorkNest PL wyjaśnia formy pracy w Polsce: etat, praca z domu, zlecenie i B2B. Bez ofert i bez pośrednictwa.",
head("O nas","O pracy w Polsce, po polsku.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Dla kogo</h2><p>WorkNest PL to niezależny serwis o rynku pracy: branże, umowy i umiejętności. Dla osoby, która układa kolejny krok, albo dokłada niepełny etat, pracę z domu albo zlecenie do tego, co już ma. Nie jesteśmy urzędem, agencją zatrudnienia ani portalem ogłoszeń.</p>
<p>Godzin jest mało, rachunki są prawdziwe, a ogłoszenia piszą „elastycznie”, „B2B” i „do”. Każdy poradnik mówi, na czym praca polega, jak może wyglądać tydzień i co sprawdzić, zanim podpiszesz.</p></div>
<div class="reveal"><h2>Jak piszemy</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Od strony osoby, która czyta ogłoszenie</h3><p>Godziny, brutto i netto, rodzaj umowy, ZUS i to, od czego zacząć.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Przy przepisach dajemy źródło</h3><p>Odsyłamy do PIP, ZUS, podatki.gov.pl, GUS i Barometru Zawodów, żeby dało się sprawdzić zdanie samemu.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Z datą</h3><p>Przy artykułach widać, kiedy tekst był aktualizowany. Przepisy o płacy i o pracy zdalnej się zmieniają.</p></div></div></div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Co znajdziesz</span><h2>Artykuły, porównania i kalkulator.</h2></div>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Formy pracy</a><a class="btn btn-ghost" href="knowledge-hub.html">Artykuły</a></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">WorkNest PL podaje ogólne informacje o pracy w Polsce. To nie jest porada prawna, podatkowa ani kadrowa. Jesteśmy publikacją internetową z redakcją w Warszawie. Nie podajemy numeru telefonu, żeby nikt nie wziął go za infolinię urzędu.</p></div></section>''')

page("contact.html","Kontakt | WorkNest PL","Napisz do WorkNest PL: pytanie, korekta albo pomysł na artykuł o pracy w Polsce.",
head("Kontakt","Pytanie, korekta albo pomysł.","Czytamy każdą wiadomość. Nie przysyłaj PESEL-u, serii dowodu, danych do banku ani kodów z mObywatel.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Imię</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">E-mail</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Temat</label><select id="topic"><option>Pytanie o niepełny etat</option><option>Pytanie o pracę z domu albo zdalną</option><option>Zlecenie, dzieło albo B2B</option><option>Podejrzane ogłoszenie</option><option>Pomysł na artykuł</option><option>Korekta</option></select></div>
<div class="field"><label for="msg">Wiadomość</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Wyślij</button>
<p class="notice">Wysłanie otwiera program pocztowy z wiadomością do {EMAIL}.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Dziękujemy za wiadomość.</h3><p>Powinien otworzyć się program pocztowy z gotową treścią. Zostaje nacisnąć wyślij.</p><p class="ok-sub">Jeśli nic się nie otworzyło, napisz na {EMAIL}.</p></div>
</div>
<div><h2>Inaczej</h2><ul class="contact-list">
<li><b>E-mail</b>{EMAIL}</li>
<li><b>Redakcja</b>Publikacja internetowa, Warszawa</li>
<li><b>Czego nie rób</b>Nie przysyłaj skanu dowodu ani danych do logowania</li>
</ul>
<p class="notice">Nie prowadzimy infolinii rekrutacyjnej. W sprawie prawa pracy: Państwowa Inspekcja Pracy i Zielona Linia 19524. Przy oszustwie: cert.pl, a gdy pieniądze już wyszły, bank i Policja.</p></div>
</div></section>''')

page("disclaimer.html","Zastrzeżenie | WorkNest PL","Zastrzeżenie serwisu WorkNest PL o formach pracy w Polsce.",
head("Zastrzeżenie","Zastrzeżenie")+'''
<section><div class="wrap article">
<h2>Tylko informacja</h2><p>WorkNest PL publikuje ogólne informacje o niepełnym etacie, pracy z domu, pracy zdalnej, zleceniu, umowie o dzieło, działalności i pracy tymczasowej w Polsce. Nie jesteśmy agencją zatrudnienia. Nie publikujemy wakatów i nie rekrutujemy, nie selekcjonujemy ani nie kierujemy kandydatów.</p>
<h2>Bez obietnicy pracy i zarobku</h2><p>Nic na tej stronie nie obiecuje zatrudnienia ani wysokości dochodu. Stawki, godziny i warunki różnią się między pracodawcami i zmieniają się w czasie. Płaca minimalna i stawka godzinowa to ustawowe podłogi dla części umów, nie typowa oferta z ogłoszenia.</p>
<h2>To nie jest porada</h2><p>Treści nie są poradą prawną, podatkową, kadrową ani finansową. Przepisy o pracy zdalnej, składkach i podatku się zmieniają. Potwierdź szczegóły w Państwowej Inspekcji Pracy, ZUS, Krajowej Administracji Skarbowej albo u osoby, która wykonuje taki zawód.</p>
<h2>Linki</h2><p>Linkujemy do urzędów i do prywatnych serwisów ogłoszeniowych jako miejsc, w których ludzie szukają pracy. Nie prowadzimy tych serwisów i nie odpowiadamy za ich treść. Wzmianka nie oznacza współpracy ani partnerstwa.</p>
<h2>Aktualność</h2><p>Staramy się poprawiać błędy. Nie gwarantujemy, że każde zdanie jest najświeższe. Jeśli coś się rozjechało, <a href="contact.html">napisz</a>.</p>
</div></section>''')

page("privacy.html","Prywatność | WorkNest PL","Jak WorkNest PL przetwarza dane osobowe zgodnie z RODO.",
head("Prywatność","Prywatność","Ostatnia aktualizacja: 17 listopada 2026")+f'''
<section><div class="wrap article">
<p>WorkNest PL („my”) szanuje prywatność i przetwarza dane osobowe zgodnie z rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 („RODO”). Ta informacja mówi, co się dzieje, gdy korzystasz ze strony albo piszesz do nas.</p>
<h2>1. Kto jest administratorem</h2>
<p>Administratorem danych podanych w wiadomości do redakcji jest wydawca serwisu WorkNest PL, publikacja internetowa z redakcją w Warszawie. Kontakt: {EMAIL}. Nie jesteśmy agencją zatrudnienia i nie prowadzimy bazy kandydatów.</p>
<h2>2. Jakie dane</h2>
<p>Dane zbieramy tylko wtedy, gdy sam je podasz w formularzu albo w mailu. Mogą to być: imię, adres e-mail i treść wiadomości.</p>
<p>Nie przysyłaj PESEL-u, serii i numeru dowodu, danych z mObywatel, kodów BLIK, numeru konta ani haseł. Nie poprosimy o nie.</p>
<p>Kalkulator godzin i lista sygnałów oszustwa liczą się w twojej przeglądarce. Tego, co tam wpiszesz albo zaznaczysz, nie wysyłamy i nie zapisujemy.</p>
<h2>3. Dane techniczne</h2>
<p>Serwer może zapisać typowe dane techniczne, takie jak adres IP, rodzaj przeglądarki i wywołany adres. Robimy to, żeby strona działała i żeby dało się reagować na nadużycia.</p>
<h2>4. Po co i na jakiej podstawie</h2>
<ul><li>odpowiedź na pytanie, korektę albo propozycję tematu, na podstawie prawnie uzasadnionego interesu, art. 6 ust. 1 lit. f RODO;</li><li>bezpieczeństwo i działanie strony, na tej samej podstawie;</li><li>obowiązek prawny, jeśli nas dotyczy, art. 6 ust. 1 lit. c RODO.</li></ul>
<p>Nie używamy tych danych do wysyłki reklamowej. Nie sprzedajemy danych.</p>
<h2>5. Komu je przekazujemy</h2>
<ul><li>dostawcom poczty i hostingu, tylko w zakresie potrzebnym do działania strony, na podstawie umowy;</li><li>organom publicznym, gdy przepis albo wezwanie tego wymaga;</li><li>innym osobom, jeśli sam o to poprosisz.</li></ul>
<h2>6. Poza Europejski Obszar Gospodarczy</h2>
<p>Dostawca poczty albo hostingu może przetwarzać dane poza EOG. Wtedy opieramy przekazanie na mechanizmie z RODO, na przykład na standardowych klauzulach umownych, albo na decyzji o adekwatności.</p>
<h2>7. Jak długo</h2>
<p>Wiadomość trzymamy tak długo, jak potrzeba, żeby odpowiedzieć i ewentualnie pokazać, skąd wzięła się korekta artykułu, a potem ją usuwamy albo skracamy tak, żeby nie dało się jej połączyć z tobą. Logi techniczne rotujemy w zwykłym cyklu hostingu.</p>
<h2>8. Twoje prawa</h2>
<p>Możesz prosić o dostęp, sprostowanie, usunięcie, ograniczenie przetwarzania, przeniesienie danych tam, gdzie ma to zastosowanie, oraz wnieść sprzeciw wobec przetwarzania opartego na prawnie uzasadnionym interesie. Część praw zależy od podstawy przetwarzania.</p>
<p>Napisz na {EMAIL}. Możemy poprosić o tyle informacji, ile potrzeba, żeby nie wydać danych innej osobie. Odpowiemy w terminie z RODO.</p>
<h2>9. Skarga</h2>
<p>Możesz złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych, ul. Stawki 2, 00-193 Warszawa, <a href="https://uodo.gov.pl" rel="noopener">uodo.gov.pl</a>.</p>
<h2>10. Inne strony</h2>
<p>Artykuły linkują do urzędów i serwisów ogłoszeniowych. Ich zasady prywatności są osobne. Przeczytaj je, zanim podasz im dane.</p>
<h2>11. Dzieci</h2>
<p>Serwis nie jest skierowany do dzieci. Jeśli uważasz, że dziecko podało nam dane, napisz. Usuniemy je.</p>
<h2>12. Zmiany</h2>
<p>Gdy zmienimy tę informację, nowa wersja będzie na tej stronie razem z datą.</p>
</div></section>''')

page("thank-you.html","Dziękujemy | WorkNest PL","Dziękujemy za wiadomość do WorkNest PL.",
head("Dziękujemy","Dziękujemy za wiadomość.","Odpowiemy na adres, z którego piszesz, gdy tylko przeczytamy.")+f'''
<section><div class="wrap" style="max-width:720px">
<p>W międzyczasie możesz czytać artykuły o rynku pracy w Polsce.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Czytaj artykuły</a><a class="btn btn-ghost" href="index.html">Wróć na start</a></div>
<p class="notice" style="margin-top:2rem">Chcesz coś dodać? Napisz na {EMAIL}.</p>
</div></section>''',extra_head='<meta name="robots" content="noindex">')

exec(open(pathlib.Path(__file__).with_name("articles2.py"),encoding="utf-8").read())
exec(open(pathlib.Path(__file__).with_name("jobpages.py"),encoding="utf-8").read())
for p in OUT.glob("*.html"):
    if p.name not in WRITTEN:
        p.unlink()
        print("removed", p.name)
print("built", len(WRITTEN))
