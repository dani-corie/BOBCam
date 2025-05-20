#!/bin/bash
    
KAMERA="BOBCam10"  
#MODUS="Invers"
MODUS="NonInvers"

cd /home/pi/BOBCamXX/

echo " "
echo "Ein Photo machen mit IR-Licht"
sudo python ./a-IrPhotoUpload.py $KAMERA $MODUS

