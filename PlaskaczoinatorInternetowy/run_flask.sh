#!/bin/bash
#
# Konfiguracja srodowiska lokalnego tak, aby nie robilo glupich rzeczy
#
set -e
set -u
echo "--------------------------------------------------------------------------------"
echo "                            Uruchamnianie Aplikacji                             "
echo "--------------------------------------------------------------------------------"
export FLASK_APP=plaskaczoinator.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0 -p 80
