question = input('\nHow old are you? ')
age = int(question)

if age < 3:
    print('You got a free ticket.')
elif age <= 12:
    print('Your ticket is $10')
else:
    print('Your ticket is $15')


