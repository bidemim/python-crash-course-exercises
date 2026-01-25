class Restaurant:
    # a class modeling a restaurant
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
    
restaurant = Restaurant('Carribean Spice', 'Haitian')
print(f"The {restaurant.name} restaurant serves {restaurant.type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
