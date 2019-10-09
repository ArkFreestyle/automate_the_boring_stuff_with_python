"""Returns list to the clipboard with bullet points added (for wikipedia articles)"""

import pyperclip

# Returns all text on the clipboard as one big string
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

print("Bulleted list has been copied to clipboard, paste to see it!")