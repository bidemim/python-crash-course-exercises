def city_country(city, country):
    describe_city = f'"{city}, {country}"'
    return describe_city.title()


location  = city_country ('bamako', 'mali')
print(location)
location  = city_country('timbuktu', 'mali')
print(location)
location  = city_country('abuja', 'nigeria')
print(location)