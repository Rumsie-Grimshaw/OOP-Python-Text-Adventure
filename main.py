import utility
import dialogue
from npc import *
from player import *

def start_game():
    # Create an instance of the Player Class
    player_instance = Player("", "", "", 0, 0, 0)
    dialogue.opening_scene()
    character_creation(player_instance)




def character_creation(player):
    brewswig.tell_me_your_name()
    player.name = player.get_player_name()
    print(brewswig.greet_player(player.name))
    utility.clear()
    player.race = player.get_player_race()
    utility.clear()
    print(f"{player.name}, {player.race}")


# Start Game
start_game()