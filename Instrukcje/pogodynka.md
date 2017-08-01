Warsztaty z wichajstrów internetowych
================
Pogodynka
----------------

Monitor temperatury oraz wilgotności (internetowy)

Autor: mroz

---

Cel
----------------
Celem warsztatu jest stworzenie stacji monitorującej temperaturę i wilgotność otoczenia oraz prezentującej wynik na cyklicznie aktualizowanej stronie.

Sprzęt i biblioteki
----------------

Do realizacji projektu wykorzystamy moduł DHT11 - scalony czujnik temperatury oraz wilgotności względnej powietrza. Oraz biblioteki "DHT11 Python library" udostępnianej n licencji MIT pod adresem [github.com/szazo/DHT11_Python](https://github.com/szazo/DHT11_Python).

Podłączenie czujnika
----------------

Czujnik może zostać podłączony bezpośrednio do raspberry pi - wymaga podłączenia trzech pinów - Sygnału, masy i zasilania, które należy podłączyć do odpowiednio: pinów GPIO18, Ground, 5V.

Wyprowadzenia Raspberry pi:
![Raspberry pi pinout](pi3-gpio.png)

Kod przykładowy do obsługi DHT11
----------------

Inicjalizacja modułu:

```python
import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin = 14)
```


Pomiar
```python
# read data using pin 14
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

Zadania
----------------

1. (40 s) przekopiuj zawartość folderu `/home/hs/RPI0-Internet-thingy-workshops/Pogodynka` do folderu projektu `/home/hs/RPI0-Internet-thingy-workshops/FlaskPrzyklad`. Potwierdź nadpisanie plików.
2. (60 s) do swojego pliku skopiuj poniższy kod:

```python

def read_dht():
  #
  # Tutaj wstaw kod odpowiedzialny za inicjalizację oraz pobieranie pomiaru z DHT
  #

  #
  #
  #
  return {
    "temperature": 1,
    "humidity: 1
  }


@app.route('/measurement.json')
def get_measurement():
  measurement = read_dht11()
  #
  # Podmień poniższą linijkę w taki sposób, aby zwracała zmienną measuremet pod postacią dokumentu JSON
  #
  return XXX

```
3. (120 s) zmodyfikuj linijkę `return XXX` wewnątrz funkcji `get_measurement` tak aby zwracała on dokument JSON (patrz do ściągawki flask). Wciśnij 'F5' i odwiedź adres `http://<nazwa malinki>/measurement.json`. Czy pojawiają się domyślne temperatura i wilgotność 1;1 ? .
4. (600 s) kożystając z przykładowego kodu do obsługi DHT uzupełnij funkcję `read_dht` w taki sposób, aby inicjalizowała ona moduł DHT11, dokonywała pomiaru i zamiast jedynek zwracała wyniki pomiarów. Wgraj kod na malinkę i odwiedź ponownie adres `http://<nazwa malinki>/measurement.json`. Działa?

Niestety biblioteka do obsłygi czujnika DHT11 jest napisana w pythonie, przez co nie jest idealna - czasami pomiar się nie uda.

Jeśli wszystko działa, odwiedź adres `http://<nazwa malinki>/`. Działa? Potestuj działanie układu - pochuchaj na czujnik, wystaw na słońce.


Informacja zwrotna
----------------
Jak wrażenia? Daj znać prowadzącemu co myślisz o tych warsztatach? Co myślisz o formie, zakresie i w ogóle? Olej literówki i ortografię ;p

