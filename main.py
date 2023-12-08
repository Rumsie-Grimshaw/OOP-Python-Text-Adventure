import character_creation
import start_menu
from npc import *

run_program = False

def initiliaze():
    utility.clear()
    start_menu.interact()
    start_game()

def start_game():
    utility.clear()
    dialogue.opening_scene()
    # Create an instance of the Player Class
    player_instance = character_creation.create_character(player)

# Start Program
initiliaze()


