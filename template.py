from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

#     R    G    B
b = (  0,   0,   0)   # Black
w = (255, 255, 255)   # White
r = (255,   0,   0)   # Red
o = (255, 127,   0)   # Orange
y = (255, 255,   0)   # Yellow
g = (  0, 255,   0)   # Green
B = (  0,   0, 255)   # Blue
i = ( 75,   0, 130)   # Indigo
v = (148,   0, 211)   # Violet


picture = [
  w, r, o, y, g, B, i, v,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


#temp = round(sense.temperature)
#sense.set_pixels(BLANK)
#sleep(2)
#sense.show_message("It is " + str(temp) + " degrees", scroll_speed=0.05, text_colour=B)

