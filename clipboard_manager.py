import pyperclip
from pynput import keyboard
import time
import threading
import tkinter as tk
import tkinter.simpledialog #for userinput
import tkinter.messagebox



class ClipboardManager:
    def __init__(self, max_items = 10):
        self.clipboard_history = []
        self.max_items = max_items   
        self.lock = threading.Lock()

    def clipboard_monitor(self):
        recent_val = ""

        # while true 
        while True:
            with self.lock:
                #get the current content of the clipboard 
                current_val = pyperclip.paste()
                
                #if the recent copied item is not empty
                if current_val != recent_val and current_val != "":
                    recent_val = current_val
                    self.add_to_history(recent_val)

                # Sleep for a short time to reduce CPU usage
                time.sleep(1)

    def add_to_history(self, current_val):
        """Add new item to clipboard hisotry and maintain max history to 10"""
        if(len(self.clipboard_history)> self.max_items):
            self.clipboard_history.pop(0) # remove the oldest item 
        self.clipboard_history.append(current_val)



        


