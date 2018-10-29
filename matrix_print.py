import os
import time
import time
from neopixel import *
import argparse
from mod_color import *

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

alphabit = {
  "A": [
  [0,1,1,0],
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "B": [
  [1,1,0],
  [1,0,1],
  [1,1,0],
  [1,0,1],
  [1,1,0]
  ],
  "C": [
  [0,1,1],
  [1,0,0],
  [1,0,0],
  [1,0,0],
  [0,1,1]
  ],
  "D": [
  [1,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,0]
  ],
  "E": [
  [1,1,1],
  [1,0,0],
  [1,1,1],
  [1,0,0],
  [1,1,1]
  ],
  "F": [
  [1,1,1],
  [1,0,0],
  [1,1,0],
  [1,0,0],
  [1,0,0]
  ],
  "G": [
  [0,1,1,0],
  [1,0,0,0],
  [1,0,1,0],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "H": [
  [0,0,0],
  [1,0,1],
  [1,1,1],
  [1,0,1],
  [0,0,0]
  ],
  "I": [
  [1],
  [0],
  [1],
  [1],
  [1]
  ],
  "J": [
  [0,0,1],
  [0,0,1],
  [0,0,1],
  [1,0,1],
  [0,1,0]
  ],
  "K": [
  [1,0,0,1],
  [1,0,1,0],
  [1,1,0,0],
  [1,0,1,0],
  [1,0,0,1]
  ],
  "L": [
  [1,0,0],
  [1,0,0],
  [1,0,0],
  [1,0,0],
  [1,1,1]
  ],
  "M": [
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "N": [
  [1,0,0,1],
  [1,1,0,1],
  [1,0,1,1],
  [1,0,1,1],
  [1,0,0,1]
  ],
  "O": [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "P": [
  [1,1,0],
  [1,0,1],
  [1,1,0],
  [1,0,0],
  [1,0,0]
  ],
  "Q": [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,1,1],
  [0,1,1,1]
  ],
  "R": [
  [1,1,1,0],
  [1,0,0,1],
  [1,1,1,0],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "S": [
  [0,1,1],
  [1,0,0],
  [0,1,0],
  [0,0,1],
  [1,1,0]
  ],
  "T": [
  [1,1,1],
  [0,1,0],
  [0,1,0],
  [0,1,0],
  [0,1,0]
  ],
  "U": [
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "V": [
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,0]
  ],
  "W": [
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,1],
  [1,1,1,1],
  [0,1,1,0]
  ],
  "X": [
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,0],
  [0,1,1,0],
  [1,0,0,1]
  ],
  "Y": [
  [1,0,1,0],
  [1,0,1,0],
  [0,1,0,0],
  [0,1,0,0],
  [0,1,0,0]
  ],
  "Z": [
  [1,1,1,1],
  [0,0,1,0],
  [0,1,0,0],
  [1,0,0,0],
  [1,1,1,1]
  ],
  "SPACE": [
    [0],
    [0],
    [0],
    [0],
    [0]
  ]
}

light_array = [
    [49,48,47,46,45,44,43,42,41,40],
    [30,31,32,33,34,35,36,37,38,39],
    [29,28,27,26,25,24,23,22,21,20],
    [10,11,12,13,14,15,16,17,18,19],
    [9,8,7,6,5,4,3,2,1,0]
]

def colorWipe(strip, color, wait_ms=50, reverse=False):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        pixel_i = strip.numPixels() -1 - i if reverse else i
        strip.setPixelColor(pixel_i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def build_message(mes):
  mes = mes.upper()
  mes_matrix = [
    [],
    [],
    [],
    [],
    []
  ]
  for c in list(mes):
    c = c if c != ' ' else "SPACE"
    if alphabit[c]:
      for index, row in enumerate(alphabit[c]):
        mes_matrix[index].extend(row)
        mes_matrix[index].extend([0])
  return mes_matrix

def print_message(mes, strip):
  display = [
    [" ", " "," ", " "," ", " "," ", " "," ", " "],
    [" ", " "," ", " "," ", " "," ", " "," ", " "],
    [" ", " "," ", " "," ", " "," ", " "," ", " "],
    [" ", " "," ", " "," ", " "," ", " "," ", " "],
    [" ", " "," ", " "," ", " "," ", " "," ", " "]
  ]
  message = build_message(mes)
  while len(message[0]) > 0:
    display_message(display)
    display_message_on_strip(strip, display)
    time.sleep(0.25)
    display = shift_left(display)
    for index, row in enumerate(message):
      display[index][-1] = row.pop(0)

def shift_left(display):
  for row in display:
    row.pop(0)
    row.append(' ')
  return display

def display_message_on_strip(strip, display):
    for row_i, row in enumerate(display):
        for col_i, col in enumerate(row):
          char = RandomColor() if col == 1 else Color(0,0,0)
          pixel_i = light_array[row_i][col_i]
          strip.setPixelColor(pixel_i, char)
    strip.show()

def display_message(display):
  for row in display:
    row_string = ''
    for col in row:
      char = col if col == 1 else ' '
      row_string = row_string + str(char) + ' '
    print(row_string)


#print_message("Hello world")
    # Main program logic follows:
if __name__ == '__main__':
    

    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print_message('hello hugh     ', strip)
    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 10)
