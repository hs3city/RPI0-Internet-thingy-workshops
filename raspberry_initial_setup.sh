#!/bin/bash
set -e
set -u
set -x
#
# basic apps and libraries
#
sudo apt-get -y install htop mc atool git tig python-pip python-dev python-pip libfreetype6-dev libjpeg-dev
sudo pip install ptpython
sudo -i pip install --upgrade pip setuptools
sudo apt-get -y purge python-pip
sudo -H pip install --upgrade luma.led_matrix
#
# ustawienia gpio
#
sudo usermod -a -G spi,gpio pi
echo 
read -n 1 -p $'Teraz zostanie uruchomiony konfigurator raspberry pi. \n1. Recznie musisz wlaczyc interfejs SPI ("5 Interfacing options" -> "SPI" -> "Would you like the SPI interface to be enabled?" -> "yes" -> "ok" -> "finish").\n2. Zmien nazwe hosta\n3. uruchom ssh\n4. Na koncu potwierdz restart urzadzenia.'
sudo raspi-config
sudo reboot
