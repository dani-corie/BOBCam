#!/bin/bash
 
KAMERA="test"
DATE=$(date +"%Y%m%d-%H%M%S") 
rpicam-still -t 1000 -n \
             -o $KAMERA-$DATE.jpg \
            --hdr auto \
            --autofocus-mode manual --lens-position 3.2 \
            --width 1500