'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet:
    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"Planet {self.name} is {self.color} and is in the {self.system} system."


earth = Planet("Earth", "blue", "Solar")
mars = Planet("Mars", "red", "Solar")
neptune = Planet("Neptune", "blue", "Solar")
print(earth)
print(mars)
print(neptune)
print(mars.name)
