fav_numbers = {
    'Alto': [22, 12, 3, 78],
    'Tracy': [17, 77, 89, 14],
    'Tola': [4, 10, 16, 8],
    'Juma': [1, 3, 5, 7],
    'June': [9, 81, 27, 63],
}
print(f'Your favorite numbers are:')
for index, (name, number) in enumerate(fav_numbers.items(), start=1):
    print(f'{index}. {name}: {number}')