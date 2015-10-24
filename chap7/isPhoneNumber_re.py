#!/bin/python3
#
# isPhoneNumber with regexes

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-555-4242. Please call me.')
print('Phone number found: ' + mo.group())
