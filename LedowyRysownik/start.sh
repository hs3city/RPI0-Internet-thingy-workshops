#!/bin/bash
#
# Skrypt uruchamiajacy nasz program w trybie debugowym.
#
export FLASK_APP=led_matrix_serv.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0