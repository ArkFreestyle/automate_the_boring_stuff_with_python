"""Password retriever program"""

import sys
import pyperclip

PASSWORDS = {
    'email': 'test123',
    'blog': 'blog123',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print("Usage: python password_retriever.py [account] - copy account password")
    print("Account options:")
    for account in PASSWORDS:
        print(f"- {account}")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")

else:
    print("There is no account named " + account)
