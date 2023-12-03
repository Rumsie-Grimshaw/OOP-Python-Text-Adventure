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
    brewswig.tell_me_your_name(player)
    utility.clear()
    brewswig.tell_me_your_race(player)
    utility.clear()
    input("Press enter to see the player.name and player.race results!")
    print(f"{player.name}, {player.race}")


# Start Program
initiliaze()