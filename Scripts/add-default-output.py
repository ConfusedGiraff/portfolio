import pyautogui as pya
import pyperclip
import re
import time 

title = pyperclip.paste() # sets title equal to the clipboard contents
time.sleep(.01) 
default_out = re.sub('[^0-9a-zA-Z\-]', '', title.strip().lower().replace(' ', '-')) + '.dita' # formats the title into a default output path
time.sleep(.01)
pya.hotkey('tab') 
pya.hotkey('tab')
pya.hotkey('tab') # tabs down to the default output path box
time.sleep(3)
pyperclip.copy(default_out) # stores the new default output path on the clipboard