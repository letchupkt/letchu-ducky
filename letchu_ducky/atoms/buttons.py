import digitalio, board
from neopixel import NeoPixel

pixel = NeoPixel(board.GP13, 1, brightness=0.2)
button = digitalio.DigitalInOut(board.GP12)