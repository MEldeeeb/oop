# here we are using __repr__() function to print the instance in a cleaner way as we want

class car:
    numcars = 0

    def __init__(self, prand, modle, price):
        self.prand = prand
        self.modle = modle
        self.price = price
        car.numcars = car.numcars + 1

    # __repr__() receives all the instances we created and put them in what ever the format that we want
    def __repr__(self):
        return f"car({self.prand},{self.modle},{self.price})"

    # note a class methode receives the class itself as the first argument, and it used when we need to deal with the class itself not a specific instance of it
    @classmethod
    def get_num_of_cars(cls):
        return cls.numcars

    # note a static methode receives any argument we want to pass as a first argument it works exactly like a normal function put it is related to the class it self
    # also static method know nothing about the class state
    @staticmethod
    def type_of_car(speed):  # here we  are deciding the type of the car according to it's top speed
        if speed <= 300:
            print("it is a family car")
        elif speed > 300 & speed <= 500:
            print("it is a sports car")
        else:
            return "it is a super sport car"


car_1 = car("BMW", "M3", 10000)
car_2 = car("Lambo", "Aventador", 1000000)
car_3 = car("maclarn", "P1", 90000000)

print(car)
print(car_1)
print(car_1.prand)
print(car_2.price)
print(car_3.modle)

car.get_num_of_cars()  # note here we don't want to deal with a specific attribute, but we want to deal with the class itself, so we used a class method
car.type_of_car(100)  #
car.type_of_car(400)
car.type_of_car(1000)

