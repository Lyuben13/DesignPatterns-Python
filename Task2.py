# Abstract Pasta Class
class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def prepare(self):
        print(f"Preparing {self.type} with {self.sauce} sauce, topped with {self.topping}, and {self.dressing} dressing.")

# Concrete Pasta Classes
class Spaghetti(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Spaghetti"
        self.sauce = "Marinara"
        self.topping = "Parmesan"
        self.dressing = "Basil"

class Penne(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Penne"
        self.sauce = "Alfredo"
        self.topping = "Chicken"
        self.dressing = "Parsley"

class Fettuccine(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Fettuccine"
        self.sauce = "Pesto"
        self.topping = "Shrimp"
        self.dressing = "Lemon Zest"

# Pasta Factory Class (Factory Method Pattern)
class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "spaghetti":
            return Spaghetti()
        elif pasta_type == "penne":
            return Penne()
        elif pasta_type == "fettuccine":
            return Fettuccine()
        else:
            raise ValueError("Unknown pasta type")

# Testing the Factory Pattern
def main():
    pasta_factory = PastaFactory()

    spaghetti = pasta_factory.create_pasta("spaghetti")
    spaghetti.prepare()

    penne = pasta_factory.create_pasta("penne")
    penne.prepare()

    fettuccine = pasta_factory.create_pasta("fettuccine")
    fettuccine.prepare()

main()
