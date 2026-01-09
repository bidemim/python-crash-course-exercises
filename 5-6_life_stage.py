life_stage = 130

if life_stage < 2:
    stage = 'infant'
elif life_stage < 4:
    stage = 'toddler'
elif life_stage < 13:
    stage = 'kid'
elif life_stage < 20:
    stage = 'teenager'
elif life_stage < 65:
    stage = 'adult'
else:
    stage = 'senior'
print(f'You are at the {stage} stage.')