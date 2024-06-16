import pyperclip
import keyboard
import re
import tkinter as tk
from tkinter import simpledialog

# Function to map grid challenge
def map_grid_challenge(foo):
    grid_mapping = {
        "A1": "?", "A2": "?", "A3": "?", "A4": "?", "A5": "?",
        "B1": "?", "B2": "?", "B3": "?", "B4": "?", "B5": "?",
        "C1": "?", "C2": "?", "C3": "?", "C4": "?", "C5": "?",
        "D1": "?", "D2": "?", "D3": "?", "D4": "?", "D5": "?",
        "E1": "?", "E2": "?", "E3": "?", "E4": "?", "E5": "?",
        "F1": "?", "F2": "?", "F3": "?", "F4": "?", "F5": "?",
        "G1": "?", "G2": "?", "G3": "?", "G4": "?", "G5": "?",
        "H1": "?", "H2": "?", "H3": "?", "H4": "?", "H5": "?",
        "I1": "?", "I2": "?", "I3": "?", "I4": "?", "I5": "?",
        "J1": "?", "J2": "?", "J3": "?", "J4": "?", "J5": "?"
    }
    return grid_mapping.get(foo, "")

# Function to read UNMC page
def read_unmc_page():
    keyboard.send('ctrl+a')
    keyboard.send('ctrl+c')
    clipboard_content = pyperclip.paste()

    lines = clipboard_content.split('\n')
    for line in lines:
        needle_regex = r"\[([A-Z0-9]{2})\] \[([A-Z0-9]{2})\] \[([A-Z0-9]{2})\]"
        match = re.search(needle_regex, line)
        if match:
            first = match.group(1)
            second = match.group(2)
            third = match.group(3)

            new_first = map_grid_challenge(first)
            new_second = map_grid_challenge(second)
            new_third = map_grid_challenge(third)

            result = f"{new_first}{new_second}{new_third}"
            display_result(result)
            break

# Function to display the result in a GUI
def display_result(result):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    simpledialog.messagebox.showinfo("Result", result)
    root.destroy()

# Set hotkey
keyboard.add_hotkey('ctrl+alt+n', read_unmc_page)

# Start the event loop to listen for the hotkey
keyboard.wait('esc')
