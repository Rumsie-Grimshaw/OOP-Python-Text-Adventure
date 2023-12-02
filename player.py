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
            name = input("Input your name: ")
            print("")
            if name != "":
                return name
            else:
                print("Invalid name. Please try again.")
                print("")



    def get_player_race(self):
        player_races = ["Human", "Dwarf", "Elf"]
        print("Select your Race")

        race = None
        choice = input("").lower()
        if choice == "h":
            return player_races[0]



