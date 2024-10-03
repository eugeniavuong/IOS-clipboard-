import threading
import tkinter as tk 
from pynput import keyboard
from clipboard_manager import ClipboardManager
from clipboard_manager_ui import ClipboardManagerUI

# monitor clipboard 
# use ctl + C I want to add this to the clipboard and have it as the most recent in the list/ DB
#there should be a limit to the number of items stored 
COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl_l, keyboard.KeyCode(char = 'v')}
trigger_ui = False # a flag to trigger the UI to handle thread management of tkinter and pynput packages 


current_keys = set() # Tracking thr current keys pressed 

def start_clipboard_monitoring(clipboard_monitor):
    """Start the clipboard monitoring process in a seperate thread"""
    print("running clipboard monitor")
    monitor_thread = threading.Thread(target=clipboard_monitor.clipboard_monitor)
    monitor_thread.daemon = True
    monitor_thread.start()

def on_press(key, ui):
    """Detect when the key combination is pressed to show the clipboard"""

    if key in COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in COMBINATION):
            ui.window.after(0, ui.show_ui)
            

def on_release(key):
    """Remove key from the current keysent on release"""
    try: 
        current_keys.remove(key)
    except KeyError:
        pass

def start_key_listener(ui):
    """Start listening for the key combination in the main thread."""
    with keyboard.Listener(
        on_press=lambda key: on_press(key, ui),
        on_release=on_release
    ) as listener:
        listener.join()

def clipboard_monitor(clipboard_manager):
    """Start the clipbaord monitoring in the background"""
    clipboard_manager.clipboard_monitor()

if __name__ == "__main__":
    # Initialize the clipboard manager instance
    clipboard_manager = ClipboardManager()


    clipboard_ui = ClipboardManagerUI(clipboard_manager)

    # Start a clipboard monitor in a seperate  thread
    monitor_thread = threading.Thread(target=clipboard_manager.clipboard_monitor)
    monitor_thread.daemon = True  # Ensure thread exits when MAIN program exits
    monitor_thread.start()

    # Start the key listener in a background thread 
    listener_thread = threading.Thread(target=start_key_listener, args=(clipboard_ui,)) 
    listener_thread.daemon = True
    listener_thread.start()

    #Run the tkinter main loop 
    clipboard_ui.start()
