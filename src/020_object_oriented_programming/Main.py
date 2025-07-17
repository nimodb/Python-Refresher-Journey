from Dog import Dog
from Enemy import Enemy

# Create a Dog object
dog = Dog()
# Access the dog's state (attributes)
print(f"Legs: {dog.legs}")
print(f"Ears: {dog.ears}")
print(f"Type: {dog.type}")
print(f"Age: {dog.age}")
print(f"Color: {dog.color}")
# Call the dog's behaviors (methods)
dog.bark()
dog.run()


# Create a Zombie enemy
enemy = Enemy(type_of_enemy="Zombie")
# Show enemy details
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can deal {enemy.attack_damage} attack damage.")