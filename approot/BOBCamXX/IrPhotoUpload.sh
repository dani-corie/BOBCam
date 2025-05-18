#!/bin/bash
  
KAMERA="BOBCam03"  
#MODUS="Invers"
MODUS="NonInvers"

cd /home/pi/BOBCamXX/

echo " "
echo "Ein Photo machen mit IR-Licht"
sudo python ./1-NoNeoIrPhoto.py $KAMERA $MODUS

echo " "
echo "Upload auf NextCloud"
/home/pi/BOBCamXX/3-UploadJpg.sh

echo " "
echo "Photo ins Archiv verschieben"
/home/pi/BOBCamXX/4-CreateMove.sh
