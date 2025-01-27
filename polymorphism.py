# Base class: Animal
class Animal:
    def move(self):
        pass

# Derived class: Bird
class Bird(Animal):
    def move(self):
        return "Flying 🐦"

# Derived class: Fish
class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Derived class: Dog
class Dog(Animal):
    def move(self):
        return "Running 🐕"

# Example usage
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    print(animal.move())

