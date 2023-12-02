# SuperClass for all entities in the game.
class Entity:
    def __init__(self, name, race, profession, health, strength, defense):
        self.name = name
        self.race = race
        self.profession = profession
        self.health_points = health
        self.strength = strength
        self.defense = defense
