

import pyperclip
import time
# monitor clipboard 
# use ctl + C I want to add this to the clipboard and have it as the most recent in the list/ DB
#there should be a limit to the number of items stored 
clipboard_history = []

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

        # Sleep for a short time to reduce CPU usage
        time.sleep(0.5)
    




#past command -> when I paste I want to be able to past the most recent item 

#shift + ctl + V
#seperate command to be able to select from the prviously copied items and paste the selected one

#interface to be able to select between different items 
#remove items 

if __name__ == "__main__":
    clipboard_monitor()
