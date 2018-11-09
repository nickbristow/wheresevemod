import sys, termios, tty, os, time
from light_config import *
# from neopixel import *
import argparse

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_key_pressed():
  char = getch()
 
  if (char == "p"):
      print("Stop!")
      exit(0)

  if (char == "a"):
      print("Left pressed")
      time.sleep(button_delay)

  elif (char == "d"):
      print("Right pressed")
      time.sleep(button_delay)

  elif (char == "w"):
      print("Up pressed")
      time.sleep(button_delay)

  elif (char == "s"):
      print("Down pressed")
      time.sleep(button_delay)

  elif (char == "1"):
      print("Number 1 pressed")
      time.sleep(button_delay)
 
button_delay = 0.2

if __name__ == '__main__':
    

    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    
    # strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    
    # Intialize the library (must be called once before other functions).
    # strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            get_key_pressed()
    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 10)
