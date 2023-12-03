import dialogue
import utility

class Brewswig:
    def __init__(self):
        pass

    def greet_player(self):
        dialogue.brewswig_greet_player()

    def tell_me_your_name(self, player):
        correct_name = False
        dialogue.brewswig_tell_me_your_name()
        player.name = input('\33[0m'"Answer: "'\33[35m')
        utility.clear()
        while not correct_name:
            if player.name == "":
                utility.clear()
                dialogue.brewswig_no_name_given()
                player.name = input('\33[0m'"Answer: "'\33[35m')
                continue
            dialogue.brewswig_query_name(player)
            print('\33[32m'"1) Agree     2) Disagree"'\33[35m')
            print()
            answer = input('\33[0m'"Answer: "'\33[35m')
            if answer == "1":
                correct_name = True
            else:
                utility.clear()
                dialogue.brewswig_incorrect_name()
                print()
                player.name = input('\33[0m'"Answer: "'\33[35m')
                utility.clear()
                continue

        utility.clear()
        return player.name

    def tell_me_your_race(self, player):
        correct_race = False
        dialogue.brewswig_tell_me_your_race(player)
        dialogue.choose_race_options()
        while not correct_race:
            race = input('\33[0m'"Answer: "'\33[35m').lower()
            if race == "h":
                player.race = "Human"
                player.health = 25
                player.strength = 10
                player.defense = 10

            elif race == "e":
                player.race = "Elf"
                player.health = 20
                player.strength = 5
                player.defense = 10

            elif race == "d":
                player.race = "Dwarf"
                player.health = 30
                player.strength = 15
                player.defense = 10

            else:
                print("\n\33[31mInvalid Selection: Please try again\n")
                continue














# Create an instance of Brewswig
brewswig = Brewswig()