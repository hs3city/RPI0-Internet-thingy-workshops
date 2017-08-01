Flask - moja pierwsza ściągawka
================
Flask jest frameworkiem w python służącym do tworzenia aplikacji internetowych. Sam z siebie nie narzuca żadnej struktury programu (z drobnymi wyjątkami), sam z siebie zapewnia tylko podstawową funkcjonalność, która w razie potrzebymoże być uzupełniana za pomocą zewnętrznych wtyczek - np. dla baz danych, enkoderów, dekoderów itd.

Witaj świecie
----------------
Stwórz plik 'hello.py'

```python
from flask import Flask, request, send_from_directory
import json

#
# Stworz obiekt aplikacji
#
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello world"

if __name__ == '__main__':
#
# uruchom aplikacje
#
  app.run(host='0.0.0.0', port=5000, debug=True)
```

taki program można uruchomić w trybie developerskim za pomocą polecenia:

```bash
$ python ./flask_przyklad.py
```

Serwowanie plików statycznych (grafiki itp.)
----------------
Jeśli w projekcie mamy folder 'static' to pliki z tego folderu można udostępnić w następujący sposób:

```python
@app.route('/static/<path:path>')
def static_handler(path):
    """
    Uchwyt serwujacy uzytkownikowi pliki statyczne z folderu 'statitc'
    :param path: nazwa pliku
    :return: zawartosc pliku
    """
    return send_from_directory('static', path)
```

Pliki te będą dostępne pod adresem "http://<nazwa malinki>.local/static/jakis_plik.jpg

Serwowanie favicon -ikonki wyświetlanej w pasku adresu przeglądarki
----------------
Zakładając że w projekcie znajduje się folder 'static' zawierający plik 'favicon.ico'

```python
@app.route('/favicon.ico')
def favicon():
    """Uchwyt serwuje favicon = czyli mala grafike wyswietlana na pasku
    przgladarki"""
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
```

Przyjmowanie zapytań POST z JSON
----------------
Zakładając że użytkownik wyśle dokument JSON `{"pole1":"wartosc1", "pole2":3}`

```python
from flask import request

@app.route("/akcja", methods=['POST'])
def update_matrix():
    # Zaloguj co tam nam uzytkownik przeslal
    app.logger.info(str(request.get_data()))
    data = request.get_json(force=True)
    pole1 = data['pole1']
    pole2 = data['pole2']
    return """{"status":"OK"}"""

```

zmienne `pole1`, `pole2` będą teraz zawierać odpowiednie wartości z dokumentu JSON.


