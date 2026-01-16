# code from 7-5
question = input('\nHow old are you? ')
age = int(question)
while True:
    if age < 3:
        print('You got a free ticket.')
    elif age <= 12:
        print('Your ticket is $10')
    elif age >= 13:
        print('Your ticket is $15')
    else:
        if age == 'quit':
            break

# creating an infinite loop
x = 1
while x <= 5:
    print(x)
