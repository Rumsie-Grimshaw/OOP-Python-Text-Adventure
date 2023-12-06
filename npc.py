import dialogue
import utility
import player

class Brewswig:
    def __init__(self):
        pass

    def greet_player(self, player):
        print('\33[32m'"Brewswig the Innkeeper:"'\33[32m')
        print(f"Greetings {player.name} the {player.race}!")


# Create an instance of Brewswig
brewswig = Brewswig()