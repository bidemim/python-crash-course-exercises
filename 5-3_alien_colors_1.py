# version that passes the if test:
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print('You just earned 5 points!')

# version that fails the if test:
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'pink':
        print('You just earned 5 points!')
