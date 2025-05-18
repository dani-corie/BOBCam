#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "d-IrStatus.py"

import time
sleeptime    = 5              # Pause zwischen den Durchläufen

# Definitionen für IR-Led an Pin 25
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LedIR = 25   
GPIO.setup(LedIR, GPIO.IN)

# GPIO.setup(LedIR, GPIO.OUT, initial= GPIO.LOW)
# GPIO.output(LedIR,GPIO.HIGH)       # ein
# GPIO.output(LedIR,GPIO.LOW)        # aus

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")

try:
    cntmax =  2
    for i in range(cntmax): 

        Status = GPIO.input(LedIR)
        print("Status von Pin", LedIR, "ist", Status)

# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:                  # Ende mit CTRL/c
    print ( "Ende von Programm ", programmname, " durch Benutzer")

   