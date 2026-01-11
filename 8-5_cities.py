def describe_city(city, country='Mali'):
    print(f'{city.title()} is a city in {country.title()}.\n')

describe_city('bamako')
describe_city('timbuktu')
# city not in country
describe_city('abuja', 'nigeria')