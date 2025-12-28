life_stage = 3

if life_stage > 2:
    stage = 'infant'
elif 2 > life_stage < 4:
    stage = 'toddler'
elif 4 >= life_stage < 13:
    stage = 'kid'


print(f'You are a(n) {stage}')