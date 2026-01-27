sandwich_orders = ['toast', 'avocado', 'bologna', 'turkey', 'pastrami', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f'I made your {made_sandwich.title()} sandwich.')
    finished_sandwiches.append(made_sandwich)
print('\nThe following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')  