"""
Boardsource Lulu SMT RP2040 - KMK Firmware Configuration
Main configuration file with all features enabled
"""
print("Starting Boardsource Lulu KMK Firmware")

import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.handlers.sequences import simple_key_sequence

# Initialize keyboard
keyboard = KMKKeyboard()

# ============================================================================
# MODULES SETUP
# ============================================================================

# Layers module
layers = Layers()

# Split keyboard configuration
# Using auto-detection based on drive name (should end with 'L' or 'R')
split = Split(
    split_flip=True,  # Lulu halves are mirrored
    split_side=None,  # Auto-detect from drive name
    split_type=SplitType.UART,
    split_target_left=True,
    uart_interval=20,
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    uart_flip=True,  # Connected through same pins
    use_pio=True,  # Use PIO for RP2040
)

# HoldTap module for home row mods
holdtap = HoldTap()
holdtap.tap_time = 200  # 200ms tap time

# Combos module
combos = Combos()

# Encoder handler
encoder_handler = EncoderHandler()

# RGB extension with per-key support
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=keyboard.rgb_num_pixels,
    rgb_order=(1, 0, 2),  # GRB for WS2812B
    val_limit=150,  # Limit brightness to 150/255 to reduce power draw
    hue_default=100,
    sat_default=255,
    val_default=100,
    animation_mode=AnimationModes.BREATHING,
    animation_speed=2,
    hue_step=10,
    sat_step=17,
    val_step=17,
)

# Add modules to keyboard (ORDER MATTERS!)
# Split must be added after HoldTap
keyboard.modules = [layers, holdtap, combos, split, encoder_handler]
keyboard.extensions = [rgb]

# ============================================================================
# ENCODER CONFIGURATION
# ============================================================================

# Configure encoders - one on each side
# Left encoder pins are defined in kb.py
# Right encoder will be auto-configured by split module
encoder_handler.pins = (
    (keyboard.encoder_pin_a, keyboard.encoder_pin_b, keyboard.encoder_button, False),
)

# Encoder map: (CCW, CW, Button) for each layer
encoder_handler.map = [
    # Layer 0 (Base): Volume control
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    # Layer 1 (Lower): Undo/Redo
    ((KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.NO),),
    # Layer 2 (Raise): Brightness
    ((KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.NO),),
    # Layer 3 (Adjust): Mouse wheel
    ((KC.MW_UP, KC.MW_DOWN, KC.NO),),
]

# ============================================================================
# HOME ROW MODS (using HoldTap)
# ============================================================================

# Home row mods - Shift on F and J as requested
SFT_F = KC.HT(KC.F, KC.LSFT)  # F/Shift on left hand
SFT_J = KC.HT(KC.J, KC.RSFT)  # J/Shift on right hand

# Additional home row mods for advanced usage
CTL_A = KC.HT(KC.A, KC.LCTL)  # A/Control
ALT_S = KC.HT(KC.S, KC.LALT)  # S/Alt
GUI_D = KC.HT(KC.D, KC.LGUI)  # D/Gui

GUI_K = KC.HT(KC.K, KC.RGUI)  # K/Gui
ALT_L = KC.HT(KC.L, KC.RALT)  # L/Alt
CTL_SC = KC.HT(KC.SCLN, KC.RCTL)  # ;/Control

# ============================================================================
# MACROS
# ============================================================================

# Example macros using simple_key_sequence
# CUSTOMIZE: Replace with your own email address
MACRO_EMAIL = simple_key_sequence([
    KC.MACRO_SLEEP_MS(10),
    KC.H, KC.E, KC.L, KC.L, KC.O,
    KC.LSFT(KC.N2),  # @
    KC.E, KC.X, KC.A, KC.M, KC.P, KC.L, KC.E,
    KC.DOT, KC.C, KC.O, KC.M
])

MACRO_ARROW = simple_key_sequence([
    KC.MINUS, KC.LSFT(KC.DOT)  # ->
])

MACRO_FAT_ARROW = simple_key_sequence([
    KC.EQL, KC.LSFT(KC.DOT)  # =>
])

# ============================================================================
# COMBOS
# ============================================================================

# Define some useful combos
combos.combos = [
    # ESC combo (Q + W)
    Chord((KC.Q, KC.W), KC.ESC),
    # Tab combo (W + E)
    Chord((KC.W, KC.E), KC.TAB),
    # Enter combo (O + P)
    Chord((KC.O, KC.P), KC.ENTER),
    # Backspace combo (I + O)
    Chord((KC.I, KC.O), KC.BSPC),
    # Delete combo (U + I)
    Chord((KC.U, KC.I), KC.DEL),
    # Screenshot combo (Left Ctrl + Shift + S on same time)
    Chord((KC.LCTL, KC.LSFT, KC.S), KC.LCTL(KC.LSFT(KC.S))),
]

# ============================================================================
# KEYMAP
# ============================================================================

# Layer definitions
BASE = 0
LOWER = 1
RAISE = 2
ADJUST = 3

# Define layer toggles and momentary switches
LOWER_MO = KC.MO(LOWER)
RAISE_MO = KC.MO(RAISE)
ADJUST_MO = KC.MO(ADJUST)

# Default Lulu/Lily58 keymap with home row mods and macros
keyboard.keymap = [
    # ============================================================================
    # Layer 0: BASE (QWERTY) - 58 keys
    # ============================================================================
    [
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                          KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.MINS,
        KC.ESC,   CTL_A,    ALT_S,    GUI_D,    SFT_F,    KC.G,                                           KC.H,     SFT_J,    GUI_K,    ALT_L,    CTL_SC,   KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.LBRC,                    KC.RBRC,  KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                                      KC.LALT,  LOWER_MO, KC.SPC,   KC.ENT,                     KC.ENT,   KC.SPC,   RAISE_MO, KC.RALT,
    ],
    
    # ============================================================================
    # Layer 1: LOWER (Numbers, Symbols, Navigation)
    # ============================================================================
    [
        KC.TILD,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                        KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.DEL,
        KC.TRNS,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                          KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.UNDS,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                                          KC.LEFT,  KC.DOWN,  KC.UP,    KC.RGHT,  KC.NO,    KC.PIPE,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.TRNS,                    KC.TRNS,  KC.HOME,  KC.PGDN,  KC.PGUP,  KC.END,   KC.NO,    KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                    KC.TRNS,  ADJUST_MO,KC.TRNS,  KC.TRNS,
    ],
    
    # ============================================================================
    # Layer 2: RAISE (Function keys, Symbols)
    # ============================================================================
    [
        KC.F12,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                          KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        KC.TRNS,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                        KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PLUS,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                                          KC.MINS,  KC.EQL,   KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.GRV,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.TRNS,                    KC.TRNS,  KC.UNDS,  KC.PLUS,  KC.LCBR,  KC.RCBR,  KC.PIPE,  KC.TRNS,
                                      KC.TRNS,  ADJUST_MO,KC.TRNS,  KC.TRNS,                    KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
    ],
    
    # ============================================================================
    # Layer 3: ADJUST (RGB, Media, System)
    # ============================================================================
    [
        KC.RESET, KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                                          KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                                          KC.RGB_TOG,KC.RGB_HUI,KC.RGB_SAI,KC.RGB_VAI,KC.RGB_ANI,KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                                          KC.RGB_M_P,KC.RGB_HUD,KC.RGB_SAD,KC.RGB_VAD,KC.RGB_AND,KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                      KC.NO,    KC.RGB_M_B,KC.RGB_M_R,KC.RGB_M_BR,KC.RGB_M_K,KC.RGB_M_S,KC.NO,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                    KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
    ],
]

# ============================================================================
# START KEYBOARD
# ============================================================================

if __name__ == '__main__':
    print("Keyboard initialization complete - starting main loop")
    keyboard.go()
