# class or object in Python
# Python is Object Oriented Programming language

# class is a 'blueprint' for creating objects, everything
# in python is part of some class

my_str = "this is a string"
my_num = 22.7 #float

def sum_two(num1, num2):
    return num1 + num2

print(type(my_str))
print(type(my_num))
print(type(sum_two))

# syntax:
# class <class_name>:
#   <class_property_1>
#   <class_property_2>
#   <class_property_3> ... etc.
#   def <method_1>:
#       <logic>

class Pokemon:
    legs_count = 4 # property
    
    def __init__(self, name):
        self.name = name 
        self.attacks = {
            "atk_0" : 10,
            "atk_1" : 28,
            "special" : 69
        }
        self.health = 100
    
    def attack(self, atk_key):
        return self.attacks[atk_key]
    
    def damage(self, dmg_value):
        self.health -= dmg_value
    
    def check_health(self):
        print(self.health)

pichu = Pokemon("pichu")

print(pichu.legs_count)
print(pichu.name)

mew = Pokemon("mew")

print(mew.name)
print(pichu.name)

mew.check_health()
my_attack = pichu.attack('atk_0')
mew.damage(my_attack)
mew.check_health()




