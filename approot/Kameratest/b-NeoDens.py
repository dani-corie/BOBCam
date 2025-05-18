#!/usr/bin/python                            # Didi Lamken    16.04.2025
programmname = "b-NeoDens.py"

import time
sleeptime    = 1               # Pause zwischen den Durchläufen

import os 

# Definitionen für Neopixel-LED an Pin 21
import board
pixel_pin  = board.D21
import neopixel
num_pixels = 10             # The number of NeoPixels
ORDER      = neopixel.GRB   # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
pixels     = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
print( num_pixels, "Pixel an Pin: ", pixel_pin, "mit Order:", ORDER )

# Hauptprogrammschleife
print ("Start von Programm ", programmname )
print (" ")

cntmax =  6
for i in range(cntmax): 
    density = i * 50

    print("rot  density:", density )
    pixels.fill((density, 0, 0 ))   
    pixels.show()
    time.sleep(sleeptime)

    print("gelb")
    pixels.fill((density, density, 0 )) 
    pixels.show()
    time.sleep(sleeptime)

    print("gruen")
    pixels.fill((0, density, 0 ))   
    pixels.show()
    time.sleep(sleeptime)

    print("blau")
    pixels.fill((0, 0, density )) 
    pixels.show()
    time.sleep(sleeptime)

    print("weiss")
    pixels.fill((density, density, density ))  
    pixels.show()
    time.sleep(sleeptime)

pixels.fill((0, 0, 0 )) 
pixels.show()