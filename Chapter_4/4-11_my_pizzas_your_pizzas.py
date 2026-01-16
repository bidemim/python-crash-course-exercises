my_pizzas = ['veggie', 'cheese', 'mushroom']

friends_pizza = my_pizzas[:]

my_pizzas.append('chicken')

friends_pizza.append('pineapple')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza.title())