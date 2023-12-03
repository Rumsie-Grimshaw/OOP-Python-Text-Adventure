import start_menu
import utility
import dialogue
from npc import *
from player import *

def initiliaze():
    start_menu.interact()
    start_game()

def start_game():
    utility.clear()
    # Create an instance of the Player Class
    player_instance = Player("", "", "", 0, 0, 0)
    dialogue.opening_scene()
    character_creation(player_instance)

def character_creation(player):
    brewswig.tell_me_your_name()
    player.name = player.get_player_name()
    player.race = player.get_player_race()
    utility.clear()
    print(f"{player.name}, {player.race}")


# Start Program
initiliaze()