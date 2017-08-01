#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Pierwsza linijka jest malo wazna - to poprostu informacja dla systemu
# operacyjnego, ze mamy do czynienia z programem, ktory powinien byc wykonywany
# za pomoca interpretera python.
#
# Druga linijka to informacja o kodowaniu znakow - narazie udajmy ze wiemy o
# co chodzi.
#
# zaimportuj niezbedne biblioteki flask - czyli odpowiedzialne za serwowanie
# uzytkownikowi strony internetowej
#
from flask import Flask, request, send_from_directory
import json
#
# Stworz obiekt aplikacji
#
app = Flask(__name__)

@app.route('/')
def hello():
  """Przykladowy uchwyt - serwuje powitanie, gdy uzytkownik odwiedzi adres malinki""""
  return "Hello world"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
