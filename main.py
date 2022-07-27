class employee:
    raise_amunt = 0.08
    num_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{self.first}{self.last}@icloud.com"
        self.pay = pay
        employee.num_of_employee = employee.num_of_employee + 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_rais(self):
        self.pay = self.pay + self.pay * employee.raise_amunt

    @classmethod
    def get_num_of_employee(cls):
        return cls.num_of_employee


# inheritance mean that we inherit all the methods and attributes from the parent class to the child class
# we are using inheritance in order not to repeat the instances and methods that are common between more than one class DRY (Don't Repeat Yourself)
# DRY (Don't Repeat Yourself) DRY code means that we don't repeat the same code more than one time


# here we are inheriting a child class called [developers] from the parent class [employee]
class developers(employee):
    raise_amunt = 0.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # here we are using super()__init__() to copy all the attributes that we pass to it in order to achieve DRY
        self.prog_lang = prog_lang


# here we are inheriting a child class called engineers from the parent class employee
class engineers(employee):
    pass


# here we are inheriting a child class called mangers from the parent class employee
class mangers(employee):
    pass


emp_1 = engineers("Mohamed", "Eldeeb", 20000)
emp_2 = developers("Mustafa", "Eldeeb", 20000, "python")
print(emp_2.pay)
emp_2.apply_rais()
print(emp_2.pay)

"""
help(developers)   # help(developers) function gives us a 
print(emp_1.email)
print(emp_2.full_name())
emp_1.apply_rais()
emp_2.apply_rais()
print(employee.get_num_of_employee())
print(emp_1.pay)
print(emp_2.pay)
"""
