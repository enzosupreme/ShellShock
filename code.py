from kb import KMKKeyboard
import board
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.modtap import ModTap
from kmk.keys import KC



keyboard = KMKKeyboard()

modtap = ModTap()
layers_ext = Layers()

keyboard.extensions = [layers_ext]

# Cleaner key name.
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.TO(2)
RAI = KC.MO(1)
RAISE = KC.TO(1)
QWERTY = KC.TO(0)

SIFL =  KC.MT(KC.SPACE,KC.LSFT)
SIFR =  KC.MT(KC.SPACE,KC.RSFT)

UNDO = KC.RCTL(KC.Z)
CUT  = KC.RCTL(KC.X)
COPY  = KC.RCTL(KC.C)
PASTE  = KC.RCTL(KC.V)

COLL = KC.LSFT(KC.SCLN)
PIPER = KC.LSFT(KC.BSLS)

# ---- EMOTES ---- #

SMIRK = simple_key_sequence(
    (

    COLL,
    KC.S,
    KC.M,
    KC.I,
    KC.R,
    KC.K,
    COLL,

    KC.SPACE,
    )
)
LOVE = simple_key_sequence(
    (

    COLL,
    KC.H,
    KC.E,
    KC.A,
    KC.R,
    KC.T,
    COLL,

    KC.SPACE,
    )
)

ANGERY = simple_key_sequence(
    (

    COLL,
    KC.A,
    KC.N,
    KC.G,
    KC.E,
    KC.R,
    KC.Y,
    COLL,

    KC.SPACE,
    )
)

SPOIL = simple_key_sequence(
    (

    PIPER,
    PIPER,
    KC.SPACE,
    PIPER,
    PIPER,
    KC.LEFT,
    KC.LEFT,
    KC.SPACE,
    )
)



# ---- SHORTCUTS ---- #


SNIP = simple_key_sequence(
    (
    KC.LGUI,
    KC.S,
    KC.N,
    KC.I,
    KC.P,
    KC.ENT,
    KC.ENT,
    )
)

MUED = simple_key_sequence(
    (
    KC.LGUI,
    KC.M,
    KC.U,
    KC.SPACE,
    KC.E,
    KC.ENT,
    KC.ENT,
    )
)

FUSE = simple_key_sequence(
    (
    KC.LGUI,
    KC.F,
    KC.U,
    KC.S,
    KC.I,
    KC.ENT,
    KC.ENT,
    )
)

VIS = simple_key_sequence(
    (
    KC.LGUI,
    KC.V,
    KC.I,
    KC.S,
    KC.U,
    KC.ENT,
    KC.ENT,
    )
)




KC_GRSF = KC.RSFT(KC.GRV)


keyboard.keymap = [
    [  #QWERTY
        KC.TILD, KC.N1,   KC.N2, KC.N3, KC.N4, KC.N5, KC.RIGHT,         KC.LEFT, KC.N6,     KC.N7,     KC.N8,     KC.N9,     KC.N0, KC.MINS,
        KC.TAB,   KC.Q,    KC.W, KC.E, KC.R, KC.T,    KC.BSPC,       KC.BSPC,   KC.Y,    KC.U,     KC.I,     KC.O,  KC.P, KC.TAB,
        KC.ENT,   KC.A,    KC.S,KC.D,KC.F,KC.G, KC.LBRC,    KC.RBRC,   KC.H,  KC.J,  KC.K,   KC.L,  KC.SCLN,  KC.ENT,
        RAI,  KC.Z,  KC.X,    KC.C,  KC.V,   KC.B,   KC.LPRN,          KC.RPRN, KC.N, KC.M, KC.SLSH, KC.BSLS,KC.QUOT,KC.EQL,
        RAISE, KC.LWIN, KC.LALT, KC.LCTRL, KC.COMM, SIFL,KC.DOWN,                 KC.UP, SIFR, KC.DOT, KC.RCTRL, KC.RALT,  KC.DEL,  LOWER,

    ],
    [  #RAISE
        KC.F11, KC.F1,   KC.F2, KC.F3, KC.F4, KC.F5, KC.MNXT,             KC.MPRV, KC.F6,     KC.F7,     KC.F8,     KC.F9,     KC.F10, KC.F12,
        KC.TAB,   KC.Q,    KC.UP,     KC.E, KC.R, KC.T,    KC.BSPC,       KC.BSPC,   KC.Y,    KC.N7,     KC.N8,     KC.N9,  KC.P, KC.TAB,
        KC.ENT,   KC.LEFT,KC.DOWN,KC.RIGHT,KC.MUTE, KC.MPLY,   KC.LBRC,    KC.RBRC,   KC.DEL,  KC.N4,  KC.N5,   KC.N6,  KC.SCLN,  KC.ENT,
        QWERTY,  UNDO,  CUT,    COPY,  PASTE,   KC.B,   KC.LPRN,          KC.RPRN, KC.N, KC.N1, KC.N2, KC.N3,KC.N0,KC.PLUS,
        LOWER, KC.MUTE, KC.LWIN, KC.LCTRL, KC.COMM, SIFL,KC.VOLD,                 KC.VOLU, SIFR, KC.DOT, KC.RALT, KC.EQL,  KC.MINS,  KC.CAPS,
    ],
    [  #LAUNCHER
        XXXXXXX, XXXXXXX,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RIGHT,         KC.LEFT, XXXXXXX, XXXXXXX, XXXXXXX,   XXXXXXX,  XXXXXXX, XXXXXXX,
        KC.TAB,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    KC.BSPC,       KC.BSPC,   XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX, XXXXXXX, KC.TAB,
        KC.ENT,   VIS,    SNIP,     MUED,     FUSE,     KC.G, KC.LBRC,      KC.RBRC,   LOVE,  SMIRK,  ANGERY,  SPOIL,  KC.SCLN,  KC.ENT,
        QWERTY,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, XXXXXXX,   KC.LPRN,            KC.RPRN, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,XXXXXXX,KC.DOT,
        LOWER,KC.MUTE, KC.LWIN, KC.LCTRL, KC.COMM, SIFL,KC.DOWN,                 KC.UP, SIFR, KC.DOT, KC.RALT, KC.EQL,  KC.DEL,  KC.CAPS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
