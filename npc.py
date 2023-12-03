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
        player.name = input('\33[0m'"Answer: "'\33[35m')













# Create an instance of Brewswig
brewswig = Brewswig()