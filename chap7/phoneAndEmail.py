#! pyhton3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboard


import pyperclip
import re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?    # area code, group[1]
    (\s|-|\.)?            # separator
    (\d{3})               # first 3 digits, group[3]
    (\s|-|\.)?            # seperator
    (\d{4})               # last 4 digits, group[5]
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # the host part
    @                     # what else to say
    [a-zA-Z0-9.-]+        # for the domain
    (\.[a-zA-Z]{2,4})     # dot somethin
    )''', re.VERBOSE)

clipText = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(clipText):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(clipText):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phoneNum numbers of email addresse found.')
