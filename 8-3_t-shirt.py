def make_shirt(size, message):

    print(f'I wear a {size} size tshirt. I want it to say: "{message}".\n')
   
# positional argument function call
make_shirt('large', 'welcome to a new dispensation')

# keyword argument funciton call
make_shirt(size='large', message='welcome to a new dispensation')