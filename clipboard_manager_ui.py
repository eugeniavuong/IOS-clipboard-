import tkinter as tk
import pyperclip
from pynput.keyboard import Controller, Key

#Build my own component here, which takes in the clipboard 

class ClipboardManagerUI:
    def __init__(self, clipboard_manager):
        """Initialize the UI and set up the Tkinter window."""
        self.clipboard_manager = clipboard_manager
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Clipboard Manager")
        self.window.withdraw()  # Initially hide the window

        # Create a Listbox to display clipboard history
        self.history_listbox = tk.Listbox(self.window, height=10, width=40)
        self.history_listbox.pack(pady=10)

        # Bind selection event to automatically copy and paste the selected item
        self.history_listbox.bind('<<ListboxSelect>>', self.copy_and_paste_selected)

        # Bind to hide the window when it loses focus
        self.window.bind("<FocusOut>", self.hide_ui)

        # Create a keyboard controller to simulate paste action
        self.keyboard_controller = Controller()


    
    def update_history(self):
        print("Updating listbox")
        self.history_listbox.delete(0, tk.END) # clear the listbox

        # Populate the listbox with the latest clipboard history
        for item in self.clipboard_monitor.clipboard_history:
            self.history_listbox.insert(tk.END, item)
        
        # Call this method every 1000ms to refresh listbox with history
        self.master.after(1000, self.update_listbox)
    
    def show_ui(self):
        """Show the Tkinter window theclipboard hsitory"""
        self.update_history() #update the window before showing the history
        self.window.deiconify()
        self.window.lift() # bring this in front of other windows

    def hide_ui(self, event=None):
        """Hide the Tkinter window when it loses focus """
        self.window.withdraw() # hide the window 

    def copy_and_paste_selected(self, event=None):
        """Copy the selected item from the listbox to the clipboard and automatically paste"""
        selected_index = self.history_listbox.curselection()
        if selected_index:
            selected_item = self.history_listbox.get(selected_index)
            pyperclip.copy(selected_item)
            print("copied to clipboard")
            self.hide_ui()
            self.simulate_paste()
    
    def simulate_paste(self):
        """Simulate the cmd +V and paste: macOS-> cmd + v linus/windows-> ctrl + v"""
        with self.keyboard_controller.pressed(Key.cmd if self.window.tk.call('tk', 'windowingsystem') == 'aqua'else Key.ctrl):
            self.keyboard_controller.press('v')
            self.keyboard_controller.release('v')

    def start(self):
        """Start the tkinter mainloop"""
        self.window.mainloop()





    