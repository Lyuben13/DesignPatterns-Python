import copy

# Abstract Prototype
class AnimalPrototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete Prototype: Dog
class Dog(AnimalPrototype):
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"

# Concrete Prototype: Cat
class Cat(AnimalPrototype):
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __str__(self):
        return f"Cat: {self.name}, Breed: {self.breed}"

# Testing the Prototype Pattern
def main():
    original_dog = Dog("Golden Retriever", "Buddy")
    cloned_dog = original_dog.clone()

    original_cat = Cat("Persian", "Whiskers")
    cloned_cat = original_cat.clone()

    print(f"Original Dog: {original_dog}")
    print(f"Cloned Dog: {cloned_dog}")

    print(f"Original Cat: {original_cat}")
    print(f"Cloned Cat: {cloned_cat}")

main()
