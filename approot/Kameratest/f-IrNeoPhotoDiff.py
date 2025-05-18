#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "f-IrNeoPhotoDiff.py"

import time
sleeptime1   = 1               # Pause zwischen den Durchläufen
sleeptime2   = 3               # Pause zwischen den Durchläufen

cntmax       = 4               # Anzahl der Photos
diffmax      = 20              # max. Differenz zwischen den Photos

import os 

# Definitionen für IR-Led an Pin 25
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LedIR = 25   
GPIO.setup(LedIR, GPIO.OUT, initial= GPIO.LOW)
# GPIO.output(LedIR,GPIO.HIGH)       # aus Invers
GPIO.output(LedIR,GPIO.LOW)        # aus

# Definitionen für Neopixel-LED an Pin 21
import board
pixel_pin  = board.D21
import neopixel
num_pixels = 10             # The number of NeoPixels
ORDER      = neopixel.GRB   # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
pixels     = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
print( num_pixels, "Pixel an Pin: ", pixel_pin, "mit Order:", ORDER )

# Image Difference
ImageDiff = 'testDiff.jpg'
from PIL import Image, ImageChops, ImageStat
def diff(Image1, Image2):
    im1 = Image.open(Image1)
    im2 = Image.open(Image2)
    diff_img           = ImageChops.difference(im1,im2)
#    print ('Saving diff image as',ImageDiff)
#    diff_img.convert('RGB').save(ImageDiff)
    stat               = ImageStat.Stat(diff_img)
    sum_channel_values = sum(stat.mean)
    max_all_channels   = len(stat.mean) * 100
    diff_ratio         = sum_channel_values/max_all_channels
    return diff_ratio

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
        os.system('./PhotoNeu.sh')

        print("LED IR    ", sleeptime1, " Sekunden aus")
        GPIO.output(LedIR,GPIO.LOW)        # aus
#       GPIO.output(LedIR,GPIO.HIGH)       # aus
        time.sleep(sleeptime2)    # Wartemodus für x Sekunden

        Image1    = "test-Alt.jpg"
        Image2    = "test-Neu.jpg"
        ImageDiff = "test-Diff" + str(i) + ".jpg"
        print(" ")
        diff_ratio  = diff( Image1, Image2 )
        diff_ratio1 = (diff_ratio * 1000 )
        print("1.:", Image1, "2.:", Image2, "Diff:", diff_ratio, "      Diff:", diff_ratio1 )
        print(" ")

        print( i, ". Photo von Neu nach Alt    " )
        os.system('./MoveToAlt.sh')

        # Photo mit Neopixel gelb nur bei diff_ratio1 > x     
        if ( diff_ratio1 > diffmax ):
            print("diff_ratio1 > diffmax   --> Photo mit Neopixel gelb ")
            print( i, ". Photo mit Datum    " )
            density = 100
            print("gelb  density:", density )  
            pixels.fill((density, density, 0 ))       # Neopixel-Licht an
            pixels.show()
            os.system('./PhotoMitDatum.sh')
            pixels.fill(( 0, 0, 0 ))                  # Neopixel-Licht aus
            pixels.show()
        print(" ")
        print("                         warten ...  ", sleeptime2, " Sekunden aus")
        time.sleep(sleeptime2)    # Wartemodus für x Sekunden

    print ( "Ende von Programm ", programmname, " normal durch Programm")

# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:                  # Ende mit CTRL/c
    print ( "Ende von Programm ", programmname, " durch Benutzer")


   