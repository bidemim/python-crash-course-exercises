usernames = ['happy', 'greg', 'titus', 'admin', 'fury']
for user in usernames:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for loggin in again.')