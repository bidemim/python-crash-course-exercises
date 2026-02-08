from pathlib import Path

username = input("Please enter your first and last name: ")
path = Path('guest.txt')
path.write_text(username)
