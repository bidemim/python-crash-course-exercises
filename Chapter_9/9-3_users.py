class User:
    # representing details about users
    def __init__(self, first_name, last_name, location, age):
        # initialize user attributes
        self.name = first_name + ' ' + last_name
      #  self.name = last_name
        self.location = location
        self.age = age    
    # describe and summarize information about user
    def describe_user(self):
        print(f'\nUser details: \n- {self.name} \n- {self.location} \n- {self.age}')
    # greet user
    def greet_user(self):
        print(f'Hello, {self.name}')

user_1 = User('Harry', 'Potter', 'London', 11)
user_2 = User('Hermione', 'Granger', 'London', 12)
user_3 = User('Ronald', 'Weasley', 'Countryside', 12)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()