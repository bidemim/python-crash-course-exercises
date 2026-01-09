numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinals = {1: 'st', 2: 'nd', 3: 'rd'}

for number in numbers:
    suffix = ordinals.get(number, 'th')
    print(f'{number}{suffix}')
