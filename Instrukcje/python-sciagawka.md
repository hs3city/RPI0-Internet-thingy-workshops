Moja pierwsza sciągawka z python
================

Python - wysokopoziomowy język programowania potokowego (szeregowego).

Program hello world:
----------------

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("witaj świecie!")
```

Dwie pierwsze linijki nie są konieczne, ale warto je umieścić na początku każdego pliku.

Absolutne podstawy
----------------


| Polecenie                         | opis                                                      | wynik dzialania na ekranie konsoli           |
| :-------------------------------- |:---------------------------------------------------------:|---------------------------------------------:|
| print(<wartość>)                  | wydrukuj na ekranie <wartość>                             | <wartość>                                    |
| x=<wartość>                       | zapisz do zmiennej x wartosc <wartość>                    | BRAK                                         |
| x="tekst"                         | zapisz do zmiennej x ciąg znaków "telkst "                | BRAK                                         |
| y=x+1                             | dodaj 1 do zmiennej x a wynik zapisz w zmiennej x         | BRAK                                         |
| foo()                             | wywołaj funkcję foo                                       | ZALEŻY OD FUNKCJI FOO                        |
| foo(<wartość>, <wartość> , <...>) | wywołaj funkcję foo z zadanymi argumentami                | ZALEŻY OD FUNKCJI FOO                        |
| foo() + bar(<wartość>)            | dodaj do siebie wartości zwracane przez funkcje foo i bar | ZALEŻY OD FUNKCJI FOO i BAR                  |


`<wartość>` - Jest to dowolne wyrażenie zwracające jakąś wartość - może to być jawnie wpisana wartosć stała (patrz niżej) lub wywołanie funkcji.

Przykłady wartości:
1. Numeryczne całkowite: `1`, `-41`, `0xdeadbeef`
2. Numeryczne zmiennoprzecinkowe: `1.0`, `-4.2`, `+321234.222222`, `12e22`
3. Ciągi znaków (tekst): `'jakiś tekst w apostrofach'`, `"jakis tekst w cudzyslowiu"`, `"""Jakis tekst intepretowany w specjalny sposób"""`

Logika
----------------

### Wartości logiczne
Python definiuje dwie podstawowe wartości logiczne: `True`, `False`.

Wartości równoważne logicznemu fałszowi `None`, `0`, `[]` (pusta lista), `{}` (pusty słownik) itd.
Wartości równoważne logicznej prawdzie: `1`, `"dowolny niepusty ciąg znaków"`, `['dowolna', 'niepusta', 'lista']`, `{'dowolny':'niepusty słownik'}`

### Instrukcje sterujące
Jest to zestaw instrukcji, które w zależności od logicznej wartości <warunek> wykonują, lub nie <operację>

#### Jeżeli (if, elif, else)

Instukcja sprawdza <warunek>, jeśli warunek zwraca wartość logiczną `True` wykonuje <operacje> w przeciwnym wypadku przechodzi do następnej opcjonalnej sekcji `elif`, sprawdza <warunekN> i w zależności od wartości warunku wykonuje <operacjeN> albo przechodzi dalej. W końcu, jeśli wszystkie warunki były fałszywe zostaje wyknany blok `else`.

```python
if <warunek>:
  <operacje>
elif <warunek2>:
  <operacje>
elif <warunek3>:
  <operacje>
elif <warunket4>:
  <peracje4>
else:
  <operacje5>
```

#### Pętla (while)

```python
while <warunek>:
  <operacje>
```
Instukcja powoduje cykliczne wykonywanie `<operacje>` za każdym razem sprawdzając czy `<warunek>` zwraca wartość `True`. W momencie, w którym warunek przestaje zwracać logiczną prawdę, pętla się kończy.

#### Iteracje (for)
<sekwencja> - pewna instrukcja zwracająca sekwencję - np. lista `[]`, słownik, ciąg znaków, a najczęściej `range(<from>,[<to>[, <step>]])` np. `range(10)`, `range(1,100,2)` - czyli odpowiednio: liczby całkowite od 0 do 9 włącznie, liczby parzyste od 1 do 99;

```python
for X in <sekwencja>:
  <instukcje>

```

czyli np (wydrukuje liczby całkowite od 0 do 9 włącznie

```python
for x in range(10):
  print(x)
```

Funkcje
----------------
Funkcja to blok instrukcji posiadający swoją nazwę, który może przyjmować argumenty, operować na nich i zwracać jakąś wartość.

```python
def <nazwa>( <argumenty> ):
  <operacje>
  return <wartość>
```

Czyli np. (wypisze w konsoli 4.5):

```python
def dodaj(x, y):
  z = x+y
  return z

print( dodaj(1, 3.5) )
```

Zmienne globalne
----------------
W normalnych warunkach zmienne zdefiniowane po za funkcją, są w niej niedostępne. Aby obejść ten problem, w ciele funkcji można umieścić instrukcję `global <nazwa zmiennej>`:

```python
licznik=0

def zwieksz_licznik():
  global licznik
  licznik+=1
  print("licznik zwiekszony, stan:" + str(licznik))
```

Zewnętrzne biblioteki
----------------
Importowanie zewnętrznych bibliotek

```python
import <biblioteka>
import <biblioteka>.<moduł>
from <biblioteka> import <moduł>
import <biblioteka> as <nowa nazwa>
```

Czyli np.

```python
from flask import Flask
app = Flask(__name__)
```

```python
import os.path
print(os.path.dirname('/home/pi/wihajstry')
```

```python
from glob import glob
print(glob("*.py"))
```

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
```

Przydatne biblioteki
----------------
1. time : zawiera funkcje takie jak `time` - zwraca aktualny czas w sekundach od "unix epoch" oraz `sleep`, która usypia program na zadaną liczbę sekund

Dekoratory
----------------
Na potrzeby tych laboratoriów nie wyjaśnimy czym są dekoratory. W uproszczeniu przyjmijmy że jest to forma dołączania do funkcji pewnej funkcjonalności.

```python

@<dekorator>( <argumenty dekoratora> )
def <nazwa funkcji>( <argumenty funkcji> ):
  <instrukcje>
```

Czyli np. (z dokumentacji Flask):

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```



