from Dog import Dog
from Bird import Bird

# Create a Dog object
dog = Dog()
dog.eat()   # Outputs: Dog eating.
dog.sleep() # Outputs: Animal sleeping.
dog.talk()  # Outputs: Bark!

# Create a Bird object
bird = Bird()
bird.animal_typ = "Bird" # Inherited attribute
bird.bird_type = "Eagle" # Bird's own attribute

# Use inherited methods
bird.eat()   # Outputs: Animal eating.
bird.sleep() # Outputs: Animal sleeping.

# Use Bird's own methods
bird.talk()  # Outputs: Chirp!
bird.fly()   # Outputs: Bird begins to soar!