while True:
    print('What is your Name?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
