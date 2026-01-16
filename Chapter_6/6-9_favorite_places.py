favorite_places = {
    'bukky': ['glacier np', 'chanel island', 'yosemite np'],
    'tola': ['balkans', 'rome', 'shangai'],
    'bob': ['banff np', 'glaciers np', 'olympic np'],
    'samuel': ['home'],
}

for name, places in favorite_places.items():
    if isinstance(places, str):
        print(f"{name.title()}'s favorite place is:")
        print(f'\t{places.title()}')
    else:  # assume list
        if len(places) == 1:
            print(f"{name.title()}'s favorite place is:")
        else:
            print(f"{name.title()}'s favorite places are:")
        for place in places:
            print(f'\t{place.title()}')
