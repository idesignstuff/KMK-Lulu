# KMK Firmware for Boardsource Lulu SMT RP2040

Best-in-class KMK firmware configuration for the Boardsource Lulu split keyboard with full hardware support.

## 🎯 Features

This firmware implementation includes all modern keyboard features:

- ✅ **Split Keyboard Support**: Full UART communication between halves with auto-detection
- ✅ **Rotary Encoders**: Both left and right encoders fully functional
- ✅ **Per-Key RGB**: WS2812B addressable RGB LEDs with multiple animation modes
- ✅ **Home Row Mods**: Shift on F and J with configurable tap timing
- ✅ **HoldTap**: Dual-function keys (tap for one key, hold for modifier)
- ✅ **Combos**: Multiple key combinations for shortcuts
- ✅ **Macros**: Pre-defined macros and easy macro creation
- ✅ **4 Layers**: Base, Lower, Raise, and Adjust layers
- ✅ **Default Keymap**: Standard Lulu/Lily58 layout

## 🎹 Keyboard Specifications

- **MCU**: RP2040 (Raspberry Pi Pico)
- **Layout**: 58-key split (6 rows × 5 columns per side)
- **Encoders**: 2 (one per side)
- **RGB LEDs**: 58 per-key WS2812B (29 per side)
- **Communication**: UART over TRRS cable
- **Firmware**: KMK (CircuitPython-based)

## 📋 Prerequisites

### Required Hardware
1. Boardsource Lulu SMT RP2040 keyboard (both halves)
2. USB-C cable
3. TRRS cable (for split communication)

### Required Software
1. **CircuitPython 9.x or later** - Download from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/)
2. **KMK Firmware** - Download from [KMK GitHub](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip)
3. **Adafruit NeoPixel Library** - Part of [Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)

## 🚀 Installation

### Step 1: Install CircuitPython

1. **Download CircuitPython UF2 file** for RP2040:
   - Visit: https://circuitpython.org/board/raspberry_pi_pico/
   - Download the latest stable release (9.x or later)

2. **Flash LEFT half**:
   - Hold the BOOT button on the left half while plugging in USB
   - The board will appear as `RPI-RP2` drive
   - Copy the `.uf2` file to the drive
   - The board will reboot and appear as `CIRCUITPY`

3. **Rename LEFT drive to end with 'L'**:
   - Create a file named `settings.toml` on the drive
   - Add: `USB_DISK_LABEL="LULUL"`
   - Safely eject and reconnect

4. **Flash RIGHT half**:
   - Repeat steps for the right half
   - Rename to end with 'R': `USB_DISK_LABEL="LULUR"`

### Step 2: Install KMK Firmware

1. **Download KMK**:
   ```bash
   wget https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip
   unzip main.zip
   ```

2. **Copy KMK to both halves**:
   - Copy the `kmk/` folder to the root of both LULUL and LULUR drives
   - Copy `boot.py` to the root of both drives

### Step 3: Install Required Libraries

1. **Download Adafruit CircuitPython Bundle**:
   - Visit: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
   - Download the bundle matching your CircuitPython version (9.x)

2. **Extract and copy libraries**:
   - Extract the zip file
   - Create a `lib/` folder on both keyboard halves
   - Copy `neopixel.mpy` from the bundle to both `lib/` folders

### Step 4: Install This Firmware

Copy these files to **both** keyboard halves:
- `main.py` - Main firmware configuration
- `kb.py` - Hardware definitions
- `boot.py` - Boot configuration

## 🎮 Keymap

### Base Layer (Layer 0)
```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│  `  │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │ BSP │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ TAB │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │  -  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │ A/^ │ S/⎇ │ D/⌘ │ F/⇧ │  G  │                    │  H  │ J/⇧ │ K/⌘ │ L/⎇ │ ;/^ │  '  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐    ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ SFT │  Z  │  X  │  C  │  V  │  B  │  [  │    │  ]  │  N  │  M  │  ,  │  .  │  /  │ SFT │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤    ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │ CTL │ GUI │LOWER│ SPC │    │ ENT │ SPC │RAISE│ ALT │
                  └─────┴─────┴─────┴─────┘    └─────┴─────┴─────┴─────┘
```

**Home Row Mods**:
- `A` - Tap: A, Hold: Left Control
- `S` - Tap: S, Hold: Left Alt
- `D` - Tap: D, Hold: Left GUI (Windows/Command)
- `F` - Tap: F, Hold: Left Shift ⭐
- `J` - Tap: J, Hold: Right Shift ⭐
- `K` - Tap: K, Hold: Right GUI
- `L` - Tap: L, Hold: Right Alt
- `;` - Tap: ;, Hold: Right Control

### Lower Layer (Layer 1)
Navigation, symbols, and numbers access
```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│  ~  │  !  │  @  │  #  │  $  │  %  │                    │  ^  │  &  │  *  │  (  │  )  │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │  _  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │  ←  │  ↓  │  ↑  │  →  │     │  |  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐    ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │     │    │     │ HOME│PGDN │PGUP │ END │     │     │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤    ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │     │     │█████│     │    │     │     │ ADJ │     │
                  └─────┴─────┴─────┴─────┘    └─────┴─────┴─────┴─────┘
```

### Raise Layer (Layer 2)
Function keys and symbols
```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│ F12 │ F1  │ F2  │ F3  │ F4  │ F5  │                    │ F6  │ F7  │ F8  │ F9  │ F10 │ F11 │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  !  │  @  │  #  │  $  │  %  │                    │  ^  │  &  │  *  │  (  │  )  │  +  │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │  -  │  =  │  [  │  ]  │  \  │  `  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐    ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │     │    │     │  _  │  +  │  {  │  }  │  |  │     │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤    ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │     │     │ ADJ │     │    │     │     │█████│     │
                  └─────┴─────┴─────┴─────┘    └─────┴─────┴─────┴─────┘
```

### Adjust Layer (Layer 3)
RGB controls, media keys, and system functions
```
┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
│RESET│     │     │     │     │     │                    │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │ TOG │ HU+ │ SA+ │ VA+ │ AN+ │     │
├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │                    │PLAIN│ HU- │ SA- │ VA- │ AN- │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┐    ┌─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │     │    │     │BREAT│RAINB│ BR+R│KNGHT│SWIRL│     │
└─────┴─────┴─────┼─────┼─────┼─────┼─────┤    ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
                  │     │     │█████│     │    │     │     │█████│     │
                  └─────┴─────┴─────┴─────┘    └─────┴─────┴─────┴─────┘
```

## 🎨 RGB Controls

### RGB Keycodes (available on Adjust layer)
- `RGB_TOG` - Toggle RGB on/off
- `RGB_HUI` / `RGB_HUD` - Increase/Decrease Hue
- `RGB_SAI` / `RGB_SAD` - Increase/Decrease Saturation
- `RGB_VAI` / `RGB_VAD` - Increase/Decrease Brightness
- `RGB_ANI` / `RGB_AND` - Increase/Decrease Animation Speed
- `RGB_M_P` - Static color mode
- `RGB_M_B` - Breathing animation
- `RGB_M_R` - Rainbow animation
- `RGB_M_BR` - Breathing rainbow
- `RGB_M_K` - Knight Rider animation
- `RGB_M_S` - Swirl animation

## 🎛️ Rotary Encoders

### Encoder Functions by Layer
- **Base Layer**: Volume control (CCW: Vol Down, CW: Vol Up, Press: Mute)
- **Lower Layer**: Undo/Redo (CCW: Undo, CW: Redo)
- **Raise Layer**: Brightness (CCW: Dim, CW: Brighten)
- **Adjust Layer**: Mouse Wheel (CCW: Scroll Up, CW: Scroll Down)

## 🤝 Combos

Pre-configured key combinations:
- `Q + W` → ESC
- `W + E` → TAB
- `O + P` → ENTER
- `I + O` → BACKSPACE
- `U + I` → DELETE
- `Ctrl + Shift + S` → Screenshot combo

## 🔧 Customization

### Changing the Keymap
Edit `main.py` and modify the `keyboard.keymap` array. Each layer is defined as a list of keycodes.

### Adding Custom Macros
Use `simple_key_sequence` to create macros:
```python
MY_MACRO = simple_key_sequence([
    KC.H, KC.E, KC.L, KC.L, KC.O
])
```

### Adjusting Home Row Mod Timing
In `main.py`, modify:
```python
holdtap.tap_time = 200  # milliseconds
```

### Customizing RGB
Modify RGB settings in `main.py`:
```python
rgb = RGB(
    val_limit=150,  # Max brightness (0-255)
    hue_default=100,  # Starting hue
    animation_mode=AnimationModes.BREATHING,
)
```

### Adding More Combos
Add to the `combos.combos` list:
```python
Chord((KC.J, KC.K), KC.ESC),  # J+K = ESC
```

## 🐛 Troubleshooting

### Keyboard not recognized
- Ensure CircuitPython is properly installed
- Check that `boot.py` is present on both halves
- Verify USB-HID is enabled in `boot.py`

### Split halves not communicating
- Check TRRS cable connection
- Verify `data_pin` and `data_pin2` are correct in `kb.py`
- Ensure both halves are named correctly (ending with L and R)

### RGB not working
- Verify `neopixel.mpy` is in the `lib/` folder
- Check `rgb_pixel_pin` matches your hardware (GP29 for Lulu)
- Reduce `val_limit` if LEDs are unstable

### Encoders not responding
- Verify encoder pins in `kb.py` match your hardware
- Check encoder wiring (A, B, and GND)
- Try reversing encoder direction with the 4th parameter

### Home row mods too sensitive
- Increase `holdtap.tap_time` in `main.py`
- Consider using `prefer_hold=False` for specific keys

## 📚 Resources

- [KMK Documentation](https://github.com/KMKfw/kmk_firmware/tree/master/docs)
- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Boardsource Lulu Info](https://www.boardsource.xyz/products/Lulu)
- [QMK to KMK Keycode Reference](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md)

## 🤖 Contributing

Issues and pull requests are welcome! Please follow these guidelines:
1. Test changes on actual hardware before submitting
2. Follow existing code style and comments
3. Update documentation for any feature changes
4. Keep commits focused and well-described

## 📄 License

This firmware configuration is provided as-is for the Boardsource Lulu keyboard. 
KMK firmware is licensed under the GPL v3. CircuitPython is licensed under the MIT license.

## 🙏 Acknowledgments

- [KMK Firmware Team](https://github.com/KMKfw/kmk_firmware)
- [Boardsource](https://www.boardsource.xyz/)
- CircuitPython and Adafruit teams
- The mechanical keyboard community

---

**Enjoy your fully-featured Boardsource Lulu keyboard!** 🎉

For questions or support, please open an issue on GitHub.