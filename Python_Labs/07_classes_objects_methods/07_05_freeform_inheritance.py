'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Shoe:
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
    def __str__(self):
        return f"This shoe is {self.color} colored, size {self.size}, and it's brand is {self.brand}."

class Hiking_shoe(Shoe):
    def __init__(self, brand, color, size, difficulty):
        super().__init__(brand, color, size)
        self.difficulty = difficulty
    def __str__(self):
        return f"This hiking shoe is {self.color} colored, size {self.size}, it's brand is {self.brand}, and it is used for {self.difficulty} hikes"
class Tennis_shoe(Shoe):
    def __init__(self, brand, color, size, type):
        super().__init__(brand, color, size)
        self.type = type
    def __str__(self):
        return f"This tennis shoe is {self.color} colored, size {self.size}, it's brand is {self.brand}, and it is a {self.type} shoe."

regular_shoe = Shoe("Puma", "red", 8)
print(regular_shoe)

hiking_shoe = Hiking_shoe("Patagonia", "brown", 12, "Advanced")
print(hiking_shoe)

tennis_shoe = Tennis_shoe("Nike", "white", 20, "Grass-Court")
print(tennis_shoe)

