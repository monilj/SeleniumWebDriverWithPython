"""
Object Oriented Programming
"""


class Car(object):

    def __init__(self, make, model="550i"):
        self.make = make
        self.model = model


c1 = Car('bmw')
print(c1.make)
print(c1.model)

c2 = Car('benz')
print(c2.make)
print(c2.model)

"""
Some more Object Oriented Programming 
"""


class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = Car('bmw', '550i')
print(c1.make)
# c1.info()

c2 = Car('benz', 'E350')
print(c2.make)
# c2.info()

print(Car.wheels)

"""
Object Oriented Programming - Inheritance
"""


class Car(object):
    print("Code for Method Inheritance")

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()

"""
Object Oriented Programming - Method Overriding
"""


class Car(object):
    print("Code for Method Overriding")

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        super(BMW, self).drive()
        print("You are driving a BMW, Enjoy...")

    def headsup_display(self):
        print("This is a unique feature")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
b.headsup_display()
