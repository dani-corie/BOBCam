#!/bin/bash
    
# DauerPhotoUpload.sh
  
KAMERA="BOBCam10"  
#MODUS="Invers"
MODUS="NonInvers"

COUNTMAX=999

cd /home/pi/BOBCamXX/

echo " "
echo "Ein Photo machen mit IR-Licht und 1mal pro Stunde mit gelben Licht"
sudo python ./d-DauerUpload.py $KAMERA $MODUS $COUNTMAX

