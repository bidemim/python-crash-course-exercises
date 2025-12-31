# check if number is a multipe of ten 
number = input('Give me a number: ')
number = int(number)

if number % 10 == 0:
    print(f'{number} is a multipe of ten.')
    
else:
    print(f'{number} is not a multipe of ten.')