#from msvcrt import getch # Only for Windows
import curses
from playsound import playsound #Only works on Windows
from pygame import mixer
import random

cur = curses.initscr() # Initialize curses
mixer.init() # Initialize sound library

cow = ['./animals/cow.wav',
       './animals/cow2.wav',
       './animals/cow3.wav',
       './animals/cow4.wav',
       './animals/cow5.wav',
       './animals/cow6.wav']

sheep = ['./animals/sheep.wav',
       './animals/sheep2.wav',]

horse = ['./animals/horse.wav',
       './animals/horse2.wav',
       './animals/horse3.wav',
       './animals/horse4.wav',
       './animals/horse5.wav',
       './animals/horse6.wav']

duck = ['./animals/duck.wav',
       './animals/duck2.wav',
       './animals/duck3.wav',
       './animals/duck4.wav',
       './animals/duck5.wav',
       './animals/duck6.wav']

elephant = ['./animals/elephant.wav',
            './animals/elephant2.wav',
            './animals/elephant3.wav']

lion = ['./animals/lion.wav',
        './animals/lion2.wav',
        './animals/lion3.wav',
        './animals/lion4.wav',
        './animals/lion5.wav',
        './animals/lion6.wav']

chicken = ['./animals/chicken.wav',
           './animals/chicken2.wav',
           './animals/chicken3.wav',
           './animals/chicken4.wav',
           './animals/chicken5.wav',
           './animals/chicken6.wav',
           './animals/chicken7.wav',
           './animals/chicken8.wav']

while True:
    key = cur.getkey() # Listen for keypresses - returns key character (char)
    mixer.music.set_volume(0.7)
    mixer.music.pause()
    print(key)
    
    if (key == 'q'):
        mixer.music.load(random.choice(cow))
        mixer.music.play()

    if (key == 100):
        mixer.music.load(random.choice(sheep))
        mixer.music.play()

    if (key == 101):
        mixer.music.load(random.choice(chicken))
        mixer.music.play()

    if (key == 102):
        mixer.music.load(random.choice(horse))
        mixer.music.play()

    if (key == 103):
        mixer.music.load(random.choice(elephant))
        mixer.music.play()

    if (key == 104):
        mixer.music.load(random.choice(lion))
        mixer.music.play()
