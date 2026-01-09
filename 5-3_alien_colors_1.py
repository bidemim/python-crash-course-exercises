alien_color = ['green', 'yellow', 'red']
target_colors = ['green', 'pink']

for color in alien_color:
    if color in target_colors:
        print(f'{color}: You just earned 5 points!')
    else:
        print(f'{color}: No points earned.')
