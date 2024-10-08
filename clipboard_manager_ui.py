import tkinter as tk
import pyperclip
from pynput.keyboard import Controller, Key

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
        self.history_listbox.bind('<<ListboxSelect>>', self.copy_selected)

        # Bind to hide the window when it loses focus
        self.window.bind("<FocusOut>", self.hide_ui)

        # Create a keyboard controller to simulate paste action
        self.keyboard_controller = Controller()

    def update_history(self):
        """Update the clipboard history list in the UI."""
        self.history_listbox.delete(0, tk.END)  # Clear the listbox

        # Populate the listbox with the latest clipboard history
        for item in self.clipboard_manager.clipboard_history:
            self.history_listbox.insert(tk.END, item)

        # Call this method every 1000ms to refresh the listbox with history
        self.window.after(1000, self.update_history)

    def show_ui(self):
        """Show the Tkinter window with the clipboard history."""
        self.update_history()  # Update the window before showing the history
        self.window.deiconify()
        self.window.lift()  # Bring the window in front of other windows

    def hide_ui(self, event=None):
        """Hide the Tkinter window when it loses focus."""
        self.window.withdraw()  # Hide the window

    def copy_selected(self, event=None):
        """Copy the selected item from the listbox to the clipboard."""
        selected_index = self.history_listbox.curselection()
        if selected_index:
            selected_item = self.history_listbox.get(selected_index)
            pyperclip.copy(selected_item)  # Copy the selected item to clipboard
            print(f"Copied to clipboard: {selected_item}")
            self.hide_ui()

    def simulate_paste(self):
        """Simulate the Cmd + V (or Ctrl + V) paste action."""
        with self.keyboard_controller.pressed(Key.cmd if self.window.tk.call('tk', 'windowingsystem') == 'aqua' else Key.ctrl):
            self.keyboard_controller.press('v')
            self.keyboard_controller.release('v')

    def start(self):
        """Start the Tkinter main loop."""
        self.window.mainloop()
