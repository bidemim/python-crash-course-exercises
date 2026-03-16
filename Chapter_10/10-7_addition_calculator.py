# put the program in 10-6 into a while loop

# start with a while loop
def sum_of_numbers():
    print('Give me two numbers to add.')
    print("Press 'q' anytime to quit the program")
    
    # get input from user
    first_number = input('Enter a number:  ').strip()
    if first_number == 'q':
        return False
    second_number = input('Enter another number: ').strip()
    if second_number == 'q':
        return False
    # convert user input to integers 
    # now try catching the error
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print(f'You need to provide a number!')
    else:
        print(f'{result} is the sum of both numbers!')

while True:
    if not sum_of_numbers():
        continue