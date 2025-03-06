def main():

    mickey_ds = Restaurant("fast food", "n American")
    kfc = Restaurant("fried chicken", "n American")
    taco_bell = Restaurant("mexican food", "n American")

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

    def __init__(self, r_type, c_type):
        self.r_type = r_type
        self.c_type = c_type

    def describe_restaurant(self):
        print(f"This restaurant is a{self.c_type} {self.r_type} place.")
    def open_restaurant(self):
        print("This restuarant is open!")

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"This user's first name is {self.first_name}, their last name is {self.last_name}")
    def greet_user(self):
        print(f"Wassup {self.first_name} {self.last_name}, welcome")
        

main()