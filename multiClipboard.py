# Multiclipboard.py save <keyword> - save clipboard to keyword.
# Multiclipboard.py <keyword> - loads keyword to clipboard.
# Multiclipboard.py list - loads all keywords to clipboard.

import pyperclip
import shelve
import sys

file = shelve.open('mbc')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    file[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(file.keys())))
elif len(sys.argv) == 2 and sys.argv[1] in file:
    pyperclip.copy(str(list(file[sys.argv[1]])))

file.close()
