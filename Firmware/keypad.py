#This is a test firmware to check if the keypad is working properly
import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.ioexpander.mcp230xx import MCP23017

keypad = KMKKeyboard()
keypad.modules.append(Layers())

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c=i2c, address=0x20)

keypad.row_pins = (
    mcp.get_pin(4), 
    mcp.get_pin(3), 
    mcp.get_pin(2), 
    mcp.get_pin(1), 
    mcp.get_pin(0)
)
keypad.col_pins = (
    mcp.get_pin(5), 
    mcp.get_pin(6), 
    mcp.get_pin(8), 
    mcp.get_pin(9)
)

keypad.diode_orientation = DiodeOrientation.COLUMNS

keypad.keymap = [
    [
        KC.NLCK, KC.PSCR, KC.DOT, KC.PSLS,
        KC.P1,   KC.P2,   KC.P3,  KC.PPLS,
        KC.P4,   KC.P5,   KC.P6,  KC.PMNS,
        KC.P7,   KC.P8,   KC.P9,  KC.PENT,
        KC.PAST, KC.P0,   KC.PDOT,KC.PEQL,
    ],
]

if __name__ == '__main__':
    keypad.go()