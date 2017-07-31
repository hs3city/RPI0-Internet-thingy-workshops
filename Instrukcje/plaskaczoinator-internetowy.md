Plaskaczoinator internetowy
================

Instrukcja do warsztatów
----------------


---

Wstęp
----------------

Celem warsztatu jest stworzenie urządzenia służącego do sprzedawania plaskaczy przez internet. Plaskacze będą dalej zwane "Bat slapami". Punktem wyjściowym projektu jest projekt wstępny stworzony na podstawie instrukcji ogólnej.

Plaskaczoinator składa się z czterech elementów:
1. Serwa z doczepioną ręką
2. Malinki
3. Aplikacji napisanej w Python z wykorzystaniem biblioteki flask
4. Strony internetowej, która jest przgotowana i przechowywana w folderach "static" oraz "templates" w folderze "PlaskaczoinatorInternetowy"

Obsługa serwomechanizmu w raspberry pi
----------------

Serwomechanizmy to układy elektromechaniczne składające się z silnika, kilku zębatek oraz pętli sprzężenia zwrotnego, spełniające jedno proste zadanie - w zależności od zadanego sygnału wychylają swój wał o x stopni.

Sygnałem sterującym jest sygnał PWM - czyli cykliczny sygnał prostokątny o sterowanym współczynniku wypełnienia (stosunek czasu w którym sygnał przyjmuje stan wysoki, do czasu w którym przyjmuje stan niski). Z naszego punktu widzenia jest ważne tylko to, że zwiększając współczynnik wypełnienia powodujemy że serwo wychyla się bardziej.

Stosunek wypełnienia sygnału sterującego serwami zazwyczaj oscyluje pomiędzy 5%, a 20% co odpowiednio powoduje wychylenie serwa na poziomie od 0 do 90 stopni.

Sposób podłączenia:
Serwo potrzebuje trzech przewodów:
1. Pomarańczowy - sygnał sterujący podłączany do GPIO raspberry pi za pośrednictwem rezystora 1 kOhm.
2. Czerwony - zasilanie 5 V
3. Brązowy - Masa "GND"

###Zadane 1
Wykorzystując rezystor, płytkę stykową oraz dodatkowe kable do płytki stykowej podłącz serwo do raspberry pi wykorzystując pin 18 (zapamiętaj ten numer)
[Opis wyprowadzeń Raspberry Pi](http://www.extremeelectronics.co.uk/wp-content/uploads/2015/12/pizeropinout.jpg)

###Obsługa serwo z poziomu python

Obsługę serwa trzeba zacząć od zaimportowania niezbędnych bibliotek oraz  inicjalizacji odpowiedniego pinu w trybie PWM:

```python
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 100)
```

Następnie trzeba wystartować serwo i ustawić je w pozycji zerowej (czyli ustawić współczynnik wypełnienia na 5%):

```python
servo.start(5.0)
```

Użytkowanie serwa polega na zadawaniu mu sygnału o odpowiednim współczynniku wypełnienia - np. żeby wychylić je o 90 stopni należy zadać sygnał PWM o wypełnieniu 20%:

```python
servo.ChangeDutyCycle(20.0)
```

Zaś żeby wrócić do pozycji początkowej należy zadać sygnał o współczynniku wypełnienia 5%:

```python
servo.ChangeDutyCycle(5.0)
```

Na koniec należy wyłączyć sygnał PWM sterujący serwem:

```python
  servo.stop()
```

###Zadanie 2


Przekopiuj poniższy kod na koniec swojego pliku:

```python
#
# Ta zmienna informuje czy
#
servo_is_working = False

@app.route('/plask')
def plask():
  """Uchwyt odpowiedzialny za sprzedawanie plaskacza!"""
  # prostu mechanizm upewniajacy sie ze w danym momencie tylko jedna osoba
  # kozysta z serwa
  global servo_is_working
  if servo_is_working:
    return "ERR"
  servo_is_working = True

  #
  # TUTAJ wstaw kod sterujący serwem - inicjalizację, plaskanie i wyłączenie sygnału sterującego
  #

  # skonczylismy, dajmy znac ze serwo jest wolne
  servo_is_working = False
  return "OK"


```

Jest to szablon funkcji, która wykorzystuje zmienną `servo_is_working` do upewnienia się że dwójka urzytkowników nie korzysta z serwa naraz. Nie jest to rozwiązanie idealne, ale działa.

sekcję `TUTAJ wstaw kod sterujący serwem` podmień kodem który:
1. Zainicjuje serwo (pamiętaj o odpowiednim pinie oraz pozycji początkowej)
2. Odczeka sekundę aż serwo się zainicjuje (patrz ściągawka python - czas)
3. wychyli się na maksa (sprzeda płaskiego)
4. odczeka sekunde aż płaski się sprzeda
5. Ustawi serwo w pozycji początkowej
6. Zwolni pin kontrolujący serwo

Do testowania postępów możesz wykorzystać przeglądarkę wchodząc na adres `http://<nazwa malinki>.local/plask` i obserwacje konsoli.

