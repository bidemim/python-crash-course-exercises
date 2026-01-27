dream_vacation = {}
get_input = True
while get_input:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[name] = location
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        get_input = False
print("\n--- Dream Vacation Poll Results ---")
for name, location in dream_vacation.items():
    print(f"{name} would like to visit {location}.")