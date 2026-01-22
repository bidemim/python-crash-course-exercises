def car_details(make, model, **car_info):
    # information about cars
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car_profile = car_details('honda', 'CRV',
                          drive='AWD', year=2020)
print(car_profile)