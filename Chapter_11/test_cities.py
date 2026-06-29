from city_function import get_city_and_country

def test_city_country_name():
    """Would a city like 'Santiago, Chile' work?'"""
    city_country = get_city_and_country("santiago", "chile")
    assert city_country == "Santiago, Chile"

def test_city_country_population_name():
    """Would details like 'New York, USA, 7 million work?'"""
    city_country = get_city_and_country("new york", 'usa', '7 million')
    assert city_country == "New York, USA, 7 million"