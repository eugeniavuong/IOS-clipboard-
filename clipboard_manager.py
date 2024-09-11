import pyperclip
from pynput import keyboard
import time
import threading
import tkinter as tk 
from tkinter import simpledialog 

# monitor clipboard 
# use ctl + C I want to add this to the clipboard and have it as the most recent in the list/ DB
#there should be a limit to the number of items stored 
clipboard_history = []
CLIPBOARD_LIMIT = 10
COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl_l, keyboard.KeyCode(char = 'v')}

current_keys = set() # Tracking thr current keys pressed 

def clipboard_monitor():
    recent_val = ""

    # while true 
    while True:
        #get the current content of the clipboard 
        current_val = pyperclip.paste()
        
         #if the recent copied item is not empty
        if current_val != recent_val:
           recent_val = current_val
           clipboard_history.append(recent_val)
           print(f"The lastest value in your clipboard is : {recent_val}")

        if(len(clipboard_history)> CLIPBOARD_LIMIT):
            clipboard_history.pop(0)

        # Sleep for a short time to reduce CPU usage
        time.sleep(0.5)

def on_press(key):
    """Detect when the key combination is pressed to show the clipboard"""
    current_keys.add(key)

    if all(k in current_keys for k in COMBINATION):
        print("print clipboard history")
        for i, item in enumerate(clipboard_history, 1):
            print(f"{i}: {item}")

def on_release(key):
    """Remove key from the current keys sent on release"""
    try:
        current_keys.remove(key)
    except KeyError:
        pass



if __name__ == "__main__":
    # Start the clipboard monitoring in a separate thread
    clipboard_thread = threading.Thread(target=clipboard_monitor, daemon=True)
    clipboard_thread.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()