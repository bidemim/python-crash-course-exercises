class Restaurant:
    # modeling a restaurant
    def __init__(self, restaurant_name, cuisine_type):
    # Initialize name and cuisine type
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        # describes the type of restaurant 
        print(f'{self.name} is a {self.type} restaurant.')
    def open_restaurant(self):
        # confirm that restaurant is open
        print(f'{self.name} is open.')

# instance 1    
haitian_restaurant = Restaurant('Carribean Spice', 'Haitian')
print(f"The {haitian_restaurant.name} restaurant serves {haitian_restaurant.type} food.")
haitian_restaurant.describe_restaurant()
haitian_restaurant.open_restaurant()

# instance 2
chinese_restaurant = Restaurant('Panda Noodles', 'Chinese')
print(f'The {chinese_restaurant.name} serves {chinese_restaurant.type} food.')
chinese_restaurant.describe_restaurant()

# instance 3
nigerian_restaurant = Restaurant('Pepper Shakers', 'Nigerian')
print(f'The {nigerian_restaurant.name} serves {nigerian_restaurant.type} food.')
nigerian_restaurant.describe_restaurant()