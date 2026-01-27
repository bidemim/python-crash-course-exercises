sandwich_orders = ['pastrami', 'toast', 'avocado', 'pastrami', 'bologna', 'turkey', 'pastrami', 'tuna']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    if sandwich == 'pastrami':
        print(f'We have run out of {sandwich} sanwiches.')
    else:
        while sandwich_orders:
            made_sandwich = sandwich_orders.pop()
            print(f'I made your {made_sandwich.title()} sandwich.')
            finished_sandwiches.append(made_sandwich)
    print('\nThe following sandwiches have been made:')
    for sandwich in finished_sandwiches:
        print(f'- {sandwich}')  