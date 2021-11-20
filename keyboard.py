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
import time
import rdm6300
from soundPaths import *

os.chdir(os.path.dirname(sys.argv[0]))
print (os.getcwd())
# cur = curses.initscr() # Initialize curses
# curses.noecho()
# curses.cbreak()

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

mixer.init() # Initialize sound library
mixer.music.set_volume(1.0)
mixer.music.load('./songs/start.wav')
mixer.music.play()

os.system("echo 0 | sudo tee /sys/class/leds/led1/brightness")
os.system("echo 0 | sudo tee /sys/class/leds/led0/brightness")

RFreader = rdm6300.Reader('/dev/ttyAMA0') #Initialize rfid card reader
currentCard = 0
cardSets = {
7646102 :  [cow, sheep, chicken, horse, duck, pig],
9819485 : [lion, elephant, monkey, bear, hawk, dolphin],
9811477 : [train, plane, car, tractor, bicycle, race_car],
9787282 : [piano, guitar, violin, trumpet, drum]}

# LED Layout (list subscript in parenthesis)
# ----------------------
# | Green(0)     Red(1)|
# | *                * |
# |                    |
# | *                * |
# |                    |
# | *                * |
# |                    |
# ----------------------


def gamePlay(stdscr):
    # Clear and refresh the screen for a blank canvas
    bootupLED()
    stdscr.clear()
    stdscr.refresh()
    currentCard = 0
    tStartPower = time.process_time()
    tStartRF = time.process_time()
    mixer.init()
    mixer.music.set_volume(1.0)
    while True:
        try:
            tCurrentRF = time.process_time()
            tCurrent = time.process_time()
            if (tCurrent - tStartPower > 5):
                print ("Shutting down...")
                shutdown()

            card = RFreader.read(timeout=None)
            time.sleep(0.0001)
            RFreader.stop()
            if card is not None:
                currentCard = card.value
                # print(card.value)
            else:
                greenLed.on()
                time.sleep(0.1)
                greenLed.off()

            if currentCard is not None:
                if greenButton.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(greenLed, cardSets[currentCard][0])
                    print(cardSets[currentCard][0])
                if yellowButton.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(yellowLed, cardSets[currentCard][1])
                    print(cardSets[currentCard][1])
                if whiteButton.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(whiteLed, cardSets[currentCard][2])
                    print(cardSets[currentCard][2])
                if white2Button.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(white2Led, cardSets[currentCard][3])
                    print(cardSets[currentCard][3])
                if blueButton.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(blueLed, cardSets[currentCard][4])
                    print(cardSets[currentCard][4])
                if redButton.is_pressed:
                    tStartPower = time.process_time()
                    soundAndColor(redLed, cardSets[currentCard][5])
                    print(cardSets[currentCard][5])


        except:
            mixer.music.stop()
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            pygame.display.quit()
            pygame.quit()


def soundAndColor(LEDcolor, soundPath):
    LEDcolor.on()
    print(LEDcolor)
    trackToPlay = random.choice(soundPath)
    mixer.music.load(trackToPlay)
    print(trackToPlay)
    mixer.music.play()
    while (mixer.music.get_busy() == True):
        a=1
    LEDcolor.off()

def shutdown():
    mixer.music.load('./songs/off_sound.wav')
    mixer.music.play()
    while (mixer.music.get_busy() == True):
        a=1
    time.sleep(0.5)
    mixer.music.stop()
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    pygame.display.quit()
    pygame.quit()
    time.sleep(0.5)
    os.system("sudo shutdown -h now")

def bootupLED():
    ledDelay = 0.55
    greenLed.on()
    time.sleep(ledDelay)
    whiteLed.on()
    time.sleep(ledDelay)
    blueLed.on()
    time.sleep(ledDelay)
    redLed.on()
    time.sleep(ledDelay)
    white2Led.on()
    time.sleep(ledDelay)
    yellowLed.on()
    time.sleep(ledDelay)
    greenLed.off()
    time.sleep(ledDelay)
    whiteLed.off()
    time.sleep(ledDelay)
    blueLed.off()
    time.sleep(ledDelay)
    redLed.off()
    time.sleep(ledDelay)
    white2Led.off()
    time.sleep(ledDelay)
    yellowLed.off()

def main():
    curses.wrapper(gamePlay)

if __name__ == "__main__":
    main()
