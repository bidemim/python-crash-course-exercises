from pathlib import Path
usernames = ''
print("Please enter your first and last name (type 'q' to quit):")

while True:
    user_input = input('Enter your name: \n')
    if user_input.lower() == 'q':
        break
    usernames += f'{user_input.title()}\n'
# print(usernames)

path = Path('guest_book.txt')
path.write_text(usernames)