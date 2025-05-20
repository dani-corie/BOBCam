#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "gg-NeoPhotoTime.py"

import datetime
import time
from   time import *

sleeptime1 =  1         # sec warten
sleeptime2 = 10         # sec warten

Stundemin  =  8         # Bilder   ab   x Uhr   
Stundemax  = 23         # Bilder   bis  x Uhr 
mindif     =  1         # ein Bild alle x min  machen
    
cntmax     =  3         # Anzahl der Durchläufe

import os 

# Definitionen für IR-Led an Pin 25
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LedIR = 25   
GPIO.setup(LedIR, GPIO.OUT, initial= GPIO.LOW)
GPIO.output(LedIR,GPIO.HIGH)       # aus Invers
# GPIO.output(LedIR,GPIO.LOW)        # aus

# Definitionen für Neopixel-LED an Pin 21
import board
pixel_pin  = board.D21
import neopixel
num_pixels = 18             # The number of NeoPixels
ORDER      = neopixel.GRB   # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
pixels     = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
print( num_pixels, "Pixel an Pin: ", pixel_pin, "mit Order:", ORDER )

# Definition der Start- und Stoppzeit
starttime = datetime.time(Stundemin, 0)  #  
stopptime = datetime.time(Stundemax, 0)  #  

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")

for i in range(cntmax): 
   # Datum und Uhrzeit erfassen
    lt = localtime()
    Datum   = strftime("%d.%m.%Y", lt)
    Uhrzeit = strftime("%H:%M:%S", lt)
    print("Datum: ", Datum, "Uhrzeit:", Uhrzeit)

    now = datetime.datetime.now().time()
    if ( starttime <= now <= stopptime ):
        print( "Zeit zwischen", starttime, "und", stopptime, " -> Photo machen" )

        print(i, ". Photo mit Zeit im Namen und Beleuchtung")
        density = 50
        print("gelb  density:", density )  
        pixels.fill((density, density, 0 ))   
        pixels.show()
        print("                                 Photo    machen ")
        os.system('./PhotoMitDatum.sh')
        pixels.fill(( 0, 0, 0 ))   # Licht aus
        pixels.show()

        # Warten auf nächsten Durchgang mit mindif
        lt = localtime()
        minanf = int(strftime("%M", lt))
        print("warten ab  Minute = ", minanf, " min")
        minend = minanf - (minanf % mindif)     # modulo
        minend = minend + mindif
        if ( minend >= 60 ):
            minend = minend - 60
        print("warten bis Minute = ", minend, " min")
        if ( minend > 0 ):
            while ( minanf < minend ):
                lt = localtime()
                minanf = int(strftime("%M", lt))
        if ( minend == 0 ):
            while ( minanf > minend ):
                lt = localtime()
                minanf = int(strftime("%M", lt))
    else:
        print( "Zeit ausserhalb", starttime, "und", stopptime, "  kein Photo machen" )
        sleep(sleeptime2)  
