Warsztaty z wichajstrów internetowych
================
Instrukcja wstępna - wstęp do python i flask.
----------------

---


Opis warsztatów (~10 min)
----------------
Celem warsztatu jest zapoznanie warsztatowicza z technologiami i narzędziami wykorzstywanymi często w szeroko rozumianym IOT (ang Internet of things) co na polski tłumaczy się jako "internetowe wichajstry". Mowa tutaj o:

1. Python - język programowania stworzony z myślą o łatwości nauki i wykorzystania
2. Raspberry PI 0 W - mini komputer typu SBC (Single Board Computer) będący częścią ekosystemu raspberry PI stworzony z myślą o edukacji
3. WiFi - muszę tłumaczyć?
4. Proste moduły elektroniczne , w tym serwomechanizm, cyfrowy termometr i wyświetlacz ledowy.
5. Flask - biblioteka programistyczna Python stworzona z myślą o szybkim i łatwym tworzeniu aplikacji internetowych.

Warsztat skład się z dwóch części - pierwszej, w której sztywno stosujemy się do instrukcji, a która ma dać podstawy do części drugiej, na której uczestnicy przy wsparciu prowadzącego samodzielnie realizują przykładowe projekty .

Na koniec warsztatów każdy uczestnik/grupa powinna zaprezentować w pełni sprawny wichajster internetowy kontrolowany przez internet za pośrednictwem przeglądarki internetowej.


---


Opis wykorzystywanych technologii oraz ważne linki (~10 min)
----------------
###Raspberry pi zero W
Strona producenta: [raspberrypi.org](https://www.raspberrypi.org)

Jest to mały komputer, oparty na procesorze w architekturze ARM (podobny do tego, który masz w telefonie) zaprojetkowany z zgodnie z dwoma głównymi założeniami:

1. Ma być tani
2. Ma być doskonałym narzędziem do edukacji

Biorąc pod uwagę, że koszt takiego komputera to 52 zł. plus przesyłka oraz karta pamięci oraz jego dużą popularność - możnaspokojnie założyc, że twórcy spełnili swoje założenia.

Komputer zawiera:

1. Kartę sieciową WiFi + BT 4.0
2. 512 MB ram
3. Procesor BCM2835 o taktowaniu 1 GHz
4. Port USB mogący służyć albo do podłączenia urządzeń zewnętrznych (np. pendrive_ albo do podłączenia do komputera (tak jak podłącza się telefon celem synchronizacji).
5. Gniazdo kart micro SD (karta pamięci jest konieczna do działania komputera)
6. Gniazdo mini HDMI do podłączenia monitora
7. 40-sto pinowe złącze GPIO - czyli zestaw pinów do których można podłączać zewnętrzne moduły elektroniczne - od prostej diodki i przycisku aż po skomplikowane kontrolery automatyki domowej.
8. Złącze kamery - pozwala na realizację projektów wizyjnych - system monitoringu, kamera internetowa, photobooth itd.

Przykładowe projekty znalezione w internetach:

1. [Portable Raspberry Pi Photo Booth](https://www.youtube.com/watch?v=SH1kTxJlQqI)
2. [Raspberry Pi Smart Mirror](https://www.youtube.com/watch?v=fkVBAcvbrjU)
3. [Pi Camera Doorbell with Notifications!](https://www.hackster.io/robin-cole/pi-camera-doorbell-with-notifications-408d3d)
4. [DIY Vintage Spotify Radio Using A Raspberry Pi](https://www.hackster.io/tinkernut/diy-vintage-spotify-radio-using-a-raspberry-pi-bc3322)
5. [Pi0drone](https://hackaday.io/project/9811-pi0drone)

####Jak zacząć zabawę z malinką?
Masz dwa wybory:

1. Przyjść na warsztaty, gdzie malinki oraz komputery są przygotowane do pracy
2. Skorzystać z materiałów edukacyjnych na stronie producent: [raspberrypi.org/help/](https://www.raspberrypi.org/help/)


###Python 2.7
Dokumentacja: [docs.python.org/2.7/](https://docs.python.org/2.7/)

Jest to język programowania wysokiego poziomu, stworzony z myślą o łatwości czytania i pisania kodu. W tych warsztatach wykorzystujemy starą wersję tego języka (2.7) ponieważ jest ona preinstalowana na raspbianie.

Przykład kodu:

```python
def heater_control(heater):
  if temperature < MIN_TEMPERATURE:
    heater.enable()
  elif temperature >= MAX_TEMPERATURE and heater.is_enabled():
    heater.disable()

heater = Heater()
while True:
  sleep(1)
```

Czy potrafisz przeczytać i zinterpretować powyższy kod python?

###Flask
Strona projektu: [flask.pocoo.org](http://flask.pocoo.org/)

Biblioteka do szybkiego tworzenia aplikacji internetowych - to znaczy aplikacji, które działają na serwerze i komunikują się z użytkownikiem za pośrednictwem strony internetowej.
Flask dąży do tego, aby w jak najmniejszym stpniu krępować programistę oraz maksymalnie uprościć proces tworzenia nowej aplikacji internetowej.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

Powyżej jest przykład minimalnej aplikacji we Flask pobrany prosto z dokumentacji.

W ramach przygotowanych warsztatów, wystarczy że wciśniesz `F5`, a prekonfigurowane środowisko programistyczne (IDE) uruchomi Twoją aplikację na malince.

Jeśli chcesz uruchomić aplikację ręcznie, to zajrzyj do ściągawki flask.

###Geany
Strona projektu: [geany.org/](https://www.geany.org/)

Jest to lekkie środowisko programistyczne obsługujące wiele różnych języków programowania. Jeśli chodzi o wsparcie dla Python jest "akceptowalne". W ramach warsztatów będziemy kożystać tego IDE ze względu na możliwość łątwej konfiguracji, lekkość programu, stabilność oraz licencję GNU GPL.

---

Instrukcja - pierwsze kroki z python (~20 min, przerwać!)
----------------

Zacznijmy szybko - krok po kroku będziemy tworzyć kod, który wydrukuje nam 10 razy "witaj świecie", lub nie w zależności od wartości parametru X.
1. (30 s) Uruchom Geany
2. (30 s) Stwórz nowy plik
3. (60 s) W ściągawce python znajdź i odpal program wypisujący "witaj świecie" w konsoli.
4. (20 s) Zapisz plik, wciśnij 'F5' aby uruchomić program
5. (300 s) Korzystając ze ściągawki python zmodyfikuj kod tak, aby wyświetlił słowa "witaj świecie" 10 razy (podpowieź: range)
6. (120 s) Kod stworzony w poprzednim punkcie zapakuj do funkcji o nazwie `moja_pierwsza_funkcja` i wywołaj tą funkcję - powinien działać w dokładnie ten sam sposób.
7. (120 s) Do kodu z poprzedniego punktu dodaj zmienną X o wartości `True`, zaś wywołaniefunkcji uzależnij od wartości zmiennej X (podpowiedź: JEŻELI). Nie zastanawiaj się - to zadanie jest naprawdę toporne)
8. (180 s) Warunek z punktu 8 zapaku do funkcji o nazwie `moja_druga_funkcja`, która przyjmuje X jako parametr wejściowy i wywołaj funkcję z wartością `True`. Uruchom program. Wyświetla "witaj świecie" 10 razy?
9. (120 s) A teraz wywołaj `moja_druga_funkcja` z parametrem `False`. Wyświetla "witaj świecie" 10 razy?

Instrukcja - pierwsze kroki z Flask (~30 min)
----------------

Stwożymy prostą aplikację internetową, która będzie zliczać liczbę kliknięć w przycisk na stronie. Wszystkie pliki statyczne, obrazki, dokumenty html, js, css są już umeszczone w folderach 'static' oraz 'templates'.

Aby uruchomić zmodyfikowany program najpierw zamknij okno terminala, które wyskoczyło poprzednim razem, a potem wciśnij klawisz 'F5', aby uruchomić aplikację jeszcze raz.

1. (20 s) Otwórz geany (zamknij wszystkie otwarte pliki)
2. (30 s) W geany wciśnij klawisze `ctrl + o`, pojawi się okno otwierania pliku, wybierz w nim `/home/hs/RPI0-Internet-thingy-workshops/FlaskPrzyklad/flask_przyklad.py`. Plik zawiera przykładowy szkielet aplikacji Flask.
3. (20 s) Wciśnij przycisk 'F5' - powinno pojawić się okienko konsoli informujące o uruchamianiu aplikacji zawierający mi. linijkę " * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)" otwórz przeglądarkę i odwiedź adres `http://localhost:5000/`. Czy widzisz "witaj świecie!"?
4. (120 s) Ze ściągawki skopiuj kod i wklej na końcu pliku kod odpowiedzialny za serwowanie plików statycznych oraz favicon. uruchom aplikację ponownie i odwiedź adres `http://localhost:5000/`. Czy widizsz różową malinkę w pasku przeglądarki?
5. (180 s) Dodaj zmienną o nazwie globalną `licznik` i wartości `0` (zerknij do python ściągawki). Zmienną zdefiniuj na początku pliku, bezpośrednio po instrukcjach `include`. Zmodyfikuj przykładowy kod tak, aby zwracał tekst "Witaj świecie po raz <licznik>", tak aby w miejscu <licznik> pojawiła się wartość zmiennej licznik. Działa?
6. (30 s) Zmodyfikuj kod tak, aby za każdym razem przed wyświetleniem tekstu zwiększał wartość zmiennej `licznik` o 1. Odśwież stronę kilka razy. Licznik się zwiększa?
7. (60 s) Zmodyfikuj kod tak, aby funkcja z poprzedniego punktu była dostępna pod adresem `/licznik` zamiast `/`. Sprawdź czy możesz wejść na `http://localhost:5000/`, a teraz sprawdź czy możesz wejść na adres `http://localhost:5000/licznik`.
8. (180 s) Ponownie skopiuj i wklej na końcu pliku kod odpowiedzialny za serwowanie favicon i zmodyfikuj go tak, aby serwował plik "index.html" z folderu "templates" (fragment kodu z mimetype usuń). Uruchom i odwieź `http://localhost:5000/` - czy pojawia się strona z przyciskiem?
9. (180 s) Zmodyfikuj kod funkcji z punktu 8. tak aby reagował na zapytania POST (patrz ściągawka flask). Wciśnij 'f5' i spróbuj przez przeglądarkę wejść na adres `http://localhost:5000/` - nie powinno działać. Teraz wejdź na `http://localhost:5000/` i wciśnij przycisk równocześnie przyglądając się okinku konsoli. Czy w konsoli wyświetliła się informacja o zapytaniu POST?
9. (300 s) Wciśnięcie przycisku powoduje wysłanie na serwer dokumentu JSON zawierającego informacje o przeglądarce oraz wartość o którą należy zwiększyć wartość licznika. Wysyłany dokument JSON ma postać `{"browser":"<informacje o przegladarce>","add": <x>}`, gdzie `x` to jakaś liczba. Odpowiedź serwera jest natychmiast wyświetlana w postaci okienka alert.
10. Wykorzystaj ściągawkę flask do przerobienia funkcj z punktu 9. w taki sposób, aby pobierała plik JSON, parsowała go i wartość `add` z tego pliku dodawała dp zmiennej licznik. Wgraj 'F5' i wejdź na `http://localhost:5000`,wciśnij przycisk kilka razy - czy licznik zwiększa swoją wartość?

Wgrywanie aplikacji na malinkę
----------------

Teraz, kiedy przećwiczyliśmy już podstawy python oraz flask na naszym komputerze lokalnym, czas przejść na programowanie malinki. Folder `FlaskPrzyklad` zawiera w sobie przykładowy projekt geany oraz skrypty konieczne do wysyłania plików na malinkę oraz ich zdalne uruchamianie.

1. (40 s) W geany w menu "Project" wybierz "open", w otwartym oknie wskaż ścieżkę "/home/hs/RPI0-Internet-thingy-workshops/FlaskPrzyklad/flask_przyklad.geany"
3. (60 s) W panelu po lewej, w zakładce "files" stronie Geany przejdź do tego samego folderu i otwórz plik "config.sh"
4. (120 s) Znajdź linijkę podobną do: `export PI_HOST="mroz3-pi0.local"` i zmień "mroz3-pi0" na nazwę malinki, którą dostałeś - powinna znajdowaćsie na naklejce na obudowie.
5. (60 s) Wciśnij 'F5' i poproś prowadzącego żeby sprawdził czy wszystko działa.
Wio la!

*Nie usuwaj plików i przejdź do instrukcji specyficznej dla Twojego wybranego projektu*
