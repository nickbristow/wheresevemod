import os

from slackclient import SlackClient

import time
from neopixel import *
from slack_users import *
import argparse

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
slack_token = os.environ["SLACK_TOKEN"]
sc = SlackClient(slack_token)

def colorWipe(strip, color, wait_ms=50, reverse=False):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        pixel_i = strip.numPixels() -1 - i if reverse else i
        strip.setPixelColor(pixel_i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def nightRider(strip, leftToRight=True):
    red = 12
    green = 12
    blue = 100
    color = Color(red,green,blue)
    direction = -1 if leftToRight else 1
    r = range(0, strip.numPixels()) if leftToRight else range((strip.numPixels()-1), -1, -1)
    for i in r:
        time.sleep(20/1000.0)
        strip.setPixelColor(i, color)
        for n in range(1,9):
            p = (n * direction) + i
            if p < 0:
                p = n
            if p > strip.numPixels() - 1:
                p = strip.numPixels() - n
            b = 16 - 2*n
            #color = b if b >= 0 else 0
            #color = Color(0,color,0)
            #print(color)
            dim_percent = ((8.0-n)/8.0)*0.5
            dim_color = Color(
                int(round(red * dim_percent)),
                int(round(green * dim_percent)),
                int(round(blue * dim_percent))
            )
            strip.setPixelColor(p, dim_color)
            strip.show()

        
def update_users(strip):
    users = sc.api_call(
        "users.list"
        )
    nightRider(strip)
    colorWipe(strip, Color(0,0,0), 1)
    
    for u in users["members"]:
        #if 'joe' in u["name"]:
            #print(u)
        name = u["profile"]["real_name_normalized"]
        if name in EXCELLA_SLACK_USERS:
            print(name)
            status = u['profile']['status_text']
            if status == 'Working remotely':
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], Color(30, 30, 255))
                strip.show()
            elif status == 'In the office':
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], Color(0, 255, 0))
                strip.show()
            elif status == 'Vacationing':
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], Color(127, 0, 255))
                strip.show()
            elif status == 'Out Sick':
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], Color(255, 0, 0))
                strip.show()
            elif status == 'Can be reached by phone/slack':
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], Color(255, 255, 0))
                strip.show()
            else:
                pcolor = Color(255, 255, 255) if check_user_presence(u["id"]) == "active" else Color(194, 76, 0)
                strip.setPixelColor(EXCELLA_SLACK_USERS[name], pcolor)
                strip.show()

def check_user_presence(user_id):
    presence = sc.api_call(
        "users.getPresence",
        user=user_id
        )
    return presence["presence"]

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
            
            update_users(strip)
            time.sleep(60)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)