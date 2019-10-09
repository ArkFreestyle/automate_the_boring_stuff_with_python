import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code - It's either 3 digits or 3 digits within brackets
    (\s|-|\.)?                      # separator - Get space, hyphen or period
    (\d{3})                         # first three digits - Get three digits
    (\s|-|\.)                       # separator - Get space, hyphen or period
    (\d{4})                         # last four digits - Get four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - any number of spaces + ext or x or ext. + two to five digits
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username - Get lowercase, uppercase, numbers, dot, underscore, percent, plus, minus or hyphen
    @                  # @ symbol 
    [a-zA-Z0-9.-]+     # domain name - lowercase, uppercase, numbers or period or hyphen
    (\.[a-zA-Z]{2,4})  # dot-something - .com or .anything basically (top-level domain) between two to four characters
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found.')
