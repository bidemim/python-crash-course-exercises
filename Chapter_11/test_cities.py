from city_function import get_city_and_country

def test_city_country_name():
    """Would a city like 'Santiago, Chile' work?'"""
    city_country = get_city_and_country("santiago", "chile")
    assert city_country == "Santiago, Chile"