#!/usr/bin/python                            # Didi Lamken    10.05.2025
programmname = "a-IrPhotoUpload.py"
 
import datetime
import time
from   time import *
sleeptime = 1         # sec

import os 
import sys

DefKamera  = "BOBCamXX"                                                    #### Parameter
Directory  = "./a-recorded/" 
DefModus   = "NonInvers"
density    = 100   
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

# Datum und Uhrzeit erfassen                                                 #### Uhrzeit
lt = localtime()
Datum     = strftime("%d.%m.%Y", lt)
Uhrzeit   = strftime("%H:%M:%S", lt)
Timestamp = strftime("%Y%m%d-%H%M%S", lt)
print("   Photo am  ", Datum, "um", Uhrzeit, "Uhr mit Timestamp:", Timestamp )

if ( Modus == "Invers" ) : 
    print("   Invers     IR-Led ein ")
    GPIO.output(LedIR,GPIO.LOW)           # ein  bei Invers
if ( Modus == "NonInvers" ) : 
    print("   NonInvers  IR-Led ein ")
    GPIO.output(LedIR,GPIO.HIGH)          # ein

ShellCommand = "libcamera-still -t 1000 -n -o " + Directory + Kamera + "-" + Timestamp
ShellCommand = ShellCommand + "ir.jpg --hdr auto --autofocus-mode manual --lens-position 3.2 --width 1500"
os.system(ShellCommand)

if ( Modus == "Invers" ) : 
    print("   Invers     IR-Led aus ")
    GPIO.output(LedIR,GPIO.HIGH)         # aus  bei Invers
if ( Modus == "NonInvers" ) : 
    print("   NonInvers  IR-Led aus ")
    GPIO.output(LedIR,GPIO.LOW)          # aus

print(" ")
print("   Upload auf NextCloud")
ShellCommand = "/home/pi/BOBCamXX/3-UploadJpg.sh"
os.system(ShellCommand)

print(" ")
print("   Photo ins Archiv verschieben")
ShellCommand = "/home/pi/BOBCamXX/4-CreateMove.sh"
os.system(ShellCommand)

