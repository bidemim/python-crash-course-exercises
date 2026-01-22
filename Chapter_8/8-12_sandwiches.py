def sandwich_fillings(*fillings):
    if len(fillings) > 1:
        print(f'\nYou requested these with your sandwich:')
    else:
        print(f'\nYou requested this with your sandwich:')
    for filling in fillings:
        print(f'- {filling}')

sandwich_fillings('cabbage')
sandwich_fillings('cabbages', 'tomatoes', 'peanut butter')
sandwich_fillings('strawberry jam', 'peanut butter', 'sesame seed', 'butter')
