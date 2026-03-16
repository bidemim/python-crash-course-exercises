# catch ValueErrors in a simple calculator

# now define a function that so the entire program is portable
def sum_of_numbers():
    print('Give me two numbers to add.')
    
    # get input from user
    first_number = input('Enter a number:  ')
    second_number = input('Enter another number: ')

    # convert user input to integers and try catching the valueerror
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print(f'You need to provide a number!')
    else:
        print(f'{result} is the sum of both numbers!')

sum_of_numbers()