#!/usr/bin/env bash

set -e

sudo apt-get install python-pip python-dev python-openssl -y

sudo pip install -r requirements.txt

cd lib
if [ ! -d Adafruit_Python_DHT ]; then
  git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  cd Adafruit_Python_DHT
  sudo python setup.py install
  cd -
fi
cd -
