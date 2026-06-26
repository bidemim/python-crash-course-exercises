from city_function import get_city_and_country

print("Enter 'e' anytime to exit.")

while True:
    city = input("\nPlease enter city name: ")
    if city == 'e':
        break

    country = input("Please enter the country: ")
    if country == 'e':
        break

    city_country = get_city_and_country(city, country)
    print(f"\tCity and Country name: {city_country}")