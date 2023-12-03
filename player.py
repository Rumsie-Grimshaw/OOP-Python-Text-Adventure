from entities import Entity

# Class for the player properties and methods
# Construct the Player object.
# Construct properties and methods from Entity.
class Player(Entity):
    def __init__(self, name, race, profession, health, strength, defense):
        super().__init__(name, race, profession, health, strength, defense)


    def get_player_name(self):
        valid_name = False
        while not valid_name:
            name = input('\33[32m'"Input your name: "'\33[0m')
            print("")
            if name != "":
                return name
            else:
                print("Thats okay. I have plenty more glasses to clean until your ready to talk.\n")

    def get_player_race_human(self, player):
            player.race = "Human"
            player.health = 25
            player.strength = 10
            player.defense = 10
            return player.race, player.health, player.strength, player.defense

    def get_player_race_elf(self, player):
            player.race = "Elf"
            player.health = 20
            player.strength = 5
            player.defense = 10
            return player.race, player.health, player.strength, player.defense

    def get_player_race_dwarf(self, player):
            player.race = "Dwarf"
            player.health = 30
            player.strength = 15
            player.defense = 10
            return player.race, player.health, player.strength, player.defense


