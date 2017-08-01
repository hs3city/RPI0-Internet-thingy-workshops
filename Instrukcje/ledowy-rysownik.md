Warsztaty z wichajstrów internetowych
================
Ledowy rysownik internetowy
----------------

Wieloosobowa gra internetowa polegająca na rysowaniu dowolnych, wybranych przez użytkownika wzorów. Przestrzeń jest ograniczona, rysować można tylko z określoną prędkością, a tego inni chcą narysować co innego, niektórzy to poprostu trolle, a co najgorsze, nie wszyscy muszą grać uczciwie!

---

Cel
----------------
Celem warsztatu jest wykorzystanie modułu macierzy led 8x16 pikseli oraz malinki do stworzenia gry internetowej w kótrej:
1. każdy, kto odwiedzi stronę malinki może zapalić albo zgasić jeden piksel
2. Przed zapaleniem/zgaszeniem każdego następnego piksela trzeba odczekać 10 sekund (no chyba że jesteś hackerem)

Opis matrycy LED oraz podłączenie
----------------

Wykorzystana matryca LED to gotowy moduł zaprojektowany specjalnie z myślą o raspberry pi. Zawiera dwie macierze 8x8 led. sterowane przez interfejs SPI (możesz olać tą informację) za pośrednictwem dwóch stwrowników led MAX7219 (ta informacja też nie jest dla Ciebie zbyt ważna).

Matryce led do raspberry pi podłącza się do 4-sto pinowego GPIO, zaczynając od pinu 1 (w pobliżu gnizda miniHDMI).

Do wykorzystania wyświetlacza na malince konieczna jest biblioteka Luma.LED_Matrix na licencji MIT, która jest preinstalowana na warsztatowych urządzeniach.

Programowanie matrycy
----------------

Jako że warsztaty mają być szybkie, zaczniemy nieco oszukując.

1. (60 s) Z folderu `/home/mroz/RPI0-Internet-thingy-workshops/LedowyRysownik` przekopiuj foldery `static` oraz `template` do naszego projektu - `/home/mroz/RPI0-Internet-thingy-workshops/FlaskPrzyklad`. Nadpisz istniejące pliki. Pliki te zawierają aplikację kliencką - czyli stronę internetową kontrolkami użytkownika. Nie musisz się nimi przejmować, technologie internetowe nie są tematem tych warsztatów.
2. (30 s) przekopiuj poniższy szkielet aplikacji do swojego pliku `flask_przyklad.py` tuż przed instrukcją `if __name__=='__main__':` :

```python
matrix_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
]

#
# Kod odpowiedzialny za obsluge wyswietlacza
#

#
# lista bibliotek koniecznych do obslugi wyswietlacza
#
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

def init_led_matrix():
    """
    Funkcja odpowiedzialna za inicjalizacje wyswietlacza
    """
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=2, block_orientation=90)
    return device

device = init_led_matrix()


@app.route("/", methods=['POST'])
def update_matrix():
    """
    Uchwyt odpowiedzialny za pobieranie informacji od uzytkownika - ktory
    pixel zapalic/zgasic
    """
    global matrix_state
    #
    # Zaloguj co tam nam uzytkownik przeslal
    #
    app.logger.info(str(request.get_data()))

    #
    # Tutaj wstaw kod odpowiedzialyza pobieranie danych JSON od użytkownika oraz zmianę stanu zadanego piksela (zajrzyj
    #


    #
    # odswierz obraz na wyswietlaczu
    #
    with canvas(device) as draw:
        for x in range(16):
            for y in range(8):
                draw.point((x, y), matrix_state[y][x])
    return "OK"

@app.route("/matrix_state.json")
def matrix_state_handler():
    """
    Uchwyt zwracajacy aktualny stan macierzy led pod postacia dwuwymiarowej
    tablicy 16 x 8 zrzuconej do formatu json.
    :return:
    """
    global matrix_state
    #
    # tutaj wstaw kod odpowiedzialny za zwracania użytkonikowi swo
    #
```
4. (120 s) We wklejonym kodzie, wewnątrz funkcji `matrix_state_handler` dodaj kod odpowiedzialny za zwracanie użytkownikowi tablicy `matrix_state` pod postacią plik JSON (flask ściągawka). Wgraj zmiany, wejdź pod adres `http://<nazwa malinki>.local/matrix_state.json` i sprawdź czy działa.
5. (600 s) We wklejonym fragmencie kodu, wewnątrz funkcji `update_matrix` wstaw kod odpowiedzialny za pobieranie przesłango przez użytkonika dokumentu JSON. Plik ten zwiera tablicę o następującej postaci: `[ <x>, <y>, <wartosc>]`, gdzie `<x>,<y>` to współrzędne piksela, zas `<wartość>` to żądana docelowa wartość piksela -czyli albo 0, albo 255. Zajrzyj do ściągawki flask. Wgraj nowy kod na malinkę, wejdź na adres `http://<nazwa malinki>.local/` i sprawdź - możesz zapalać i gasić piksele?

Viola! Podaj adres malinki innej grupie i rozpocznij walkę! Narysuj serduszko, a oni niech zrobią napis'HS'. Kto wygrał?


