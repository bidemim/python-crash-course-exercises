questions = {
    "username": "What is your name? ",
    "favorite_number": "What is your favorite number? ",
    "favorite_color": "What is your best friend's name? "
    }

userdetails = {}

for key, question in questions.items():
    userdetails[key] = input(question)

print(userdetails)
