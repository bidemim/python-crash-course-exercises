class Restaurant:
    # a class modeling a restaurant.
    def __init__(self, restaurant_name, cuisine_type):
    # Initialize name and cuisine type.
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        # describes the type of restaurant.
        print(f'{self.name} is a {self.type} restaurant.')
    def open_restaurant(self):
        # confirm that restaurant is open.
        print(f'{self.name} is open.')
    def set_number_served(self, number_served):
        # set the number of customers the restaurant has served.
        self.number_served += 
    def increment_number_served(self, ):
        # increment the number of customers who've been served.
    
restaurant = Restaurant('Carribean Spice', 'Haitian')
print(f"The {restaurant.name} restaurant serves {restaurant.type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
