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
from flask import Flask, request, send_from_directory, url_for
import logging


#
# Stworz obiekt aplikacji
#
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    """
    Glowny uchwyt serwujacy wlasciwa strone
    """
    return send_from_directory('templates', 'index.html')

@app.route('/favicon.ico')
def favicon():
    """Uchwyt serwuje favicon = czyli mala grafike wyswietlana na pasku
    przgladarki"""
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/static/<path:path>')
def static_handler(path):
    """Uchwyt serwujacy uzytkownikowi pliki statyczne - np. grafiki z folderu
    'statitc'"""
    return send_from_directory('static', path)

# Fragment pliku odpowiedzialny za obsluge serwomechanizmu
#

@app.route('/plask')
def plask():
  """Uchwyt odpowiedzialny za sprzedawanie plaskacza!"""
  # prostu mechanizm upewniajacy sie ze w danym momencie tylko jedna osoba
  # kozysta z serwa
  global servo_is_working
  if servo_is_working:
    return "ERR"
  servo_is_working = True

  from time import sleep
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.OUT)
  servo = GPIO.PWM(18, 100)
  servo.start(5.0)
  # plaskacz!
  app.logger.info("plask start" + repr(servo))
  servo.ChangeDutyCycle(20.0)
  sleep(2)
  servo.ChangeDutyCycle(5.0)
  sleep(2)
  app.logger.info("plask stop")
  servo.stop()
  # skonczylismy, dajmy znac ze serwo jest wolne
  servo_is_working = False
  return "OK"

#
# Ta zmienna informuje czy
#
servo_is_working = False
