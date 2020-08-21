"""
This is our own module which does not exist in python builtins
"""
import math
from math import sqrt


def info(make, model):
    print("Make of the car: " + make)
    print("Model of the car: " + model)


"""
https://docs.python.org/3/library/
"""
# Please refer import statement available in the beginning of the class

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))


m = ModulesDemo()
m.builtin_modules()


# Please refer import statement available in the beginning of the class
class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()
