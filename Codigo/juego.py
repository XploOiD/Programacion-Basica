import random

# Define the character class
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage.")
        enemy.take_damage(self.attack)
        print(f"{enemy.name} has {enemy.health} health left.")

# Define the player class
class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=10)

    def heal(self):
        heal_amount = random.randint(10, 30)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount}. Health is now {self.health}.")

# Define the enemy class
class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

# Game logic
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.attack_enemy(enemy)
        if enemy.is_alive():
            enemy.attack_enemy(player)
        print()  # Empty line for better readability

def main():
    print("Welcome to the RPG Game!")

    # Create player
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    # Create enemies
    enemies = [
        Enemy("Goblin", health=30, attack=5),
        Enemy("Orc", health=50, attack=7),
        Enemy("Dragon", health=80, attack=15)
    ]

    # Main game loop
    for enemy in enemies:
        print(f"A wild {enemy.name} appears!")
        battle(player, enemy)
        if not player.is_alive():
            print("You have been defeated. Game Over!")
            break
        else:
            print(f"You defeated the {enemy.name}!")
            player.heal()
            print()  # Empty line for better readability

    if player.is_alive():
        print("Congratulations! You have defeated all enemies!")

if __name__ == "__main__":
    main()