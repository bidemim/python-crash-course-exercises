my_foods= ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('These are my favorite foods:')
for food in my_foods:
    print(f'{food.title()}')

print(f"These are my friend's favorite foods:")
for food in friend_foods:
     print(f'{food.title()}')
    
    

