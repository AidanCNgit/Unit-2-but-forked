def main():

    mickey_ds = Restaurant("Mc Donalds", "American")
    kfc = Restaurant("Kentucky Fried Chicken", "Fried Chicken")
    taco_bell = Restaurant("Taco Bell", "Mexican")

    john = User("John", "Marton")
    franiselin = User("Franiselin", "James")
    riqui = User("Riqui", "Puig")

    mickey_ds.describe_restaurant()
    kfc.describe_restaurant()
    taco_bell.describe_restaurant()

    john.describe_user()
    john.greet_user()

    franiselin.describe_user()
    franiselin.greet_user()

    riqui.describe_user()
    riqui.greet_user()


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")
    def greet_user(self):
        print(f"Welcome {self.first_name}!")
        

main()