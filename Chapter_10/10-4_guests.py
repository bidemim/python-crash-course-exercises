from pathlib import Path

username = input("Please enter your first and last name: ")
path = Path('txt_files/guest.txt')
path.write_text(username)
