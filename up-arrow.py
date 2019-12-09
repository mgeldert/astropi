from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

RD = [255, 0, 0]
BK = [0, 0, 0]

STRAIGHT_ARROW = [
  BK, BK, BK, RD, RD, BK, BK, BK,
  BK, BK, RD, RD, RD, RD, BK, BK,
  BK, RD, BK, RD, RD, BK, RD, BK,
  BK, BK, BK, RD, RD, BK, BK, BK,
  BK, BK, BK, RD, RD, BK, BK, BK,
  BK, BK, BK, RD, RD, BK, BK, BK,
  BK, BK, BK, RD, RD, BK, BK, BK,
  BK, BK, BK, RD, RD, BK, BK, BK
]

DIAGONAL_ARROW = [
  BK, BK, BK, BK, RD, RD, RD, RD,
  BK, BK, BK, BK, BK, RD, RD, RD,
  BK, BK, BK, BK, RD, RD, RD, RD,
  BK, BK, BK, RD, RD, RD, BK, RD,
  BK, BK, RD, RD, RD, BK, BK, BK,
  BK, RD, RD, RD, BK, BK, BK, BK,
  RD, RD, RD, BK, BK, BK, BK, BK,
  BK, RD, BK, BK, BK, BK, BK, BK
]


def set_rotation_angle(yaw_degrees):
  if 25 <= yaw_degrees < 65:
    arrow = DIAGONAL_ARROW
    angle = 0
  elif 65 <= yaw_degrees < 115:
    arrow = STRAIGHT_ARROW
    angle = 0
  elif 115 <= yaw_degrees < 155:
    arrow = DIAGONAL_ARROW
    angle = 270
  elif 155 <= yaw_degrees < 205:
    arrow = STRAIGHT_ARROW
    angle = 270
  elif 205 <= yaw_degrees < 245:
    arrow = DIAGONAL_ARROW
    angle = 180
  elif 245 <= yaw_degrees < 295:
    arrow = STRAIGHT_ARROW
    angle = 180
  elif 295 <= yaw_degrees < 335:
    arrow = DIAGONAL_ARROW
    angle = 90
  else:
    arrow = STRAIGHT_ARROW
    angle = 90
  return arrow, angle


while True:
  orientation = sense.get_orientation_degrees()
  yaw = round(orientation['yaw'])
  arrow, angle = set_rotation_angle(yaw)
  sense.set_rotation(angle)
  sense.set_pixels(arrow)
  sleep(0.2)