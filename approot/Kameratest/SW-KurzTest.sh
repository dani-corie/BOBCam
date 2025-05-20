#!/bin/bash   

echo " "
echo "IR-Licht ausschalten"
sudo python d-IrEinAus.py

echo " "
echo "Ein Photo machen ohne Licht"
sudo python a-EinPhoto.py

echo " "
echo "Neopixel-Licht testen"
sudo python b-NeoDens.py

