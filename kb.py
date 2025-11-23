"""
Boardsource Lulu SMT RP2040 Keyboard Definition
Hardware configuration for the Lulu split keyboard
"""
import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    """
    Boardsource Lulu keyboard configuration
    - 58 keys total (29 per side)
    - 6 rows x 5 columns per side
    - 2 rotary encoders (1 per side)
    - Per-key RGB LEDs (58 total)
    """
    
    def __init__(self):
        super().__init__()
        
        # Lulu has 6 rows and 5 columns per side
        # Left half pin configuration
        self.col_pins = (
            board.GP28,
            board.GP27,
            board.GP26,
            board.GP22,
            board.GP20,
        )
        
        self.row_pins = (
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
            board.GP8,
            board.GP9,
        )
        
        # Lulu uses COL2ROW diode orientation
        self.diode_orientation = DiodeOrientation.COL2ROW
        
        # Create matrix scanner
        self.matrix = MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            columns_to_anodes=self.diode_orientation,
            interval=0.02,
            max_events=64
        )
        
        # RGB LED configuration
        # Lulu has 58 per-key RGB LEDs (29 per side)
        self.rgb_pixel_pin = board.GP29
        self.rgb_num_pixels = 29  # Per side
        
        # Encoder pins for left side
        # The right side will be handled by the split module
        self.encoder_pin_a = board.GP16
        self.encoder_pin_b = board.GP17
        self.encoder_button = board.GP18
        
        # Split keyboard UART pins for communication
        self.data_pin = board.GP1  # TX
        self.data_pin2 = board.GP0  # RX


# Coordinate mapping for the Lulu keyboard
# This maps physical key positions to matrix positions
# The Lulu has 58 keys arranged in a split layout
# Using standard matrix layout (6 rows x 5 columns per side)
coord_mapping = []
