# Python OOPS concepts
# Object-oriented programming (OOP) is a method of 
# structuring a program by bundling related properties 
# and behaviors into individual objects.

class Pet:
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(f"{self.name} said: ", end="")

# Python Inheritance
class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def call(self):
        super().call()
        print("bark")

my_dog = Dog("Scooby")
my_dog.call()

# Function Polymorphism
# len() is a built in function with Polymorphism
print(len("length of this string")) # len on str
print(len([1, 'list', 22.7, True])) # len on list


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def call(self):
        super().call()
        print("mew")

class Rabbit(Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def call(self):
        super().call()
        print("...")

my_dog = Dog("Scooby")
my_cat = Cat("Tom")
my_rabbit = Rabbit("Pichu")

my_dog.call()
my_cat.call()
my_rabbit.call()

for x in (my_dog, my_cat, my_rabbit):
    x.call()