from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)


COMFORTABLE_LOW = 14.0
COMFORTABLE_HIGH = 30.0
LONG_PAUSE = 0.4
SHORT_PAUSE = 0.1

LIGHT_BLUE = [0, 0, 48]
DARK_BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLACK = [0, 0, 0]

LB = LIGHT_BLUE
DB = DARK_BLUE
YW = YELLOW
BK = BLACK

LOGO = [
  DB, DB, DB, DB, LB, LB, LB, LB,
  DB, YW, DB, YW, LB, YW, LB, LB,
  DB, DB, YW, YW, YW, LB, LB, LB,
  DB, DB, DB, YW, YW, YW, LB, LB,
  LB, YW, YW, YW, YW, DB, YW, DB,
  LB, LB, LB, YW, DB, DB, DB, DB,
  LB, YW, YW, YW, YW, YW, YW, DB,
  LB, LB, LB, LB, DB, DB, DB, DB
]

BLANK = [BK for _ in range(64)]


def pull_row(src, dst, row):
  for _ in range(8):
    dst.pop()
  start_index = 63 - (row * 8)
  for pixel in range(start_index, start_index - 8, -1):
    dst.insert(0, src[pixel])
  return dst


def scroll_replace(src, dst):
  img = dst[:]
  for row in range(9):
    sense.set_pixels(img)
    img = pull_row(src, img, row)
    sleep(0.075)  


def flash_image(img):
  for _ in range(3):
    for screen in [BLANK, img]:
      sense.set_pixels(screen)
      sleep(0.3)

def draw_line(colour):
  for y in range(1, 8):
    sense.set_pixel(3, y, *colour)
  sleep(SHORT_PAUSE)
  sense.clear()


def twist_letter(letter, colour):
  for count in range(4):
    if letter == " ":
      sleep(LONG_PAUSE)
      continue
    sense.show_letter(letter, text_colour=colour)
    if count % 2 == 1:
      sense.flip_h()
    sleep(SHORT_PAUSE)
    sense.clear()
    draw_line(colour)
  sense.show_letter(letter, text_colour=colour)
  sleep(LONG_PAUSE)
  sense.clear()
  draw_line(colour)


def spin(msg, colour):
  for letter in msg:
    for angle in [0, 90, 180, 270]:
      sense.clear()
      sleep(0.1)
      sense.set_rotation(angle)
      sense.show_letter(
        letter,
        text_colour=colour
      )
      sleep(0.1)
    sleep(0.5)
    sense.clear()
 
  
sleep(1)
scroll_replace(LOGO, BLANK)
sleep(0.7)
flash_image(LOGO)
sleep(0.7)
scroll_replace(BLANK, LOGO)

for letter in "HELLO":
  twist_letter(letter, YW)

sense.show_message("The temperature is", scroll_speed=0.04)

temperature = round(sense.get_temperature())
if temperature < COMFORTABLE_LOW:
  spin("Cold", LB)
elif temperature > COMFORTABLE_HIGH:
  spin("Hot", RED)
else:
  spin("Nice", GREEN)