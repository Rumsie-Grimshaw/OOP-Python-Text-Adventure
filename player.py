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

    def get_player_race(self):
        player_races = ["Human", "Dwarf", "Elf"]
        print("Select your Race")

        race = None
        choice = input("").lower()
        if choice == "h":
            return player_races[0]
        if choice == "d":
            return player_races[1]
        if choice == "e":
            return player_races[2]



