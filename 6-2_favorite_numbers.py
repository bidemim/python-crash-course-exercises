fav_numbers = {
    'Alto': 22,
    'Tracy': 17,
    'Tola': 4,
    'Juma': 1,
    'June': 9,
}
print(f'Your favorite numbers are:')
for index, (name, number) in enumerate(fav_numbers.items(), start=1):
    print(f'{index}. {name}: {number}')