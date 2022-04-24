print("Starting")

import board

from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.keys import KC
from kmk.matrix import DiodeOrientation



keyboard = KMKKeyboard()
modtap_ext = ModTap()
layers_ext = Layers()
keyboard.modules.append(modtap_ext)
#split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT

data_pin = board.SCL if split_side == SplitSide.LEFT else board.SCL
data_pin2 = board.SDA if split_side == SplitSide.LEFT else board.SDA

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=True,
    data_pin=data_pin,
    data_pin2=data_pin2
)

RSFT = KC.MT(KC.SPC, KC.RSFT)
LSFT = KC.MT(KC.SPC, KC.LSFT)

keyboard.col_pins = (board.D4,board.D7,board.D9,board.D10,board.D11,board.D12,board.D13)
keyboard.row_pins = (board.A2,board.A3,board.A4,board.A5,board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.TILD, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,   KC.RIGHT,

     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.BSPC,

     KC.ENTER,KC.A,KC.S,KC.D,KC.F,KC.G,KC.LBRC,

     KC.EQL,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.LPRN,

     KC.ESC,KC.MUTE,KC.LWIN,KC.LALT,KC.COMM,  LSFT,KC.DOWN]
]

if __name__ == '__main__':
    keyboard.go()

