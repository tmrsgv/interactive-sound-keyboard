#from msvcrt import getch # Only for Windows
import curses
# from playsound import playsound #Only works on Windows
from pygame import mixer
import pygame
import random
import os
import sys
from gpiozero import LED, Button
from time import sleep
import rdm6300
import soundPaths.py


os.chdir(os.path.dirname(sys.argv[0]))
print (os.getcwd())
cur = curses.initscr() # Initialize curses
curses.noecho()
curses.cbreak()

mixer.init() # Initialize sound library
mixer.music.load('./songs/start.wav')
mixer.music.play()

greenLed = LED(26)
greenButton = Button(19,pull_up = True,bounce_time= None)
whiteLed = LED(13)
whiteButton = Button(6,pull_up = True,bounce_time= None)
white2Led = LED(7)
white2Button = Button(8,pull_up = True,bounce_time= None)
redLed = LED(5)
redButton = Button(11,pull_up = True,bounce_time= None)
blueLed = LED(21)
blueButton = Button(20,pull_up = True,bounce_time= None)
yellowLed = LED(16)
yellowButton = Button(12,pull_up = True,bounce_time= None)

RFreader = rdm6300.Reader('/dev/ttyS0') #Initialize rfid card reader
cardSets = {
7633229 :  [cow, sheep, chicken, horse, duck],
7642883 : [lion, elephant, tiger, bear],
1234567 : [train, plane, car, tractor, bike],
7654321 : [piano, guitar, violin, trumpet, drum]}

# LED Layout (list subscript in parenthesis)
# ----------------------
# | Green(1)     Red(2)|
# | *                * |
# |                    |
# | *                * |
# |                    |
# | *                * |
# |                    |
# ----------------------

while (mixer.music.get_busy() == True):
    a=1

while True:
    try:
        card = RFreader.read()
        currentCard = card.value
        print(f"[{card.value}]")

        mixer.music.set_volume(0.8)
        mixer.music.stop()

        if greenButton.is_pressed:
            soundAndColor('greenLed', cardSets[currentCard][0])
        if yellowButton.is_pressed:
            soundAndColor('yellowLed', cardSets[currentCard][1])
        if whiteButton.is_pressed:
            soundAndColor('whiteLed', cardSets[currentCard][2])
        if white2Button.is_pressed:
            soundAndColor('white2Led', cardSets[currentCard][3])
        if blueButton.is_pressed:
            soundAndColor('blueLed', cardSets[currentCard][4])
        if redButton.is_pressed:
            soundAndColor('redLed', cardSets[currentCard][5])


    except:
        mixer.music.stop()
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        pygame.display.quit()
        pygame.quit()


def soundAndColor(LEDcolor, soundPath):

    LEDcolor.on()
    mixer.music.load(random.choice(soundPath))
    mixer.music.play()
    while (mixer.music.get_busy() == True):
        a=1
    LEDcolor.off()
