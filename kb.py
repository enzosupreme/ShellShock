import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP22,
	 board.GP21,
	 board.GP20,
	 board.GP19,
	 board.GP18,)
    col_pins = (board.GP9,
	 board.GP10,
	 board.GP11,
	 board.GP12,
	 board.GP13,
	 board.GP14,
	 board.GP15,
     board.GP8,
     board.GP7,
     board.GP6,
     board.GP5,
     board.GP4,
     board.GP3,
     board.GP2,)

    diode_orientation = DiodeOrientation.COL2ROW
    #led_pin = board.P1_06
    #rgb_pixel_pin = board.P0_06
    #rgb_num_pixels = 12
    #data_pin = board.SDA
    #data_pin2 = board.SCL
    #i2c = board.I2C
    #powersave_pin = board.P0_13

    # NOQA
    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  5, 6,           7, 8, 9, 10, 11, 12, 13,
     14,  15,  16, 17, 18, 19, 20,          21, 22, 23, 24, 25, 26, 27,
     28, 29, 30, 31, 32, 33, 34,         35, 36, 37, 38, 39, 40, 41,
        42, 43, 44, 45, 46,47, 48,           49, 50, 51, 52, 53, 54, 55,
      56,57, 58, 59, 60, 61, 62,       63, 64, 65, 66, 67, 68, 69,
    ]
