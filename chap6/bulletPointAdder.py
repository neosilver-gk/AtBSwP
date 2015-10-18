#! python
# bulletPointAdder.py - Add Bullets to WikiMarkup

import sys
import pyperclip

clipboard = pyperclip.paste()

list_of_clipboard = clipboard.split('\n')

for n in range(len(list_of_clipboard)):
    list_of_clipboard[n] = '* ' + list_of_clipboard[n]

text = '\n'.join(list_of_clipboard)

pyperclip.copy(text)
