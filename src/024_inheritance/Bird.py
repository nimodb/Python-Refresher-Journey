from Animal import Animal

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.bird_type = ""  # str

    def talk(self):
        print("Chirp!")

    def fly(self):
        print("Bird begins to soar!")

    # Inherits all Animal attributes and methods