from Enemy import Enemy

# Create a Zombie enemy
zombie = Enemy()

# Set the private type_of_enemy using the setter
zombie.set_type_of_enemy("Zombie")

# Get the private type_of_enemy using the getter
print(f"Enemy type: {zombie.get_type_of_enemy()}")

# Use enemy methods
zombie.talk()
zombie.walk_forward()
zombie.attack()

# Try to access public attributes directly
print(f"Health: {zombie.health_points}, Damage: {zombie.attack_damage}")

# Try to access private attribute directly (will raise an error)
# print(zombie.__type_of_enemy)  # AttributeError