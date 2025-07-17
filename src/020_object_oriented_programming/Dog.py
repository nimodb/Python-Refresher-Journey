class Dog:
    def __init__(self):
        self.legs: int = 4
        self.ears: int = 2
        self.type: str = 'GoldenDoodle'
        self.age: int = 5
        self.color: str = 'Yellow'

    def bark(self) -> None:
        print("Woof! Woof!")

    def run(self) -> None:
        print("The dog is running!")