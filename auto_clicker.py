# Run this code to execute an auto clicker.

import pyautogui
import time
import keyboard

# Initialize click
click = False

def click_toggle():
    global click
    click = not click

keyboard.add_hotkey("F6", click_toggle)

# Set the clicks per second and exit key
exit_key = "esc"
# Set clicks per second
cps = 10 
interval = 1 / cps


time.sleep(3) # Delay 3 seconds

last_click_time = 0

while True:
    current_time = time.time()

    if click and (current_time - last_click_time) >= interval:
        pyautogui.doubleClick()
        last_click_time = current_time

    if keyboard.is_pressed(exit_key):
        break

    time.sleep(0.001)  # Tiny delay to reduce lag