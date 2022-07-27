class Item:  # creating a class called Item which containes some methodes and attreputes and we can create instances(objects) of it as many as we want

    pay_rate = 0.08  # here we are ceating a class attribute which means it is the class level not in instance level(instance attribute)
    all = []  # here we are ceating a class attribute which simply represents a list

    # note __init__ methode (function) is called every time we creata a new instance
    # the prameter (self) means each instance we create is passed as a prameter to the metode
    def __init__(self, name: str, price: float, quantity: int):
        # if we want to make sure that price and quantity is grater that 0 we use assert comand which returens an assertion error is the
        assert price >= 0, f"price {price} is not greater or equal to Zero"
        assert quantity >= 0, f"quantity {quantity} is nit greater or equal to Zero"

        # creating an attreputes for instance (self) and give them the arguments passed to the methode(__init__)
        self.name = name
        self.price = price
        self.quantity = quantity

        # here we are using the class instance all to store all the insetences and ther attributes
        Item.all.append(self)

        # creating a methode that calculates the total price of each item we created

    def Total_price(self):
        return self.price * self.quantity  # note here we are passing the instance it self as an argument to the method this means we can use any attreputes related to the instansces

    # creating a method that applyes a descoubt
    def apply_discount(self):
        self.price = self.price - self.price * self.pay_rate  # note althoudh the attribute pay_rate is a class attribute we stil mange to accesse it from instance level

    # here we are using __repr__() function to print the instance in a cleaner way as we want
    def __repr__(self):
        return f"Item{self.name},{self.price},{self.quantity},"

    @classmethod
    def __repr(cls):
        return f"Item{self.name},{self.price},{self.quantity},"
    # ------------------------------------------------------------------------------


item1 = Item('phone', 1000, 3)  # creating an instance called item1
item2 = Item('laptob', 4000, 2)  # creating an instance called item2
item3 = Item('watch', 500, 10)  # creating an instance called item3
item4 = Item('head phone', 200, 13)  # creating an instance called item4
# ------------------------------------------------------------------------------
""" 
print (f"Name: {item1.name}")          # printing the value of attribute name related to instance item1
print (f"Price:{item1.price}")         # printing the value of attribute price related to instance item2
print (f"quantity:{item1.quantity}")   # printing the value of attribute quantity related to instance item3
"""
# ------------------------------------------------------------------------------
"""
print ("The Total price of item1 is:" ,item1.Total_price ())   # note that Total_price methode resives the inctance we called it with as an aregument
print ("The Total price of item2 is:" ,item2.Total_price ())   # note that Total_price methode resives the inctance we called it with as an aregument   
print ("The Total price of item3 is:" ,item3.Total_price ())   # note that Total_price methode resives the inctance we called it with as an aregument
"""
# ------------------------------------------------------------------------------
"""
#here we are using the apply_discount methode to apply a discount to item1
item1.apply_discount()      
print (f"New Price: {item1.price}")
"""
# ------------------------------------------------------------------------------

# here we are printing the names of each instance stored in all metode
for aal_instances in Item.all:
    print(aal_instances.name)

# ------------------------------------------------------------------------------
"""
print (Item.pay_rate)    # accessing the class attribute from class level
print (item1.pay_rate)   # accessing the class attribute from instance level through item1
print (item3.pay_rate)   # accessing the class attribute from instance level through item3
"""
# -------------------------------------------------------------------------------

# to get all the attributes we use a puilt in attribute called (__dict__)
print(Item.__dict__)  #
print(item1.__dict__)  # note dict is abbreviation dictionary this means the return is the attributes and thir values in form of dictionary
print(item3.__dict__)  #
