print("\nPlease enter your pizza toppings:")
print("(Enter 'quit' when you are finished.)")

while True:
    topping = input()

    if topping == 'quit':
        break
    else:
        print(f"\nI'll add that to your pizza.")