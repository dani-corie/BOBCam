#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "a-EinPhoto.py"

import time
sleeptime    = 1              # Pause zwischen den Durchläufen

import os 

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")

os.system('./PhotoMitDatum.sh')

print ( "Ende von Programm ", programmname, " durch Benutzer")
