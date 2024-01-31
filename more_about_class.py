# OOPS, more about class in Python

class Dog:
    leg_count = 4
    
    def __init__(self, name) -> None:
        self.name = name
    
    def method_one(self):
        print(f"instance method of {self.name}")
    
    @staticmethod
    def method_two():
        print("This is static method")
    
    @classmethod
    def method_three(self):
        print(f"This is class method, {self.__name__} has {self.leg_count} legs")

Dog.method_three()
Dog.method_two()

my_dog = Dog("Popo")
my_dog.method_one()