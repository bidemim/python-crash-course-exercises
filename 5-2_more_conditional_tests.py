# equality & inequality tests with strings
print('book' == 'Book')
print('book' == 'Book'.lower())

# numerical tests
print(2 == 20/10)
print(10 >= 11)
print(14 <= 20)
print(14 > 49/9)
print(50 < 100/2)
print(13 != 15-2)

jollof_ingredients = ['rice', 'onion', 'bell pepper', 'sweet pepper', 'vegetable oil']
# and or test
print('oil' and 'onion' in jollof_ingredients)
print('oil' and 'onion' not in jollof_ingredients)
'oil' or 'bell pepper' in jollof_ingredients
'rice' or 'onion' not in jollof_ingredients

# list test
print('pepper' in jollof_ingredients)
print('onion' not in jollof_ingredients)
print('vege oil' not in jollof_ingredients)
print('sweet pepper' in jollof_ingredients)



