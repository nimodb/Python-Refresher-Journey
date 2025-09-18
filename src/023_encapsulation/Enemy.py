class Enemy:
    def __init__(self):
        self.__type_of_enemy = ""  # Private attribute
        self.health_points = 10    # Public attribute
        self.attack_damage = 1     # Public attribute

    # Getter method for type_of_enemy
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    # Setter method for type_of_enemy
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")