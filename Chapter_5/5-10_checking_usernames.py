current_users = ['abbott', 'jane',  'buddy', 'anthony', 'alex']
new_users = ['buddy', 'judy', 'mary', 'anthony', 'joe']

for user in new_users:
    new_users = [name.lower() for name in new_users]
    current_users = [name.lower() for name in current_users]
    if user in current_users:
        print('You will need a new username.')
    else:
        print(f'{user.title()} is available.')
