import random
from abc import ABC
# SuperClass for all entities in the game.
class Entity(ABC):
    def __init__(self):
        def attack(self):
            pass

# Class for the player properties and methods
# Construct the Player object.
# Construct properties and methods from Entity.
class Player(Entity):
    def __init__(self, name='', race='', profession='', weapon='', max_health=0, health=0, strength=0, defense=0,
                 gold=0, health_potion=0):
        super().__init__()

        self.name = name
        self.race = race
        self.profession = profession
        self.weapon = weapon
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.defense = defense
        self.gold = gold
        self.health_potion = health_potion

        self.tutorial_quest = False

        def attack(self):
            damage = random.randint(1, 10)
            damage_total = self.strength + damage
            pass

class Enemy(Entity):
    def __init__(self, name='', race='', profession='', weapon='', max_health=0, health=0, strength=0, defense=0,
                 gold=0, health_potion=0):
        super().__init__()


bubbles_the_cow = Enemy("Bubbles", "Cow", "Grazer", "Horns", 30, 30, 12, 0, 0, 0)