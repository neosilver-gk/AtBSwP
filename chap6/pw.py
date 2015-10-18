#! python
#pw.py - A insecure password locker

import sys
import pyperclip

passwords = {'email': 'test_email_password',
        'blog': 'test_blog_password',
        'luggage': 'password_for_luggage_test'}

if len(sys.argv) < 2:
    print('Usage: pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('No password for ' + str(account) + ' is saved!')

