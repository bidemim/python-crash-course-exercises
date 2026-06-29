from city_function import get_city_and_country

print("Enter 'e' anytime to exit.")

while True:
    city = input("\nPlease enter city name: ")
    if city == 'e':
        break

    country = input("Please enter the country: ")
    if country == 'e':
        break

    population = input("Please enter the city's population: ")
    if population == 'e':
        break
    elif population == "usa" or "uk" or "uae":
        population.capitalize()

    city_country = get_city_and_country(city, country, population)
    print(f"\tCity and Country name: {city_country}")