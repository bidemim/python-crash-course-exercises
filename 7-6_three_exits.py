# original code
question = input('\nHow old are you? ')
age = int(question)

if age < 3:
    print('You got a free ticket.')
elif age <= 12:
    print('Your ticket is $10')
else:
    print('Your ticket is $15')

# modified code with three exits

question = input('\nHow old are you? ')
age = int(question)

while True:
    if age < 3:
        print('You got a free ticket.')
    elif age <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
        break

# assigning active = true
active = True
while active:
    question = input('\nHow old are you? ')
    age = int(question)

    if age < 3:
        print('You got a free ticket.')
    elif age <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
        active = False

# using a flag to exit the loop
while True:
    question = input('\nHow old are you? ')
    age = int(question)

    if age < 3:
        print('You got a free ticket.')
    elif age <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
        break


