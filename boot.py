"""
Boot configuration for Boardsource Lulu KMK Firmware
This file runs before main.py and configures the USB device
"""
import supervisor
import board
import storage
import usb_cdc
import usb_hid

# Disable auto-reload to prevent issues during development
supervisor.set_next_code_file(None, reload_on_error=True)

# Enable USB HID (required for keyboard functionality)
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     usb_hid.Device.CONSUMER_CONTROL)
)

# Enable USB CDC (serial console) for debugging
usb_cdc.enable(console=True, data=True)

# Make the filesystem read-only when connected via USB
# This protects against accidental file modifications
# To make it writable again, comment out the line below
storage.remount("/", readonly=False)
