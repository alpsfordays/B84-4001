import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap]

keyboard.col_pins = (board.A0,board.A1,board.A2,board.A3,board.D24,board.D25,board.SCK,board.MOSI,board.MISO,board.D2,board.RX,board.TX,)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.D13,board.D12, board.D11,board.D10, board.D9,board.D7,board.SDA,)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
    KC.PAUS, KC.SLCK, KC.PSCR, KC.TG(1),KC.F10,  KC.F9,   KC.F8,   KC.F7,   KC.F6,   KC.F5,   KC.F4,   KC.F3,   KC.F2,   KC.F1,   KC.ESC,
    KC.HOME, KC.BSPC, KC.EQL,  KC.MINS, KC.N0,   KC.N9,   KC.N8,   KC.N7,   KC.N6,   KC.N5,   KC.N4,   KC.N3,   KC.N2,   KC.N1,
    KC.PGUP, KC.BSLS, KC.RBRC, KC.LBRC, KC.P,    KC.O,    KC.I,    KC.U,    KC.Y,    KC.T,    KC.R,    KC.E,    KC.W,    KC.Q,    KC.TAB,
    KC.PGDN, KC.ENT,  KC.QUOT, KC.SCLN, KC.L,    KC.K,    KC.J,    KC.H,    KC.G,    KC.F,    KC.D,    KC.S,    KC.A,    KC.CAPS,
    KC.END,  KC.UP,   KC.RSFT, KC.SLSH, KC.DOT,  KC.COMM, KC.M,    KC.N,    KC.B,    KC.V,    KC.C,    KC.X,    KC.Z,    KC.LSFT,
    KC.RGHT, KC.DOWN, KC.LEFT, KC.DEL,  KC.INS,  KC.RALT, KC.SPC,  KC.GRV,  KC.LGUI, KC.LALT, KC.LCTL,
    ],
    [
    KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.F12,  KC.F11,  KC.ESC,  
    KC.NO,   KC.BSPC, KC.NO,   KC.NO,   KC.PAST, KC.P9,   KC.P8,   KC.P7,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  
    KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.PMNS, KC.P6,   KC.P5,   KC.P4,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  
    KC.NO,   KC.PENT, KC.NO,   KC.PPLS, KC.P3,   KC.P2,   KC.P1,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  
    KC.NO,   KC.NO,   KC.NO,   KC.PSLS, KC.PDOT, KC.NO,   KC.P0,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  
    KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS,  
    ]
]


if __name__ == '__main__':
    keyboard.go()