print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation



keyboard = KMKKeyboard()
LSFT = KC.LSFT(KC.SPACE(KC.LSFT))
RSFT = KC.RSFT(KC.SPACE(KC.RSFT))

keyboard.col_pins = (board.D13,board.D12,board.D11,board.D10,board.D9,board.D7,board.D4)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.A2,board.A3,board.A4,board.A5,board.D2)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LEFT, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,   KC.MINUS,

     KC.BSPC,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.TAB,

     KC.RBRC,KC.H,KC.J,KC.K,KC.L,KC.SCLN,KC.ENTER,

     KC.RPRN,KC.N,KC.M,KC.SLASH,KC.BSLASH,KC.QUOTE,KC.LGUI,

     KC.UP,KC.RSFT,KC.PDOT,KC.LALT,KC.COMM,  KC.SPACE,KC.DOWN]
]

if __name__ == '__main__':
    keyboard.go()

