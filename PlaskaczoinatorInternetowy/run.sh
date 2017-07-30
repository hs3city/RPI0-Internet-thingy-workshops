#!/bin/bash
#
# Konfiguracja srodowiska lokalnego tak, aby nie robilo glupich rzeczy
#
set -e
set -u
# wymagane sa zmienne srodowiskowe:
#   $PI_USER
#   $PI_PASS
#   $PI_HOST
#   $TARGET_FOLDER
#   $LOCAL_PROJECT_PATH
#
echo "INFO|$(date)|Wczytuje konfiguracje"
source ./config.sh
chmod +x ./*.sh
#
# Upewnij sie ze mamy dobry adres oraz ze pi jest dostepne w sieci
#

echo "INFO|$(date)|Sprawdzam czy docelowa malinka jest w sieci"
ping -c 1 -W 1 "$PI_HOST" || echo "ERROR|$(date)|Nie udalo sie odnalezc malinki"
#
# Zabij flaska i usun stare pliki
#

echo "INFO|$(date)|Czyszcze srodowisko docelowe"
sshpass -p "$PI_PASS" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r "$LOCAL_PROJECT_PATH"/config.sh "$PI_USER""@""$PI_HOST"":""$TARGET_FOLDER" > /dev/null
sshpass -p "$PI_PASS" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r "$LOCAL_PROJECT_PATH"/stop_flask.sh "$PI_USER""@""$PI_HOST"":""$TARGET_FOLDER" > /dev/null
sshpass -p "$PI_PASS" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$PI_USER""@""$PI_HOST"  'cd '"$TARGET_FOLDER"' && echo "'"$PI_PASS"'" | sudo -S ./stop_flask.sh || exit 0' > /dev/null
sshpass -p "$PI_PASS" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$PI_USER""@""$PI_HOST"  'echo "'"$PI_PASS"'" | sudo -S rm -rf '"$TARGET_FOLDER"' || exit 0' > /dev/null
sshpass -p "$PI_PASS" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$PI_USER""@""$PI_HOST"  'mkdir '"$TARGET_FOLDER"'' > /dev/null
#
# Wyslij pliki na serwer
#
echo "INFO|$(date)|Wysylam pliki do malinki"
sshpass -p "$PI_PASS" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r "$LOCAL_PROJECT_PATH" "$PI_USER""@""$PI_HOST"":""$TARGET_FOLDER" > /dev/null
sshpass -p "$PI_PASS" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$PI_USER""@""$PI_HOST" 'cd '"$TARGET_FOLDER"' && cd "$(ls)" && echo "'"$PI_PASS"'" | sudo -S chmod +x ./run_flask.sh' > /dev/null
#
# Uruchom aplikacje
#
echo "INFO|$(date)|Uruchamiam zdalna aplikacje"
sshpass -p "$PI_PASS" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$PI_USER""@""$PI_HOST" 'cd '"$TARGET_FOLDER"' && cd "$(ls)" && echo "'"$PI_PASS"'" | sudo -S ./run_flask.sh'

