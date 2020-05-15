#from msvcrt import getch # Only for Windows
import curses
from playsound import playsound
import random

cur = curses.initscr() # Initialize curses

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
    key = ord(cur.getch())
    print(key)
    if (key == 99): #c
        playsound(random.choice(cow))

    if (key == 100):
        playsound(random.choice(sheep))

    if (key == 101):
        playsound(random.choice(chicken))

    if (key == 102):
        playsound(random.choice(horse))

    if (key == 103):
        playsound(random.choice(elephant))

    if (key == 104):
        playsound(random.choice(lion))
