import os

from slackclient import SlackClient

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
slack_token = os.environ["SLACK_TOKEN"]

def colorWipe(strip, color, wait_ms=50, reverse=False):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        pixel_i = strip.numPixels() -1 - i if reverse else i
        strip.setPixelColor(pixel_i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def nightRider(strip, leftToRight=True):
    direction = -1 if leftToRight else 1
    r = range(0, strip.numPixels()) if leftToRight else range((strip.numPixels()-1), -1, -1)
    for i in r:
        time.sleep(10/1000.0)
        strip.setPixelColor(i, Color(255, 0, 0 ))
        for n in range(0,9):
            p = (n * direction) + i
            if p < 0:
                p = n
            if p > strip.numPixels() - 1:
                p = strip.numPixels() - n
            b = 255 - (32 * n)
            color = b if b >= 0 else 0
            strip.setPixelColor(p, Color(color, 0, 0))
            strip.show()

        
def update_users(strip):
    sc = SlackClient(slack_token)
    
    users = sc.api_call(
        "users.list"
        )
    for u in users["members"]:
        if u["name"] == 'nick_bristow':
            print(u)
            print('')
            status = u['profile']['status_text']
            print(status)
            if status == 'Working remotely':
                strip.setPixelColor(45, Color(0, 0, 255))
                strip.show()
            if status == 'In the office':
                strip.setPixelColor(45, Color(0, 255, 0))
                strip.show()


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
            print ('Getting Users')
            for i in range(1,10): 
                nightRider(strip)
                nightRider(strip, False)
            update_users(strip)
            time.sleep(10)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)