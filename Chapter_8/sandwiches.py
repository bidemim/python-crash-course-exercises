# code copied from 8-12_sandwiches.py
# using this file as a module that would be imported in 8-16_imports.py
def sandwich_fillings(*fillings):
    if len(fillings) > 1:
        print(f'\nYou requested these with your sandwich:')
    else:
        print(f'\nYou requested this with your sandwich:')
    for filling in fillings:
        print(f'- {filling}')

