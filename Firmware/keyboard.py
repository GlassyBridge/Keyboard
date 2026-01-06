import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.row_pins = (
    board.P1_11,
    board.P1_13,
    board.P1_15,
    board.P0_29,
    board.P0_31,
    board.p0_30
)

keyboard.col_pins = (
    board.P0_27,
    board.P0_00,
    board.P1_12,
    board.P0_15,
    board.P0_16,
    board.P0_18,
    board.P0_17,
    board.P0_19,
    board.P0_21,
    board.P0_20,
    board.P0_22,    
    board.P0_23, 
    board.P1_00, 
    board.P0_24, 
    board.P0_25
)

keyboard.keymap = [
    [
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NO, KC.NO,
        KC.GRV, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.NO,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.HOME,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO, KC.END,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.NO, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.RALT, KC.RGUI,KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()