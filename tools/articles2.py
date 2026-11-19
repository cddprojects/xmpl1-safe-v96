GUS="https://stat.gov.pl"
SRC={
"gus":("Główny Urząd Statystyczny",GUS),
"barometr":("Barometr Zawodów","https://barometrzawodow.pl"),
"mrpips":("Ministerstwo Rodziny, Pracy i Polityki Społecznej","https://www.gov.pl/web/rodzina"),
"oferty":("oferty.praca.gov.pl","https://oferty.praca.gov.pl"),
"zus":("ZUS","https://www.zus.pl"),
"podatki":("Podatki.gov.pl","https://www.podatki.gov.pl"),
"pip":("Państwowa Inspekcja Pracy","https://www.pip.gov.pl"),
"bur":("Baza Usług Rozwojowych","https://uslugirozwojowe.parp.gov.pl"),
"zielona":("Zielona Linia","https://zielonalinia.gov.pl"),
"placa":("Minimalna stawka godzinowa, gov.pl","https://www.gov.pl/web/rodzina/minimalna-stawka-godzinowa"),
}
def stats(items):
    return '<div class="statrow">'+"".join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n,t in items)+'</div>'
for k,v in {
"artykul-branze.html":["gus","barometr","mrpips"],
"artykul-zawody.html":["barometr","oferty","gus"],
"artykul-dorabianie.html":["placa","podatki","zus"],
"artykul-trend-zdalna.html":["pip","mrpips"],
"artykul-szkolenia.html":["bur","zielona"],
"artykul-dane-rynku.html":["gus","barometr","oferty"],
}.items(): SOURCES[k]=[SRC[x] for x in v]

TAKE.update({
"artykul-branze.html":["W raportach wracają opieka, produkcja, budownictwo, logistyka i centra usług wspólnych.","Ten sam zawód bywa deficytem w jednym województwie i równowagą w innym.","IT nie jest jedną branżą: część specjalizacji jest rozchwytywana, na część juniorskich ról kandydatów jest więcej niż ofert.","Zanim wybierzesz kierunek, otwórz aktualny Barometr Zawodów dla swojego województwa."],
"artykul-zawody.html":["Ogłoszenia skupiają się wokół opieki, rzemiosła i produkcji, logistyki, danych oraz finansów i obsługi w centrach usług.","Część tych ról da się robić na niepełny etat, na zastępstwo albo zdalnie. Dopytaj, nie zakładaj.","Widełki z ogłoszenia to nie obietnica. Porównaj je z kilkoma aktualnymi ofertami.","Krótki kurs ma sens jako most do roli, którą już widzisz w ogłoszeniach."],
"artykul-dorabianie.html":["Niepełny etat dokłada dochód bez wychodzenia z umowy o pracę jako formy.","Praca z domu odcina dojazd, nie odcina podatku.","Zlecenie studenta do 26. roku życia i etat osoby w tym samym wieku to dwa różne układy składek.","Każdą obietnicę wysokiej dniówki za proste klikanie traktuj jak sygnał, nie jak plan."],
"artykul-trend-zdalna.html":["Praca zdalna jest nazwana w Kodeksie pracy, nie tylko w ogłoszeniu.","Okazjonalnie to najwyżej 24 dni w roku i tylko na wniosek pracownika.","Stała praca zdalna albo hybryda to osobne ustalenie: sprzęt albo ryczałt, miejsce, zasady kontaktu.","Wniosek nie jest zgodą. Pracodawca może odmówić, a przy części osób musi podać przyczynę."],
"artykul-szkolenia.html":["Najpierw dwa albo trzy ogłoszenia, potem kurs pod luki, nie odwrotnie.","Krajowy Fundusz Szkoleniowy uruchamia pracodawca przez powiatowy urząd pracy.","Osoba zarejestrowana w urzędzie pyta o szkolenie albo staż tam, nie na przypadkowej stronie z obietnicą pracy.","Nie płać za kurs, który gwarantuje zatrudnienie albo konkretną kwotę."],
"artykul-dane-rynku.html":["Stopa bezrobocia rejestrowanego i badanie aktywności ekonomicznej mierzą różne grupy ludzi.","Liczba ogłoszeń w internecie nie jest liczbą wolnych miejsc z urzędu.","Mediana albo przeciętne wynagrodzenie to środek rozkładu, nie oferta dla ciebie.","Najpierw tabela GUS albo Barometr dla województwa, potem komentarz."],
})
EXTRA.update({
"artykul-branze.html":([("Gdzie są najświeższe liczby?","GUS publikuje bezrobocie i wynagrodzenia, a Barometr Zawodów pokazuje zawody deficytowe, zrównoważone i nadwyżkowe w podziale na województwa."),("Czy rosnąca branża znaczy, że łatwo o pracę?","Nie. W jednym zawodzie brakuje ludzi, w sąsiednim jest tłok. Liczą się umiejętności i województwo.")],[("artykul-zawody.html","Zawody z ogłoszeń"),("artykul-dane-rynku.html","Jak czytać dane"),("artykul-szkolenia.html","Szkolenia")]),
"artykul-zawody.html":([("Czy te role da się robić na część etatu albo zdalnie?","Część tak, zwłaszcza analizę, treść, wsparcie i koordynację. Produkcja i opieka częściej mają zmiany na miejscu. Dopytaj w konkretnej firmie."),("Czy potrzebny jest dyplom?","Zależy od roli. W ogłoszeniach obok studiów coraz częściej stoi konkretna umiejętność albo uprawnienie.")],[("artykul-branze.html","Branże"),("artykul-szkolenia.html","Szkolenia"),("praca-zdalna.html","Praca zdalna")]),
"artykul-dorabianie.html":([("Ile godzin zajmie dorabianie?","Zależy od kwoty i stawki. Rząd wielkości policzysz w <a href='dorabianie.html'>kalkulatorze</a>."),("Czy muszę powiedzieć głównemu pracodawcy?","Przeczytaj umowę, zwłaszcza zakaz konkurencji i obowiązek informowania o dodatkowym zajęciu. Część umów tego wymaga.")],[("praca-niepelny-etat.html","Niepełny etat"),("praca-z-domu.html","Praca z domu"),("praca-freelance.html","Zlecenie i B2B")]),
"artykul-trend-zdalna.html":([("Czy mogę złożyć wniosek o pracę z domu?","Tak. Osobno działa praca zdalna uzgodniona na stałe albo hybrydowo i osobno praca okazjonalna, do 24 dni. Krok po kroku jest w poradniku."),("Czy rola zdalna jest otwarta dla osoby mieszkającej w Polsce?","Część tak. Sprawdź strefę czasową, to, kto jest stroną umowy, i w jakiej walucie przyjdzie płatność.")],[("artykul-wniosek.html","Wniosek o pracę zdalną"),("praca-zdalna.html","Praca zdalna"),("artykul-cv.html","CV")]),
"artykul-szkolenia.html":([("Kto może skorzystać z dofinansowania?","To zależy od ścieżki: pracodawca wnioskuje o środki z KFS, osoba zarejestrowana w urzędzie pracy pyta o szkolenie urzędu, a baza usług rozwojowych opisuje usługi, przy których bywa dopłata. Kwoty się zmieniają."),("Czy da się uczyć przy niepełnym etacie?","Wiele kursów jest wieczorami albo online. Sprawdź, czy zjazd wypada w twoim grafiku, zanim zapłacisz.")],[("artykul-zawody.html","Zawody z ogłoszeń"),("artykul-powrot.html","Powrót po przerwie"),("artykul-cv.html","CV")]),
"artykul-dane-rynku.html":([("Czym wolne miejsce różni się od ogłoszenia na portalu?","Urząd i GUS liczą zgłoszone miejsca. Na portalu to samo ogłoszenie bywa powtórzone, a część już obsadzona."),("Gdzie są oficjalne tabele?","Na stat.gov.pl oraz w Barometrze Zawodów, w rozbiciu na województwa.")],[("artykul-branze.html","Branże"),("artykul-zawody.html","Zawody z ogłoszeń"),("glossary.html","Słownik")]),
})

article("artykul-branze.html","Gdzie w Polsce naprawdę przybywa pracy","Które branże wracają w danych o polskim rynku pracy i co z tego wynika przy wyborze kierunku.","Branże",f'''
<p class="lede">Polski rynek pracy nie jedzie w jedną stronę. W jednym województwie brakuje opiekunów i spawaczy, w innym tłok jest na stanowiskach, które rok wcześniej wyglądały na pewne. Tu jest obraz, bez obietnicy, że „branża rośnie, więc cię wezmą”.</p>
{stats([("5","grup, które wracają w danych: opieka, produkcja, budownictwo, logistyka, centra usług"),("Województwo","Barometr Zawodów czyta się lokalnie, nie z nagłówka ogólnopolskiego"),("4 806 zł","płaca minimalna brutto na pełen etat od 1 stycznia 2026 r.")])}
<h2>Opieka i zdrowie</h2><p>Starzejące się społeczeństwo trzyma popyt na pielęgniarki, opiekunów, fizjoterapeutów i rejestrację. Dużo z tych ról to zmiany, czasem niepełny etat, rzadziej pełna praca z domu.</p>
<h2>Produkcja, budownictwo i rzemiosło</h2><p>Spawacze, elektrycy, operatorzy maszyn i brygady budowlane regularnie wpadają w deficyt Barometru. To praca na miejscu, często zmianowa, z uprawnieniami ważniejszymi niż sam dyplom.</p>
<h2>Logistyka</h2><p>Magazyny przy obwodnicach dużych miast, kompletacja i transport. Grafik bywa wieczorny i weekendowy. Dla części osób to realne dorabianie, dla części główna praca.</p>
<h2>Centra usług i finanse</h2><p>W Warszawie, Krakowie, Wrocławiu, Trójmieście, Poznaniu, Katowicach i Łodzi stoją centra księgowości, kadr, obsługi klienta i zgodności. Hybryda jest tu częstsza niż przy taśmie. Język obcy bywa warunkiem, nie dodatkiem.</p>
<h2>Technologie, bez jednego hasła</h2><p>Dane, bezpieczeństwo, utrzymanie systemów i część ról produktowych nadal się pojawiają. Jednocześnie na wiele ról juniorskich kandydatów jest więcej niż ofert. Patrz na konkretne ogłoszenie, nie na zdanie „w IT biorą każdego”.</p>
<h2>Co z tego masz</h2><p>Przy zmianie zawodu albo przy dorabianiu patrz na umiejętność z ogłoszenia, nie na nazwę branży. Sąsiednie umiejętności przenoszą się łatwiej niż tytuł stanowiska. I otwórz Barometr dla swojego województwa: deficyt w podlaskim nie jest deficytem w dolnośląskim.</p>
<div class="callout"><p>Liczby zmieniają się co kwartał i co rok. Płacę minimalną i stawki potwierdź w aktualnym rozporządzeniu oraz na gov.pl. Barometr czytaj w edycji na swój rok.</p></div>''')

article("artykul-zawody.html","Zawody, o które pytają pracodawcy","Jakie grupy ról wracają w polskich ogłoszeniach i jak czytać ten trend bez obietnicy zatrudnienia.","Zawody",f'''
<p class="lede">Nazwy stanowisk żyją krócej niż umiejętności, o które naprawdę pytają. W polskich ogłoszeniach te umiejętności układają się w kilka grup.</p>
{stats([("Opieka","pielęgniarka, opiekun, fizjoterapia, rejestracja"),("Warsztat","spawanie, elektryka, maszyny, budowa"),("Biuro usług","księgowość, kadry, obsługa w języku obcym"),("Dane","analiza, raporty, porządek w systemach")])}
<h2>Opieka</h2><p>Pielęgniarki, opiekunowie osób starszych, fizjoterapeuci i personel rejestracji wracają w planach kadrowych szpitali i opieki środowiskowej. Zmianowość jest tu normą.</p>
<h2>Produkcja i budowa</h2><p>Uprawnienia i praktyka liczą się bardziej niż ogólny „profil techniczny”. Część firm bierze osoby po kursie spawania albo uprawnieniach elektrycznych, jeśli da się pokazać robotę, nie tylko papier.</p>
<h2>Centra usług i finanse</h2><p>Księgowość, kadry i płace, obsługa klienta, sprawdzanie klientów, koordynacja. Wejście bywa przez język i dokładność, nie przez jeden certyfikat. Hybryda jest częsta, pełna dowolność miejsca rzadziej.</p>
<h2>Dane, marketing, treść</h2><p>Analiza, reklama w internecie, treści, projektowanie. Tu częściej widać zlecenie i B2B. Faktura nie jest „wyższą formą etatu”: sam liczysz ZUS i podatek.</p>
<h2>Jak użyć tej listy</h2><ul><li>Otwórz kilka aktualnych ogłoszeń i porównaj widełki. „Do” jest sufitem.</li><li>Czytaj wymagania, nie tylko tytuł.</li><li>Dopytaj, czy jest niepełny etat, hybryda albo umowa na czas określony. Nie zakładaj, że jest.</li></ul>
<p>Formy umów, które stoją pod tymi rolami, są w <a href="jobs.html">zestawieniu</a>.</p>''')

article("artykul-dorabianie.html","Dlaczego tyle osób dokłada drugie zajęcie","Niepełny etat, praca z domu i zlecenie jako drugi dochód w Polsce: co ustalić, zanim się zgodzisz.","Dorabianie",f'''
<p class="lede">Coraz więcej osób dokłada zmianę w handlu, kilka godzin obsługi klienta z domu albo zlecenie w weekend. Powody są przyziemne.</p>
{stats([("1/2","przykładowy niepełny etat, nie „poniżej 35 godzin”"),("31,40 zł","minimalna stawka godzinowa brutto przy części zleceń w 2026 r."),("24 dni","limit okazjonalnej pracy zdalnej w roku")])}
<h2>Rachunki są głównym powodem</h2><p>Najem albo rata, żłobek, żywność i dojazd. Drugie zajęcie daje oddech, jeśli godziny naprawdę istnieją w twoim tygodniu. Nie zmienia zawodu samo z siebie.</p>
<h2>Form jest więcej niż pięć lat temu</h2><p>Niepełny etat, praca z domu, hybryda, korepetycje online i krótkie zlecenia da się wpiąć obok głównej pracy. Da się też wpaść w ogłoszenie, które brzmi jak praca, a jest prośbą o wpłatę. To nie jest ten sam rynek.</p>
<h2>Druga praca bywa też próbą zawodu</h2><p>Kilka miesięcy w innej roli, portfolio albo powrót po przerwie. Niskie ryzyko dotyczy kalendarza tylko wtedy, gdy główna umowa pozwala dorabiać.</p>
<h2>Co ustalić, zanim powiesz tak</h2><ul><li>Ile godzin tygodniowo możesz przeznaczyć, licząc dojazd.</li><li>Jaka to umowa i co z ZUS oraz PIT. Student na zleceniu i pracownik na etacie w tym samym wieku nie są w tym samym układzie.</li><li>Czy w głównej umowie jest zakaz konkurencji albo obowiązek zgody.</li></ul>
<p>Drogi są porównane w <a href="dorabianie.html">zestawieniu dorabiania</a>.</p>''')

article("artykul-trend-zdalna.html","Praca zdalna i hybryda po nowelizacji Kodeksu pracy","Jak praca zdalna, hybryda i 24 dni okazjonalne wyglądają w polskich przepisach.","Branże",f'''
<p class="lede">Praca z domu przeszła z przywileju „dla wybranych zespołów” do rozmowy, którą da się oprzeć na Kodeksie pracy. Rozmowa nadal nie jest zgodą.</p>
{stats([("24 dni","tyle najwyżej trwa okazjonalna praca zdalna w roku kalendarzowym"),("Wniosek","okazjonalnie składa go pracownik, nie pracodawca"),("Odmowa","jest możliwa. Przy części osób pracodawca podaje przyczynę")])}
<h2>Dwie różne rzeczy</h2><p>Stała praca zdalna albo hybryda wynika z umowy, regulaminu albo porozumienia. Jest tam miejsce pracy, sposób kontaktu i zwykle sprzęt albo ryczałt na koszty. Okazjonalna praca zdalna to osobny, krótszy tryb: do 24 dni w roku, na twój wniosek, w papierze albo elektronicznie. Niewykorzystane dni nie przechodzą na kolejny rok.</p>
<h2>Czego wniosek nie załatwia</h2><p>Pracodawca może nie wyrazić zgody na dni okazjonalne. Przy pracy zdalnej uzgadnianej na dłużej część pracowników, między innymi w ciąży oraz opiekujących się małym dzieckiem, ma mocniejszą pozycję: odmowa jest wtedy związana z rodzajem albo organizacją pracy i powinna mieć przyczynę. Aktualny katalog osób i terminy odpowiedzi sprawdź w Kodeksie pracy albo zapytaj w PIP. Nie obiecujemy, że wniosek przejdzie.</p>
<h2>Jak to wygląda w ogłoszeniach</h2><p>„Home office”, „2 dni w biurze” i „100% zdalnie” bywają trzema różnymi grafikami. Dopytaj, które dni są w biurze i czy biuro jest w twoim mieście. Rola w centrum usług w Krakowie z dwoma dniami w biurze nie jest pracą z dowolnego miejsca w Polsce.</p>
<p>Gotowy tekst wniosku jest w poradniku <a href="artykul-wniosek.html">krok po kroku</a>.</p>''')

article("artykul-szkolenia.html","Szkolenia, które da się połączyć z pracą","KFS, urząd pracy i baza usług rozwojowych: jak wybrać kurs pod ogłoszenie, którego naprawdę szukasz.","Szkolenia",f'''
<p class="lede">Szkolenie otwiera drogę tylko wtedy, gdy umiesz wskazać ogłoszenia, w których ta umiejętność już stoi. Sam dyplom z reklamy kursu pracy nie załatwia.</p>
{stats([("Ogłoszenie","najpierw rola, potem kurs pod luki"),("KFS","wniosek składa pracodawca do powiatowego urzędu pracy"),("Bez obietnicy","kurs nie gwarantuje zatrudnienia ani stawki")])}
<h2>Zacznij od roli</h2><p>Wybierz dwa albo trzy ogłoszenia, które naprawdę byś wysłał. Wypisz umiejętności, których ci brakuje. Dopiero wtedy szukaj kursu. Inaczej łatwo zapłacić za program, który dobrze wygląda w poście, a w wymaganiach go nie ma.</p>
<h2>Skąd biorą się pieniądze na kurs</h2><p>Krajowy Fundusz Szkoleniowy to droga przez pracodawcę i powiatowy urząd pracy, nie przez przypadkowy formularz z internetu. Osoba zarejestrowana jako bezrobotna albo poszukująca pracy pyta o szkolenie w swoim urzędzie. Baza Usług Rozwojowych zbiera usługi, przy których bywa dofinansowanie dla pracowników firm. Procenty i limity się zmieniają. Sprawdź je w urzędzie albo na stronie bazy, zanim zapłacisz.</p>
<h2>Wieczory i niepełny etat</h2><p>Część kursów jest modułami, online albo po 17:00. To pasuje do osób, które już pracują. Sprawdź, czy zjazd wpada w twoją zmianę.</p>
<h2>Czego nie rób</h2><ul><li>Nie płać za „gwarancję pracy” albo „gwarantowane 10 tys. na rękę po kursie”.</li><li>Nie wysyłaj skanu dowodu firmie, której nie umiesz znaleźć w KRS albo CEIDG.</li></ul>
<p>Po przerwie zajrzyj też do tekstu <a href="artykul-powrot.html">o powrocie do pracy</a>.</p>''')

article("artykul-dane-rynku.html","Jak czytać dane o rynku pracy","Bezrobocie rejestrowane, badanie aktywności, wolne miejsca i płace: co naprawdę mierzą polskie statystyki.","Kariera",f'''
<p class="lede">Nagłówek „bezrobocie spadło” mieści w sobie kilka różnych liczb. Tu jest, co która mierzy, zanim ułożysz sobie z niej plan.</p>
{stats([("Rejestr","osoby zarejestrowane w urzędach pracy"),("Aktywność","badanie aktywności ekonomicznej, inna definicja niż rejestr"),("Barometr","deficyt, równowaga albo nadwyżka w zawodzie")])}
<h2>Dwie stopy bezrobocia</h2><p>Stopa bezrobocia rejestrowanego liczy osoby wpisane w urzędach pracy. Badanie aktywności ekonomicznej (BAEL) pyta reprezentację ludzi, czy pracują albo szukają pracy, i nie pokrywa się z rejestrem. Jedna liczba może iść w dół, gdy w twoim zawodzie nic się nie ruszyło.</p>
<h2>Wolne miejsca i ogłoszenia</h2><p>Liczba ofert na portalu nie jest liczbą miejsc z urzędu. Ogłoszenie bywa w kilku serwisach naraz i zostaje po zamknięciu rekrutacji. Do obrazu branży lepszy jest Barometr Zawodów: mówi, czy w twoim województwie zawód jest deficytowy, w równowadze czy w nadwyżce.</p>
<h2>Płace</h2><p>GUS podaje przeciętne wynagrodzenie i rozkłady, nie stawkę z twojego ogłoszenia. Środek rozkładu nie jest obietnicą. „Do 12 tys. brutto” w ogłoszeniu jest sufitem widełek.</p>
<h2>Prosty rytuał</h2><ul><li>Sprawdź ostatni komunikat GUS o wynagrodzeniach albo bezrobociu, zależnie od pytania.</li><li>Otwórz Barometr na swoje województwo i zawód.</li><li>Porównaj to z trzema aktualnymi ogłoszeniami, nie z jednym.</li></ul>
<p>Branże opisujemy osobno w tekście <a href="artykul-branze.html">o tym, gdzie przybywa pracy</a>.</p>''')
