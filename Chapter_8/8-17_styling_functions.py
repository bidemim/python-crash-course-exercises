# rewriting functions to confirm with pep8 standards

# example 1 from 8-4_large_shirts.py
def make_shirt(message, size='large'):
# function that takes a message to be printed on a shirt and the shirt size.
# the shirt size has a 'large' default value.
    print(f'I wear a {size} size tshirt, I want it to say: "{message}".\n')
make_shirt('I love Python.')
make_shirt('I love Python.', 'medium')
make_shirt('Go hiking!', 'small')

# example 2 from 8-5_cities.py
def describe_city(city, country='Mali'):
# describe_city mention cities in a country, with a default value of 'Mali'.
    print(f'{city.title()} is a city in {country.title()}.\n')
describe_city('bamako')
describe_city('timbuktu')
# city not in country
describe_city('abuja', 'nigeria')

# example  from 8-14_cars.py
def car_details(make, model, **car_info):
# car_details takes information about cars. the make and model must be supplied
# with an arbitrary number of details following.
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car_profile = car_details('honda', 'CRV',
                          drive='AWD', year=2020)
print(car_profile)
