#!/bin/bash

sudo apt-get -y install git atool geany git python-pip
sudo pip install flask
cd ~
mv ~/RPI0-Internet-thingy-workshops /tmp
git clone https://github.com/hs3city/RPI0-Internet-thingy-workshops.git
find -name "*.geany" -type f | xargs -I {} sed -i 's|base_path=/home/mroz/|base_path='"$HOME"'/|g' {}
echo "INFO|$(date)| Inicjalizacja srodowiska skonczon, uruchamiam geany"
geany&
