def get_city_and_country(city, country, population=""):
    """Get city, country and population from user."""
    if population:
        city_details = f"{city.title()}, {country.title()} - Population {population}"
    elif population == "usa" or "uk" or "uae":
        population.capitalize()

    else:
        city_details = f"{city.title()}, {country.title()}"
    return city_details