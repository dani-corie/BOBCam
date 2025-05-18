#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "e-IrDauerPhoto.py"

import time
sleeptime1   = 1               # Pause zwischen den Durchläufen
sleeptime2   = 2               # Pause zwischen den Durchläufen

cntmax       = 4               # Anzahl der Photos

import os 

# Definitionen für IR-Led an Pin 25
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LedIR = 25   
GPIO.setup(LedIR, GPIO.OUT, initial= GPIO.LOW)
# GPIO.output(LedIR,GPIO.HIGH)       # ein
# GPIO.output(LedIR,GPIO.LOW)        # aus

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")

try:
    for i in range(cntmax): 

        print(" ")
        print("LED IR    ", sleeptime1, " Sekunden ein ")
        GPIO.output(LedIR,GPIO.HIGH)       # ein
#       GPIO.output(LedIR,GPIO.LOW)        # ein
        time.sleep(sleeptime1)    # Wartemodus für x Sekunden

        print( i, ". Photo mit Datum    " )
        os.system('./PhotoMitDatum.sh')

        print("LED IR    ", sleeptime2, " Sekunden aus")
        GPIO.output(LedIR,GPIO.LOW)        # aus
#       GPIO.output(LedIR,GPIO.HIGH)       # aus
        time.sleep(sleeptime2)    # Wartemodus für x Sekunden

# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:                  # Ende mit CTRL/c
    print ( "Ende von Programm ", programmname, " durch Benutzer")
#   GPIO.cleanup()   # schaltet IR-Led ein

   