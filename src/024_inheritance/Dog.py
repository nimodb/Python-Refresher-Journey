from Animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Inherit from Animal
        self.can_shed = False  # bool
    
    def talk(self):
        print("Bark!")
    
    def eat(self):  # Overrides Animal's eat()
        print("Dog eating.")
    

    # Inherits all Animal attributes and methods