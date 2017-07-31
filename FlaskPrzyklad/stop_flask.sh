#!/bin/bash
#
# Konfiguracja srodowiska lokalnego tak, aby nie robilo glupich rzeczy
#
set -e
set -u
source ./config.sh
#
# zabij flaska - i zabij go na pewno!
#
echo "INFO|$(date)|Wylaczam poprzednie instancje programu"
ps_aux="$(ps aux)"
ps_aux="$(echo "$ps_aux" | fgrep -v `basename "$0"`)"
PIDS="$(echo "$ps_aux" | egrep "(python|flask)" | egrep -o "^[^ \t]+[\t ]+[0-9]+" | egrep -o [0-9]+)"
for pid in $PIDS
do
  if [ "$$" -ne "$pid" ] ;then
    echo "$PI_PASS" | sudo -S kill -2 "$pid"
  fi
done

for pid in $PIDS
do
  if [ "$$" -ne "$pid" ] ;then
    echo "INFO|$(date)|Czekam az proces $pid zostanie zamkniety"
    while [ -e /proc/$pid ] ;do
      sleep 0.1
    done
  fi
done
echo "INFO|$(date)|Wylaczono poprzednie instancje"
