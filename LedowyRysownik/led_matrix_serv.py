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

@app.route("/", methods=['GET'])
def hello():
    """
    Glowny uchwyt serwujacy wlasciwa strone
    """
    return send_from_directory('templates', 'index.html')

@app.route("/", methods=['POST'])
def update_matrix():
    """
    Uchwyt odpowiedzialny za pobieranie informacji od uzytkownika - ktory 
    pixel zapalic/zgasic
    """
    #
    # Zaloguj co tam nam uzytkownik przeslal
    #
    app.logger.info(str(request.get_data()))
    #
    # pobierz i rozpakuj dane od uzytkownika - czyli wspolrzedne punktu oraz
    # oczekiwana wartosc (0/255)
    #
    data = request.get_json(force=True)
    x, y, value = data
    #
    # Dla pewnosci
    #
    if value != 0:
        value = 255
    #
    # zaktualizuj stan wyswietlacza
    #
    matrix_state[y][x] = value

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
    return json.dumps(matrix_state)


@app.route('/static/<path:path>')
def static_handler(path):
    """
    Uchwyt serwujacy uzytkownikowi pliki statyczne z folderu 'statitc'
    :param path: nazwa pliku
    :return: zawartosc pliku
    """
    return send_from_directory('static', path)


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