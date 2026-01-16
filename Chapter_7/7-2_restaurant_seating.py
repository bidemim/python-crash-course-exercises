# ask how many guests are in the group
message = input('Hello, may I ask how many people are in your dinner group? ')
message = int(message)

if message >= 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready, please follow me.')