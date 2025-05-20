#!/usr/bin/python                            # Didi Lamken    10.05.2025
programmname = "d-DauerUpload.py"

import datetime
import time
from   time import *
#from   datetime import datetime

Stundemin  =    5         # Bilder    ab   x Uhr        mit IR-Licht     
Stundemax  =   22         # Bilder    bis  x Uhr 
mindif     =   15         # ein Bild  alle x min  machen   
PhotoMin   =  "00"        # Bild zu Minute x mit        gelben Licht
       
CountMax     =   20       # Anzahl der Durchläufe

sleeptime1 =    1         # sec warten
sleeptime2 =   10         # sec warten

import os 
import sys

DefKamera   = "BOBCamXX"                                                    #### Parameter
Directory   = "./a-recorded/" 
DefModus    = "NonInvers"
DefCountMax = 2
density     = 100   
try:                                                                       
    Kamera = sys.argv[1]
except:
    Kamera = DefKamera
print("   Kamera:   ", Kamera )
try:
    Modus = sys.argv[2]
except:
    Modus = DefModus
print("   Modus:    ", Modus )
try:
    CountMax = int(sys.argv[3])
except:
    CountMax = DefCountMax
print("   CountMax:    ", CountMax )

# Definitionen für Neopixel-Led an Pin 21                                   ####  Neopixel
import board
pixel_pin  = board.D21
import neopixel
num_pixels = 10             # The number of NeoPixels
ORDER      = neopixel.GRB   # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
pixels     = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
print("   Neopixel: ", num_pixels, "Led an Pin:", pixel_pin, "mit Order:", ORDER )

# Definitionen für IR-Led an Pin 25                                          ####  IR-Led
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LedIR = 25   
GPIO.setup(LedIR, GPIO.OUT, initial= GPIO.LOW)
if ( Modus == "Invers" ) : 
    print("   Invers     IR-Led aus ")
    GPIO.output(LedIR,GPIO.HIGH)         # aus  bei Invers
if ( Modus == "NonInvers" ) : 
    print("   NonInvers  IR-Led aus ")
    GPIO.output(LedIR,GPIO.LOW)          # aus

# Definition der Start- und Stoppzeit
starttime = datetime.time(Stundemin, 0)  #  
stopptime = datetime.time(Stundemax, 0)  #  

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")
for i in range(CountMax): 
    # Datum und Uhrzeit erfassen                                                 #### Uhrzeit
    lt = localtime()
    Datum     = strftime("%d.%m.%Y", lt)
    Uhrzeit   = strftime("%H:%M:%S", lt)
    Timestamp = strftime("%Y%m%d-%H%M%S", lt)
    Minute    = strftime("%M", lt)
    Sekunde   = strftime("%S", lt)

    # zu jeder Minute x ein Photo mit gelben Licht
    print("   jetzt  ist Minute = ", Minute, "  -> Photo mit Gelblicht bei Minute", PhotoMin )
    if ( Minute == PhotoMin ):
        print("   Minute    ", Minute, "    = ", PhotoMin, "  -> Photo mit Gelblicht" )
        ####   Ge-Photo machen   Ende
        print("   Photo mit  Gelblicht am  ", Datum, "um", Uhrzeit, "Uhr mit Timestamp:", Timestamp )
        Photoshell = "sudo python c-GePhotoUpload.py " + Kamera + " " + Modus
        os.system(Photoshell)
        ####   Ge-Photo machen   Ende

    # zwischen starttime und stopptime Photo mit IR-Licht machen
    now = datetime.datetime.now().time()
    if ( starttime <= now <= stopptime ):
        print(" ")
        print("   Zeit zwischen", starttime, "und", stopptime, " -> Photo machen" )
        ####   IR-Photo machen   Anfang
##      print("   Photo mit Ir-Licht am  ", Datum, "um", Uhrzeit, "Uhr mit Timestamp:", Timestamp )
##      Photoshell = "sudo python b-TiPhotoUpload.py " + Kamera + " " + Modus
        print("   Photo mit Ir-Licht am  ", Datum, "um", Uhrzeit, "Uhr " )
        Photoshell = "sudo python a-IrPhotoUpload.py " + Kamera + " " + Modus
        os.system(Photoshell)
        ####   IR-Photo machen   Ende
    else:
        print(" ")
        print( "    Zeit ausserhalb", starttime, "und", stopptime, "  -> kein Photo machen" )
        print( i, ". jetzt ", sleeptime2, " sec warten ..." )
        sleep(sleeptime2)  

    # Warten auf nächsten Durchgang mit mindif
    lt = localtime()
    minanf = int(strftime("%M", lt))
    print("   warten ab  Minute = ", minanf, " min")
    minend = minanf - (minanf % mindif)     # modulo
    minend = minend + mindif
    if ( minend >= 60 ):
        minend = minend - 60
    print("   warten bis Minute = ", minend, " min")
    if ( minend > 0 ):
        while ( minanf < minend ):
            lt = localtime()
            minanf = int(strftime("%M", lt))
            sleep(sleeptime1) 
    if ( minend == 0 ):
        while ( minanf > minend ):
            lt = localtime()
            minanf = int(strftime("%M", lt))
            sleep(sleeptime1) 
