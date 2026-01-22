def make_shirt(shirt_size, message):

    print(f'I wear a {shirt_size} size tshirt. I want it to say: "{message}".\n')
   
# positional argument function call
make_shirt('large', 'welcome to a new dispensation')

# keyword argument funciton call
make_shirt(shirt_size='large', message='Go hiking!')