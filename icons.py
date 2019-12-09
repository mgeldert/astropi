from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()
sense.set_rotation(270)

COMFORTABLE_LOW = 18.0
COMFRTABLE_HIGH = 24.0

LIGHT_BLUE = [0, 0, 48]
DARK_BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

LB = LIGHT_BLUE
DB = DARK_BLUE
YW = YELLOW
BK = BLACK
WH = WHITE
GN = GREEN
LG = [0, 48, 0]

COLD = [
  BK, WH, BK, BK, WH, BK, BK, BK,
  BK, BK, WH, BK, WH, BK, BK, WH,
  BK, BK, BK, WH, WH, BK, WH, BK,
  WH, WH, WH, WH, WH, WH, BK, BK,
  BK, BK, WH, WH, WH, WH, WH, WH,
  BK, WH, BK, WH, WH, BK, BK, BK,
  WH, BK, BK, WH, BK, WH, BK, BK,
  BK, BK, BK, WH, BK, BK, WH, BK
]

NICE = [
  BK, BK, BK, LG, LG, BK, BK, BK,
  BK, LG, BK, BK, BK, BK, LG, BK,
  BK, BK, BK, BK, BK, BK, BK, BK,
  LG, BK, GN, BK, BK, GN, BK, LG,
  LG, BK, BK, BK, BK, BK, BK, LG,
  BK, BK, GN, BK, BK, GN, BK, BK,
  BK, LG, BK, GN, GN, BK, LG, BK,
  BK, BK, BK, LG, LG, BK, BK, BK
]

HOT = [
  BK, BK, BK, BK, YW, BK, BK, BK,
  BK, YW, BK, BK, BK, BK, YW, BK,
  BK, BK, BK, YW, YW, BK, BK, BK,
  YW, BK, YW, YW, YW, YW, BK, BK,
  BK, BK, YW, YW, YW, YW, BK, YW,
  BK, BK, BK, YW, YW, BK, BK, BK,
  BK, YW, BK, BK, BK, BK, YW, BK,
  BK, BK, BK, YW, BK, BK, BK, BK
]

temperature = round(sense.get_temperature())
if temperature < COMFORTABLE_LOW:
  sense.set_pixels(COLD)
elif temperature > COMFRTABLE_HIGH:
  sense.set_pixels(HOT)
else:
  sense.set_pixels(NICE)