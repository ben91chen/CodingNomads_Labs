'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed=0):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed += 5

    def __str__(self):
        return f"This car is a {self.year} {self.model} with a max speed of {self.max_speed} mph."

my_car = Car("Toyota", "2010", 100)
dream_car = Car("Acura", "2021", 130)
print(my_car)
my_car.accelerate()
print(my_car)
print(dream_car)