# Poradniki form pracy. Wykonywane z build.py (te same zmienne).

def _li(items): return "".join(f"<li>{i}</li>" for i in items)

def jobpage(fname,cls,eyebrow,h1,seo_title,seo_desc,intro,facts,roles,week,steps,know,questions,mistakes,faqs,related):
    facts_html="".join(f"<dt>{k}</dt><dd>{v}</dd>" for k,v in facts)
    roles_html="".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in roles)
    week_html="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in week)
    steps_html="".join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(steps))
    know_html="".join(f'<article class="tile"><h3>{t}</h3><p>{d}</p></article>' for t,d in know)
    faq_html="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    rel_html="".join(f'<a class="rel" href="{h}"><b>{t}</b><span>{d}</span></a>' for h,t,d in related)
    body=f'''
<div class="page-head jobhero {cls}"><div class="wrap jh-grid">
<div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{intro}</p>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Porównaj formy</a><a class="btn btn-ghost" href="knowledge-hub.html">Artykuły</a></div></div>
<aside class="qf" aria-label="Skrót"><h2>Skrót</h2><dl>{facts_html}</dl><p class="rv">Ostatnia aktualizacja: listopad 2026</p></aside>
</div></div>
<section><div class="wrap"><div class="head"><span class="eyebrow">Role</span><h2>Co ludzie naprawdę robią w tej formie.</h2></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Rola</th><th>Na czym polega</th></tr></thead><tbody>{roles_html}</tbody></table></div></div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Przykładowy tydzień</span><h2>Jak to może wyglądać obok twojego dnia.</h2><p class="lede">Przykład, nie grafik. Prawdziwe godziny zależą od pracodawcy.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Dzień</th><th>Godziny</th><th>Co robisz</th></tr></thead><tbody>{week_html}</tbody></table></div></div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">Od czego zacząć</span><h2>{len(steps)} kroków.</h2></div><ol class="steps">{steps_html}</ol></div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Zanim podpiszesz</span><h2>Co sprawdzić w praktyce.</h2></div><div class="tiles">{know_html}</div></div></section>
<section><div class="wrap split"><div><h2>Pytania</h2><ul class="qlist">{_li(questions)}</ul></div><div><h2>Czego nie rób</h2><ul class="qlist bad">{_li(mistakes)}</ul></div></div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><div class="head"><span class="eyebrow">Pytania</span><h2>Najczęstsze.</h2></div>{faq_html}</div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">Dalej</span><h2>Powiązane.</h2></div><div class="rels">{rel_html}</div>
<p class="notice" style="margin-top:1.5rem">Informacja ogólna. Stawki, godziny i warunki zależą od pracodawcy i nie są gwarantowane. Szczegóły potwierdź w <a href="https://www.pip.gov.pl" rel="noopener">Państwowej Inspekcji Pracy</a>, <a href="https://www.zus.pl" rel="noopener">ZUS</a> albo na <a href="https://www.podatki.gov.pl" rel="noopener">podatki.gov.pl</a>.</p></div></section>
<section class="alt"><div class="wrap" style="text-align:center;max-width:680px"><h2>Coś się zdezaktualizowało?</h2><p class="lede" style="margin-inline:auto">Przepisy i stawki się zmieniają. Napisz, jeśli zdanie trzeba poprawić.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="contact.html">Kontakt</a></div></div></section>'''
    page(fname,seo_title,seo_desc,body)

jobpage("praca-niepelny-etat.html","jh1","Niepełny etat","Praca na część etatu: wymiar, grafik i co sprawdzić",
"Niepełny etat w Polsce: wymiar, urlop i płaca minimalna | WorkNest PL",
"Poradnik o pracy na część etatu w Polsce: typowe role, przykładowy tydzień i co sprawdzić w umowie, na pasku wypłaty i w grafiku.",
"Większość osób bierze niepełny etat obok studiów, opieki albo głównej pracy. Przydatne pytania są przyziemne: które zmiany, kto układa grafik i czy po dojeździe kwota nadal ma sens.",
[("Wymiar","Ułamek pełnego etatu, na przykład 1/2 albo 3/4"),("Gdzie","Sklep, biuro, czasem dom"),("Umowa","Pracownik, umowa o pracę"),("ZUS i PIT","Pracodawca zgłasza i pobiera zaliczkę"),("Dla kogo","Studenci, rodzice, opiekunowie, osoby dokładające dochód")],
[("Sklep i gastronomia","Obsługa, kasa, wykładanie towaru, zamknięcie. Często zmiany, także wieczorem i w weekend w galerii."),("Asystent biura","Dokumenty, kalendarz, proste zestawienia, telefony. Zwykle w dni powszednie."),("Korepetycje i szkoła","Zajęcia, sprawdzanie, recepcja. Szczyt po południu i w weekend."),("Promocje i targi","Krótkie zmiany na targach albo w akcji sezonowej."),("Obsługa klienta","Telefon, czat albo mail w ustalonych zmianach.")],
[("Wtorek","16:00–20:00","Zmiana po głównej pracy albo po zajęciach"),("Czwartek","16:00–20:00","Druga zmiana w tygodniu"),("Sobota","10:00–18:00","Dzień w galerii albo w lokalu"),("Pozostałe dni","Wolne","Nauka, rodzina albo etat")],
[("Rozpisz prawdziwą dostępność","Wypisz dni i godziny, które możesz przeznaczyć co tydzień, razem z dojazdem. Liczy się regularność, nie maksymalna liczba godzin na papierze."),("Jednostronicowe CV","Na górze: dostępność, kontakt z ludźmi i narzędzia, których już używasz."),("Szukaj u źródła","Oferty urzędów, strona kariery firmy, którą sam otworzysz. Przeczytaj wymiar etatu i widełki, nie tylko tytuł."),("Weź warunki na piśmie","Wymiar, brutto, dzień wypłaty, okres próbny i wypowiedzenie. Ustalenie z czatu nie zastępuje umowy."),("Po kilku tygodniach sprawdź grafik","Jeśli zmiany rozjeżdżają się z tym, co podpisałeś, mów od razu, nie po kwartale.")],
[("Grafik","Dopytaj, z jakim wyprzedzeniem wychodzą zmiany i jak działają zamiany. Sezon, święta i wyprzedaże zwykle dokładają godzin."),("Wypłata","Ustal, czy kwota jest miesięczna od wymiaru etatu, czy godzinowa, i którego dnia wpływa. Zostaw paski."),("Urlop i L4","Przy niepełnym etacie urlop liczy się proporcjonalnie. Zwolnienie lekarskie działa, ale zasady wypłaty wynagrodzenia chorobowego zależą od stażu. Potwierdź u pracodawcy albo w ZUS."),("Główna umowa","Jeśli już masz etat, przeczytaj zakaz konkurencji, zanim weźmiesz drugą umowę.")],
["Jaki jest wymiar etatu i czy grafik jest stały?","Kwota w ogłoszeniu jest brutto czy netto i kiedy wpływa?","Czy to umowa o pracę?","Z jakim wyprzedzeniem znam zmiany?","Jaki jest okres próbny i wypowiedzenie?","Do kogo piszę, gdy muszę zmienić dostępność?"],
["Zgoda bez znajomości grafiku","Pomylenie brutto z kwotą na konto","Wzięcie większej liczby zmian, niż dasz radę","Pominięcie zakazu konkurencji w głównej umowie"],
[("Ile godzin to niepełny etat?","Tyle, ile wynika z wymiaru. 1/2 pełnego etatu to przeciętnie połowa 40 godzin, nie sztywny próg „poniżej 35”. Dokładny rozkład jest w umowie i w grafiku."),("Czy na części etatu jest urlop?","Tak, proporcjonalnie do wymiaru. Aktualne zasady potwierdź w Kodeksie pracy albo w PIP."),("Czy da się łączyć z pełnym etatem?","Często tak, jeśli główna umowa nie zabrania i jeśli godziny się nie pokrywają. Przeczytaj zakaz konkurencji.")],
[("artykul-zus.html","ZUS i pasek z wypłaty","Co widać na pasku"),("artykul-ogloszenie.html","Jak czytać ogłoszenie","Wymiar, brutto, umowa"),("praca-z-domu.html","Praca z domu","Kolejny poradnik")])

jobpage("praca-z-domu.html","jh2","Praca z domu","Praca z domu: godziny, sprzęt i czego dopytać",
"Praca z domu w Polsce: godziny, sprzęt i rodzaj umowy | WorkNest PL",
"Poradnik o pracy z domu w Polsce: typowe role, przykładowy tydzień i pytania o umowę, sprzęt oraz to, kto płaci za internet.",
"Praca z domu to najczęściej obsługa, administracja albo księgowość na ustalonych godzinach. Różnica między dobrą a słabą rolą siedzi w szczegółach: sprzęt, czas reakcji i rodzaj umowy.",
[("Godziny","Ustalone, część albo pełen etat"),("Gdzie","Dom"),("Umowa","Zwykle pracownik"),("ZUS","Zwykle jak przy etacie, jeśli to umowa o pracę"),("Dla kogo","Rodzice, opiekunowie, osoby, którym odpada codzienny dojazd")],
[("Obsługa klienta","Czat, mail albo telefon w systemach firmy."),("Praca biurowa","Dokumenty, formularze, prosta kontrola danych."),("Pomoc biurowa na odległość","Kalendarz, skrzynka, rezerwacje."),("Media społecznościowe","Posty, terminarz, proste grafiki, odpowiedzi."),("Transkrypcja i tłumaczenia","Z nagrania na tekst albo z języka na język, często za konkretne zlecenie.")],
[("Poniedziałek–piątek","8:00–12:00","Zmiana z domu, w godzinach szkoły"),("Środa","13:00–14:00","Spotkanie z zespołem"),("Weekend","Wolne","Bez dyżuru")],
[("Ułóż miejsce","Spokojny kąt, internet, który nie zrywa rozmowy, i laptop. Dopytaj, czy sprzęt jest służbowy."),("Wypisz, co już umiesz","Pisanie, dokładność, arkusz, poczta, narzędzie do rozmów."),("Szukaj firmy, którą da się znaleźć","Strona kariery albo publiczna oferta. Sprawdź, czy to etat, czy zlecenie."),("Dopytaj o zasady","Czas reakcji, godziny, nadzór, sposób rozliczania dnia."),("Weź to na piśmie","Godziny, kwota, sprzęt, ryczałt albo jego brak, wypowiedzenie.")],
[("Sprzęt i koszty","Kto daje laptop i programy. Czy prąd i internet zostają po twojej stronie, czy jest ryczałt."),("Nadzór","Część firm mierzy aktywność albo oczekuje odpowiedzi w kilka minut. Dopytaj, zanim uznasz, że „z domu” znaczy dowolnie."),("Etat czy zlecenie","Tytuł stanowiska tego nie rozstrzyga. Od umowy zależy urlop, ZUS i to, kto pilnuje podatku."),("Dane klientów","Przy danych osobowych będą zasady urządzeń i haseł. To nie jest formalność.")],
["Czy to etat, zlecenie czy B2B?","Jakie są godziny kontaktu i czy mierzycie aktywność?","Kto daje sprzęt?","Kwota jest brutto czy netto i kiedy wpływa?","Czy wdrożenie jest płatne?","Czy godziny mogą się zmienić i z jakim wyprzedzeniem?"],
["Założenie, że praca z domu nie ma godzin","Pomylenie pracy z domu ze zleceniem","Służbowe dane na wspólnym komputerze bez hasła","Zgoda bez ustaleń na piśmie"],
[("Czy praca z domu w Polsce jest realna?","Tak. Obsługa, administracja, księgowość i treść bywają robione z domu. Firmę i umowę sprawdzasz tak samo jak przy pracy w biurze."),("Czym to się różni od pracy zdalnej?","W mowie potocznej praca z domu to praca u siebie. Praca zdalna w Kodeksie pracy może być też w innym uzgodnionym miejscu. Zobacz poradnik o pracy zdalnej."),("Czy potrzebuję własnego laptopa?","Zależy od firmy. Dopytaj przed podpisem.")],
[("praca-zdalna.html","Praca zdalna","Więcej o pracy zdalnej"),("artykul-formy.html","Etat, hybryda, zlecenie","Co znaczą słowa"),("artykul-wniosek.html","Wniosek o pracę zdalną","Gdy już masz etat")])

jobpage("praca-zdalna.html","jh3","Praca zdalna","Praca zdalna: godziny, strona umowy i podatek",
"Praca zdalna w Polsce: hybryda, godziny i rodzaj umowy | WorkNest PL",
"Poradnik o pracy zdalnej w Polsce: role, wspólne godziny, pytanie o to, kto jest pracodawcą, oraz różnica między etatem a B2B.",
"Role zdalne częściej premiują konkretną umiejętność. Część jest w polskim centrum usług, część w zespole z innego kraju. Dla osoby mieszkającej tutaj liczy się, kto jest stroną umowy, które godziny musisz być dostępny i jak wygląda podatek.",
[("Godziny","Pełny albo niepełny etat"),("Gdzie","Uzgodnione miejsce, czasem hybryda"),("Umowa","Pracownik albo umowa B2B"),("ZUS","Zależy od tego, kto zatrudnia i na jakiej umowie"),("Dla kogo","Osoby z umiejętnością, które pracują bez nadzoru")],
[("Marketing i analityka","Kampanie, treści, raporty."),("Projektowanie","Grafika, makiety, strony."),("Programowanie i testy","Kod albo testy w rozproszonym zespole."),("Koordynacja","Terminy, klienci, dostawy."),("Księgowość oraz kadry i płace","Często w centrum usług wspólnych, z językiem obcym.")],
[("Poniedziałek–czwartek","9:00–17:00","Godziny wspólne z zespołem"),("Piątek","9:00–13:00","Krótszy dzień, raport"),("Weekend","Wolne","Bez dyżuru, chyba że umowa mówi inaczej")],
[("Pokaż robotę, nie deklarację","Krótkie portfolio albo przykład: raport, ekran, tekst. Zdalny zespół nie widzi, jak siedzisz przy biurku."),("Szukaj ról otwartych na twoje miasto","Część ogłoszeń wymaga dni w biurze w Krakowie, Wrocławiu albo Warszawie. Przeczytaj to w pierwszym akapicie."),("Ustal, kto jest stroną umowy","Polska spółka, agencja czy kontrahent z innego kraju. Od tego zależy ZUS i waluta."),("Rozmowa wideo","Sprawdź kamerę i łącze. Miej jeden przykład pracy bez stania nad biurkiem."),("Dopytaj o podatek i składki","Etat, zlecenie i faktura rozliczają się inaczej. Przy wątpliwości sprawdź na zus.pl i podatki.gov.pl.")],
[("Kto zatrudnia","Składki przy umowie o pracę nalicza polski pracodawca. Przy umowie z firmą z innego kraju albo przy B2B układ jest inny. Nie zakładaj, że „ktoś to ogarnie”."),("Wspólne godziny","Dopytaj, w jakich godzinach masz być dostępny. Zespół z Londynu i zespół ze Stanów to dwa różne wieczory."),("Waluta","Ustal walutę, dzień płatności i kto bierze opłatę banku."),("Podatek","Przychód od firmy z innego kraju nadal jest przychodem. Sposób rozliczenia zależy od umowy i od tego, gdzie masz miejsce zamieszkania dla podatku. Sprawdź na podatki.gov.pl.")],
["Kto jest stroną umowy i w jakim kraju?","Jakie godziny muszę być dostępny?","Etat, zlecenie czy faktura?","W jakiej walucie i którego dnia wpływa płatność?","Jaki sprzęt dostanę?","Kto zgłasza ZUS i jak rozliczam PIT?"],
["Pominięcie wspólnych godzin z inną strefą","Założenie, że kontrakt z zagranicy ma składki jak polski etat","Brak zapisu przychodu pod PIT","Zgoda ustna zamiast umowy"],
[("Czy praca zdalna jest tylko dla programistów?","Nie. Marketing, projektowanie, wsparcie, koordynacja, księgowość i kadry też bywają zdalne albo hybrydowe."),("Czy muszę mieszkać w mieście biura?","Część ról tego wymaga przez dni w biurze albo przez podatki. Dopytaj na początku, nie po trzeciej rozmowie."),("Czy płacę podatek od umowy z firmą z innego kraju?","Zależy od twojej sytuacji i od umowy. Sprawdź na podatki.gov.pl albo u doradcy. Nie zgadujemy stawki.")],
[("praca-freelance.html","Zlecenie i B2B","Gdy wolisz fakturę"),("artykul-cv.html","CV","Pokaż samodzielną robotę"),("praca-online.html","Praca online","Całość przez internet")])

jobpage("praca-online.html","jh4","Praca online","Praca online: kto płaci i na jakich zasadach",
"Praca online w Polsce: korepetycje, moderacja i na co uważać | WorkNest PL",
"Poradnik o pracy online w Polsce: korepetycje, moderacja, obsługa sklepu, przykładowy tydzień i pytania o to, kto płaci.",
"Praca online rozciąga się od korepetycji po moderację i sprawdzanie informacji. Skoro rozrzut jest tak duży, najważniejsze jest to, kto płaci i na jakiej umowie. Reszta jest dodatkiem.",
[("Godziny","Bloki albo stałe sesje"),("Gdzie","Przez internet"),("Umowa","Etat albo zlecenie, różnie"),("ZUS","Zależy od umowy"),("Dla kogo","Osoby, które chcą krótkie bloki przy ekranie")],
[("Korepetytor","Zajęcia jeden na jeden albo w małej grupie, na wideo."),("Moderator","Porządek w społeczności albo na czacie."),("Sprawdzanie informacji","Szukanie, sprawdzanie albo opisywanie informacji."),("Sklep internetowy","Opisy produktów, zamówienia, pytania klientów."),("Wydarzenia online","Czat, zapisy, techniczna obsługa transmisji.")],
[("Wtorek","17:00–19:00","Korepetycje"),("Czwartek","17:00–19:00","Korepetycje"),("Niedziela","14:00–17:00","Zamówienia albo opisy")],
[("Wybierz jedną umiejętność","Nauka, tekst, sprawdzanie informacji, porządek w arkuszu albo obsługa klienta."),("Przygotuj warsztat","Internet, który nie zrywa zajęć, spokojny kąt, program, którego rola wymaga."),("Znajdź firmę, nie samą nazwę z komunikatora","Nazwa, którą wpiszesz w KRS albo CEIDG, i sposób wypłaty."),("Ustalenia na piśmie","Stawka, termin płatności, to, czy pierwsze zajęcia są płatne, i rodzaj umowy."),("Zacznij od małego zlecenia","Jedna grupa albo jeden tydzień. Potem zdecyduj, czy dokładamy.")],
[("Kto płaci","Nazwa i rachunek albo lista płac, zanim zaczniesz. Nie wystarczy nazwa z Messengera."),("Opłata na start","Nie powinna być warunkiem pracy. Jeśli proszą o wpłatę, zatrzymaj się i sprawdź firmę."),("Rodzaj umowy","Od tego zależy ZUS, urlop i to, kto wystawia rachunek."),("Próba","Dopytaj, czy pierwsze zadania są płatne. „Szkolenie za darmo przez miesiąc” bywa sposobem na darmową robotę.")],
["Jak nazywa się firma i gdzie ją sprawdzę?","Płatność jest za godzinę, za zadanie czy miesięcznie?","Kiedy wpływa?","Czy mam coś wpłacić, żeby zacząć? Nie powinienem.","Etat czy zlecenie?","Co się dzieje, gdy uczeń odwoła zajęcia?"],
["Wpłata za „dostęp do zadań”","Praca bez wiedzy, kto płaci","Pominięcie przychodu w PIT","Ustalenia tylko na czacie, bez śladu"],
[("Czy praca online jest prawdziwa?","Część tak. Korepetycje, moderacja i obsługa sklepu są zwykłymi rolami. Sprawdź firmę i umowę."),("Co ludzie mają na myśli przez pracę online?","Robotę przez internet, z domu albo z innego miejsca, za ustaloną stawkę. Nie za obietnicę dniówki z reklamy."),("Czy jest ZUS?","Przy umowie o pracę tak. Przy zleceniu zależy od tytułu, w tym od statusu ucznia albo studenta do 26. roku życia. Przy dziele zwykle nie, z wyjątkami.")],
[("praca-z-domu.html","Praca z domu","Stałe godziny u siebie"),("praca-freelance.html","Zlecenie i B2B","Gdy sam bierzesz klientów"),("artykul-ogloszenie.html","Jak czytać ogłoszenie","Stawka i umowa")])

jobpage("praca-freelance.html","jh5","Zlecenie i B2B","Zlecenie, dzieło i działalność: od czego zacząć",
"Zlecenie, dzieło i B2B w Polsce: umowa, PIT i ZUS | WorkNest PL",
"Poradnik o zleceniu, umowie o dzieło, działalności nierejestrowanej i JDG: klienci, umowa, faktura, podatek i składki.",
"Własne zlecenia zamieniają pasek z wypłaty na kontrolę nad tygodniem. W zamian umowa, rachunek albo faktura, podatek i często ZUS zostają po twojej stronie.",
[("Godziny","Ustalasz sam"),("Gdzie","Dowolnie, byle oddać pracę na czas"),("Umowa","Zlecenie, dzieło albo działalność"),("ZUS","Zależy od umowy. Przy JDG płacisz sam"),("Dla kogo","Osoby z portfolio albo wąską umiejętnością")],
[("Grafika","Znaki, proste layouty, ilustracje."),("Tekst i tłumaczenie","Artykuły, hasła, korekta, pary językowe."),("Wideo i zdjęcia","Montaż krótkich form."),("Księgowość małych firm","Ewidencja i porządek w dokumentach."),("Strony","Proste serwisy i poprawki.")],
[("Poniedziałek","9:00–12:00","Projekt dla klienta A"),("Wtorek i środa","10:00–15:00","Projekt B i maile"),("Czwartek","Popołudnie","Rachunki i szukanie kolejnego zlecenia"),("Piątek","Wolne","Albo główny etat")],
[("Zawęź ofertę","Jedna albo dwie usługi, które umiesz powiedzieć jednym zdaniem."),("Dwa, trzy przykłady","Portfolio nie musi być duże. Ma pokazać skończoną robotę."),("Ustal cenę","Za godzinę albo za projekt. Dolicz poprawki, maile i podatek, nie tylko „samą robotę”."),("Skąd klienci","Polecenia, poprzednie miejsce pracy, profil. Portale są dodatkiem, nie planem."),("Umowa przed robotą","Zakres, termin, liczba poprawek, zaliczka przy większym zleceniu, termin płatności."),("Zapisuj przychód","Pod PIT. Przy działalności nierejestrowanej pilnuj limitu kwartalnego.")],
[("Umowa","Zakres, termin, poprawki i płatność na piśmie. Przy większej kwocie zaliczka od klienta, nie opłata tobie „za możliwość pracy”."),("Podatek","Przychód wykazujesz. Ulgi, w tym ulga dla młodych, mają swoje wyłączenia. Aktualne zasady są na podatki.gov.pl."),("ZUS","Zlecenie bywa oskładkowane, z wyjątkiem ucznia albo studenta do 26. roku życia. Dzieło zwykle nie, chyba że z własnym pracodawcą. JDG płaci składki przedsiębiorcy. Potwierdź w ZUS, zanim ułożysz cenę."),("Nierejestrowana czy CEIDG","Od 2026 r. działalność nierejestrowana mieści się w 10 813,50 zł przychodu na kwartał, jeśli spełniasz też pozostałe warunki ustawy. Po przekroczeniu jest 7 dni na wpis do CEIDG. Osoba zarejestrowana jako bezrobotna ma osobny, niższy limit przychodu. Zapytaj w urzędzie pracy, zanim zaczniesz.")],
["Co dokładnie jest w zakresie?","Ile poprawek jest w cenie?","Jaki jest harmonogram płatności?","Do kogo należą prawa do gotowej pracy?","Czy jest zaliczka?","Co przy zmianie zakresu?"],
["Start bez umowy","Cena, w której nie ma maili i podatku","Brak ewidencji pod PIT","Pięciu klientów naraz w pierwszym miesiącu"],
[("Czy przy zleceniu jest ZUS od klienta?","Nie ma „składek pracodawcy” jak przy etacie. Przy zleceniu składki często są, przy studencie do 26. roku życia często ich nie ma, przy JDG płacisz je sam. Sprawdź w ZUS, jaka to umowa."),("Czy muszę zakładać firmę?","Nie zawsze. Działalność nierejestrowana ma limit przychodu i warunki z Prawa przedsiębiorców. Powyżej limitu jest CEIDG. To nie jest porada dla twojej sytuacji, tylko kierunek, gdzie sprawdzić."),("Skąd brać zlecenia?","Najczęściej z polecenia i z ludzi, z którymi już pracowałeś. Portal jest dodatkiem.")],
[("praca-zdalna.html","Praca zdalna","Gdy wolisz etat"),("artykul-formy.html","Rodzaje umów","Etat a zlecenie"),("dorabianie.html","Dorabianie","Porównanie dróg")])

jobpage("dorabianie.html","jh6","Dorabianie","Jak dołożyć dochód: drogi obok siebie",
"Dorabianie w Polsce: etat, praca z domu, zlecenie | WorkNest PL",
"Porównanie dróg dorabiania w Polsce: niepełny etat, praca z domu, praca online i zlecenie, z kalkulatorem godzin bez obietnicy kwoty.",
"Osoby, które chcą dołożyć dochód, zwykle wybierają jedną z czterech dróg: niepełny etat, pracę z domu, pracę online albo zlecenie. Każda pasuje do innych godzin i innej potrzeby spokoju wypłaty.",
[("Drogi","Etat na część, praca z domu, online, zlecenie"),("Czas","Od kilku godzin w tygodniu"),("Start","Najpierw godziny, potem forma"),("Pieniądze","Zależą od roli i godzin, nikt ich nie gwarantuje")],
[("Niepełny etat","Grafik i umowa o pracę, w miejscu albo z domu. <a href='praca-niepelny-etat.html'>Poradnik</a>."),("Praca z domu","Rola z godzinami, u siebie. <a href='praca-z-domu.html'>Poradnik</a>."),("Praca online","Korepetycje, moderacja, sklep. <a href='praca-online.html'>Poradnik</a>."),("Zlecenie albo B2B","Płatność za projekt, sam układasz tydzień. <a href='praca-freelance.html'>Poradnik</a>.")],
[("Krok 1","Kwota","Ile chcesz dołożyć w miesiącu, na rękę."),("Krok 2","Stawka","Z prawdziwego ogłoszenia albo z twojej wyceny, nie z reklamy."),("Krok 3","Godziny","Policz w kalkulatorze niżej.")],
[("Nazwij kwotę","Ile ma zostać po dojeździe i po opiece, nie „ile brzmi dobrze”."),("Policz wolne godziny","Szczerze, razem z drogą i ze snem."),("Wybierz drogę","Stały grafik: niepełny etat. Własne tempo i klienci: zlecenie."),("Szukaj u źródła","Publiczne oferty i strony firm. Komunikator z nieznajomym nie jest źródłem."),("Po miesiącu sprawdź","Czy godziny, wypłata i zmęczenie nadal się spinają.")],
[("Oczekiwania","Kwota zależy od roli, umiejętności i godzin. Ogłoszenie z wysoką dniówką za proste klikanie jest powodem do ostrożności, nie do planu."),("Koszty","Dojazd, sprzęt, internet, żłobek, podatek."),("Ochrona","Etat ma urlop i składki po stronie pracodawcy. Zlecenie i JDG układają to inaczej."),("Siły","Drugie zajęcie, które zjada sen, szybko przestaje być dochodem.")],
["Ile godzin tygodniowo naprawdę mam?","Potrzebuję stałej wypłaty czy mogę znieść cichszy miesiąc?","Etat czy działalność?","Jakie koszty dojdą?","Jak zapiszę przychód pod PIT?","Czy główna umowa pozwala dorabiać?"],
["Gonienie ogłoszeń o łatwych pieniądzach","Pominięcie kosztów i podatku","Więcej godzin, niż dasz radę","Brak umowy"],
[("Która droga jest najłatwiejsza?","Żadna nie jest łatwa dla wszystkich. Niepełny etat i praca z domu dają spokojniejszy grafik. Zlecenie daje kontrolę i większą nierówność miesięcy."),("Czy da się zacząć bez doświadczenia?","Część ról w obsłudze i w handlu nie wymaga długiego stażu. Wymagania zależą od firmy."),("Czy dochód z domu trzeba wykazać?","Przychód z pracy, zlecenia i działalności co do zasady tak, w PIT. Ulgi sprawdź na podatki.gov.pl.")],
[("praca-niepelny-etat.html","Niepełny etat","Stałe godziny"),("praca-freelance.html","Zlecenie i B2B","Własny grafik"),("artykul-koszty.html","Czynsz i rata","Kiedy dorabianie ma sens")])

_p=OUT/"dorabianie.html"
_h=_p.read_text(encoding="utf-8")
_calc='''<section class="alt"><div class="wrap split"><div><span class="eyebrow">Kalkulator</span><h2>Ile godzin w tygodniu?</h2><p class="lede">Wpisz swoje liczby. Nic nie jest zapisywane ani wysyłane. Wynik nie jest obietnicą wypłaty.</p></div>
<form class="fit" id="calc" onsubmit="return false"><div class="field"><label for="c-target">Ile chcesz dołożyć miesięcznie (zł)</label><input id="c-target" inputmode="decimal" placeholder="np. 800"></div>
<div class="field"><label for="c-rate">Stawka za godzinę (zł)</label><input id="c-rate" inputmode="decimal" placeholder="np. 31,40"></div>
<div id="c-out" class="fit-out" role="status" aria-live="polite" hidden></div></form></div></section>'''
_h=_h.replace('<section class="alt"><div class="wrap" style="max-width:860px">',_calc+'<section class="alt"><div class="wrap" style="max-width:860px">',1)
_p.write_text(_h,encoding="utf-8")

_h=_p.read_text(encoding="utf-8")
for a,b in [("Przykładowy tydzień","Policz"),("Jak to może wyglądać obok twojego dnia.","Trzy kroki do realnego planu."),("Przykład, nie grafik. Prawdziwe godziny zależą od pracodawcy.","Krok trzeci jest w kalkulatorze niżej."),("<th>Dzień</th><th>Godziny</th><th>Co robisz</th>","<th>Krok</th><th>Co</th><th>Po co</th>")]:
    _h=_h.replace(a,b,1)
_p.write_text(_h,encoding="utf-8")

TAKE.update({
"artykul-wniosek.html":["Pracownik może wnioskować o pracę zdalną. Zgoda nie jest automatyczna.","Napisz, o jaki układ prosisz, od kiedy i jak praca zostanie zrobiona.","Okres próbny ustaleń, z datą przeglądu, ułatwia zgodę.","Okazjonalnie limit wynosi 24 dni w roku. Przy części osób pracodawca odmawia tylko z przyczyny związanej z rodzajem albo organizacją pracy."],
"artykul-zus.html":["Przy umowie o pracę składki i zaliczka na PIT są po stronie pracodawcy, także na niepełnym etacie.","Pasek pokazuje brutto, składki, zaliczkę i kwotę do wypłaty.","Zlecenie studenta albo ucznia do 26. roku życia często jest bez składek ZUS. Etat w tym wieku już nie.","Stawki składek zmieniają się. Aktualne tabele są na zus.pl."],
"artykul-ogloszenie.html":["Najpierw wymiar, miejsce, rodzaj umowy i to, czy kwota jest brutto.","„Do” i widełki nie są stawką, którą dostaniesz.","Okres próbny i wypowiedzenie przeczytaj przed wysłaniem CV, nie po ofercie.","Firmę sprawdź sam, nie linkiem z wiadomości."],
"artykul-cv.html":["Pokaż rzeczy zrobione samodzielnie, bez stania nad biurkiem.","Wypisz narzędzia, których już używasz.","Napisz wprost, w jakich godzinach jesteś dostępny i w jakiej strefie.","Jedna albo dwie strony wystarczą."],
})

article("artykul-wniosek.html","Wniosek o pracę zdalną, krok po kroku","Jak złożyć wniosek o pracę zdalną albo o dni okazjonalne u polskiego pracodawcy.","Prawo",'''
<p class="lede">Jeśli masz już umowę o pracę i chcesz część tygodnia z domu, inny wymiar albo inne godziny, da się to napisać. Dobrze napisany wniosek zwiększa szansę. Nie zamienia jej w zgodę.</p>
<h2>Nazwij, o co prosisz</h2><ul><li><strong>Praca zdalna stała albo hybrydowa:</strong> uzgodnione miejsce i dni, zwykle ze sprzętem albo ryczałtem.</li><li><strong>Okazjonalna praca zdalna:</strong> do 24 dni w roku kalendarzowym, na twój wniosek. Niewykorzystane dni nie przechodzą na kolejny rok.</li><li><strong>Inny wymiar:</strong> na przykład przejście na 3/4 albo 1/2 etatu. To osobna zmiana umowy, nie „praca zdalna”.</li></ul>
<h2>Krok po kroku</h2><ol><li>Przeczytaj umowę i regulamin. Część firm ma już tryb wniosków.</li><li>Napisz, jakich dni albo jakiego wymiaru chcesz, od kiedy i na jak długo.</li><li>Napisz, jak praca zostanie zrobiona: godziny kontaktu, zastępstwo, co zostaje w biurze.</li><li>Zaproponuj okres próbny ustaleń i datę, kiedy razem sprawdzicie, czy układ działa.</li><li>Złóż wniosek na piśmie albo mailem, tak jak wymaga regulamin. Zostaw sobie kopię.</li><li>Jeśli nie ma odpowiedzi, przypomnij się spokojnie. Brak odpowiedzi nie jest zgodą.</li></ol>
<h2>Czego się spodziewać</h2><p>Pracodawca może odmówić. Przy okazjonalnej pracy zdalnej odmowa nie wymaga rozbudowanego uzasadnienia. Przy wnioskach części pracowników, między innymi osób w ciąży oraz opiekujących się małym dzieckiem, przepisy wiążą odmowę z rodzajem albo organizacją pracy i z podaniem przyczyny. Katalog osób i terminy sprawdź w Kodeksie pracy albo w PIP, bo to nie jest streszczenie całego rozdziału.</p>
<div class="callout"><p>Wniosek nie jest gwarancją. Najmocniejszy jest konkret: dni, godziny kontaktu i data przeglądu.</p></div>''')

article("artykul-zus.html","ZUS, PIT i pasek z wypłaty","Co sprawdzić przy niepełnym etacie i przy zleceniu, zanim uznasz kwotę z ogłoszenia za wypłatę.","Prawo",'''
<p class="lede">Przy drugiej pracy pytanie praktyczne brzmi inaczej niż „czy ZUS istnieje”. Brzmi: czy ta umowa jest oskładkowana, kto zgłasza i co z tego widać na pasku.</p>
<h2>Umowa o pracę</h2><p>Pracodawca zgłasza cię do ubezpieczeń i pobiera zaliczkę na podatek, także przy niepełnym etacie. Płaca minimalna spada proporcjonalnie do wymiaru. W 2026 r. pełen etat ma podłogę 4&nbsp;806&nbsp;zł brutto, więc 1/2 etatu to 2&nbsp;403&nbsp;zł brutto. To podłoga, nie typowa oferta w twoim zawodzie.</p>
<h2>Co jest na pasku</h2><ul><li>Brutto i okres, którego dotyczy.</li><li>Składki finansowane przez ciebie.</li><li>Zaliczka na PIT.</li><li>Kwota do wypłaty.</li></ul>
<p>Jeśli paska nie dostajesz, poproś. Bez niego trudno sprawdzić, czy zgłoszenie w ogóle jest.</p>
<h2>Zlecenie</h2><p>Przy zleceniu składki często są, ale uczeń albo student do 26. roku życia zwykle ich nie płaci. To nie jest to samo co ulga dla młodych w PIT i nie dotyczy etatu. Umowa o dzieło zwykle nie rodzi składek, z ważnym wyjątkiem: dzieło z własnym pracodawcą. Zanim ułożysz sobie „na rękę”, dopytaj, jaki to tytuł.</p>
<h2>B2B</h2><p>Na fakturze nie ma paska. Składki przedsiębiorcy i podatek liczysz sam albo z księgową. Ulga na start i niższy ZUS mają terminy. Nie obiecujemy, która forma podatku wyjdzie taniej. To zależy od przychodu i od twojej sytuacji.</p>
<h2>Pytania przed podpisem</h2><ul><li>Czy to umowa o pracę?</li><li>Kto zgłasza mnie do ZUS i od którego dnia?</li><li>Kiedy dostanę pasek albo rachunek?</li></ul>
<p>Więcej o godzinach jest w <a href="praca-niepelny-etat.html">poradniku o niepełnym etacie</a>.</p>''')

article("artykul-ogloszenie.html","Jak czytać ogłoszenie o pracę","Na co patrzeć w ogłoszeniu o niepełny etat, pracę z domu i pracę zdalną.","Podstawy",'''
<p class="lede">Ogłoszeń czyta się dużo. Przy elastycznych rolach kilka linijek decyduje o tym, czy to etat, zlecenie, czy prośba o wpłatę.</p>
<h2>Cztery rzeczy na początku</h2><ul><li><strong>Wymiar:</strong> 1/2 etatu, „około 20 godzin”, albo „elastycznie” bez liczby. Bez liczby nie wiesz, czy dasz radę.</li><li><strong>Miejsce:</strong> „home office” bywa jednym dniem w tygodniu. Dopytaj, zanim ułożysz opiekę.</li><li><strong>Umowa:</strong> o pracę, zlecenie, dzieło albo B2B. Od tego zależy urlop, ZUS i podatek.</li><li><strong>Pieniądze:</strong> za godzinę, miesięcznie, za sztukę albo sama prowizja. I czy to brutto.</li></ul>
<h2>Słowa przy kwocie</h2><p>„Do” jest sufitem widełek, nie stawką. Sama prowizja zależy od wyniku i bywa zerem w słabym miesiącu. Przy zleceniu, którego dotyczy stawka godzinowa, podłoga w 2026 r. to 31,40&nbsp;zł brutto. Ogłoszenie wyraźnie pod tą kwotą jest powodem do pytania, nie do entuzjazmu.</p>
<h2>Drobny druk</h2><ul><li>Okres próbny i wypowiedzenie w jego trakcie.</li><li>Zakaz konkurencji, jeśli już gdzieś pracujesz.</li><li>Kto daje laptop i kto płaci za dojazd albo internet.</li><li>Opłata „za szkolenie” albo „za wydanie odzieży” przed startem. To sygnał, nie formalność.</li></ul>
<h2>Sprawdź firmę</h2><p>Nazwę wpisz sam w KRS albo CEIDG. Ofertę porównaj ze stroną kariery. Agencję znajdź w KRAZ. Mniej znane słowa są w <a href="glossary.html">słowniku</a>.</p>''')

article("artykul-cv.html","CV do pracy zdalnej i z domu","Jak ułożyć CV, gdy pracodawca nie widzi, jak pracujesz.","Kariera",'''
<p class="lede">Przy pracy zdalnej nikt nie patrzy, czy siedzisz przy biurku. CV ma pokazać, że pracujesz samodzielnie.</p>
<h2>Najpierw wynik</h2><p>Krótkie punkty: ile zgłoszeń domknąłeś, jaki materiał wyszedł na czas, jaki kawałek procesu wziąłeś od początku do końca. Nie lista obowiązków przepisana z poprzedniej umowy.</p>
<h2>Narzędzia, których już używasz</h2><ul><li>Poczta, czat, arkusz, rozmowy wideo, lista zadań.</li><li>Pisanie: krótko i konkretnie. Przy centrach usług dopisz język i poziom, jeśli umiesz go udowodnić.</li><li>Terminy, których dotrzymujesz.</li></ul>
<h2>Godziny wprost</h2><p>Napisz, w jakich godzinach jesteś dostępny i że mieszkasz w Polsce, jeśli masz pracować w tych samych godzinach co zespół z innego kraju. Przy niepełnym etacie dostępność jest ważniejsza niż dodatkowa strona o zainteresowaniach.</p>
<h2>Porządek</h2><p>Jedna albo dwie strony, prosty układ, trzy zdania na górze. Link do portfolio, jeśli masz co pokazać. Zdjęcie dowodu nie jest elementem CV.</p>
<p>Role, do których to CV pasuje, są w <a href="praca-z-domu.html">poradniku o pracy z domu</a>.</p>''')
