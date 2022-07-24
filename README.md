# Interactive Sound Keyboard (Kids Toy)
A smart, interactive, python based, kids toy. A re-take on old-school "farm animals sound" toys.

## Table of Contents
* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Non-SW](#Non-SW)
* [Author](#author)
* [License](#license)

## Description
A while back I wanted to create children's toys, but with a twist.
As a first take in the field, thought it would be interesting to do something related to those old-school farm animal sound toys. I am talking about the ones with the animals lined up and concealed, press a big plastic button and the corresponding animal would pop up and make the animal's sound.
Now that's nice and all, but very limited.
The new and improved version features six LED big arcade buttons with a printed card slip in the middle.
The card has a nice secret inside, an RFID tag. The toy casing holds the RFID reader, and as you have probably figured out by now, will change the set of sounds the toy can generate as a function of which card is being mounted on the toy.

So far I have created the ol' classic farm animal sound set, safari animals, transportation, and musical instruments.

Further features include:
- Sound and light sequence at start and shutdown
- Implementation of a sleep timer for energy saving
- having multiple sounds (of the same type) for each button, meaning there will be a random sound even if you press the same button twice

## Installation
No installation required, just put the project folder on a Raspberry Pi and run the 'keyboard.py'. It is recommended to create a deamon or service to run at Rpi boot.

## Usage
All of the framework is ready for operation. All is required is changing the RFID tags UID in the code to match your specific tags
Changing of sound sets is done 'on the fly' when the device is ON and cards are swapped

## Non-SW
### HW Shopping List
- A Raspberry Pi 2 and above would be optimal
- computer speakers, with a built-in amp and 5V and 3.5mm inputs (can be connected directly to the Rpi)
- 6 'arcade style' push buttons (with LEDs)
- A Li-ion battery output 5V (can use a powerbank)
- RFID tag reader
- Some Jumper wires
- A box to hold everything together

### Further Info
- Electrical diagrams TBD
- Project photos TBD

## Author
Myself, Tomer Segev

## License
This project is licensed under GNU GPLv3 license
