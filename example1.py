"""
9-1.
Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

9-2.
Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance

"""


class Restaurent:
    number_served = 0

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the restaurant name is:{self.restaurant_name}")
        print(f"the cuisine type is:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    @staticmethod
    def set_number_served(num_ser):
        Restaurent.number_served = num_ser

    def increment_number_served(self, in_num_ser):
        Restaurent.number_served = self.number_served + in_num_ser


# __________________________


class user:
    login_attempts = 0

    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        return f"Name:{self.first_name}{self.last_name} \n "

    def greet_user(self):
        print(f"hi! {self.first_name}{self.last_name}")

    @staticmethod
    def increment_login_attempts():
        user.login_attempts = user.login_attempts + 1

    @staticmethod
    def reset_login_attempts():
        user.login_attempts = 0



"""
Restaurent_1 = Restaurent("Sterio","Italian")
Restaurent_2 = Restaurent("Desoke","Eguption")
Restaurent_3 = Restaurent("mack","amirican")


Restaurent_1.describe_restaurant()
Restaurent_2.describe_restaurant()
Restaurent_3.describe_restaurant() 
Restaurent_1.open_restaurant()
Restaurent_2.open_restaurant()
Restaurent_3.open_restaurant() 
"""

restaurent = Restaurent("Bafalo", "Amirican")
restaurent.set_number_served(10)
restaurent.increment_number_served(5)
print(Restaurent.number_served)
