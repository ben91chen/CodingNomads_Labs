'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Dog:
    def __init__(self, type, color, age):
        self.type = type
        self.color = color
        self.age = age
    def __str__(self):
        return f"This dog is a {self.age} year old, {self.color} {self.type}!"
    def __add__(self, other):
        if self.type == other.type:
            return self.type
        else:
            return f"{self.type}-{other.type} mix"

class Dog_food:
    def __init__(self, type, flavor, price):
        self.type = type
        self.flavor = flavor
        self.price = price
    def __str__(self):
        return f"This dog food is {self.type} food, {self.flavor} flavored, and is {self.price} compared to other dog foods!"

class Dog_toys:
    def __init__(self, type, color, size):
        self.type = type
        self.color = color
        self.size = size

    def __str__(self):
        return f"This dog toy is a {self.size}, {self.color} {self.type}."

my_dog = Dog("rottweiler", "black", 4)
your_dog = Dog("Vizsla", "brown", 3)
new_dog = Dog("Vizsla", "purple", 8)
dry_food = Dog_food("dry", "salmon", "cheap")
wet_food = Dog_food("wet", "chicken", "expensive")
my_dog_toy = Dog_toys("ball", "yellow", "small")
your_dog_toy = Dog_toys("dinosaur", "red", "big")

print(your_dog, my_dog)
#print(f"Total age of these dogs is {your_dog + my_dog} years")
print(f"These dogs combined is a {your_dog + new_dog}.")
print(dry_food, wet_food)
print(your_dog_toy, my_dog_toy)

