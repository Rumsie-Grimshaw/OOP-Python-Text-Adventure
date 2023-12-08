import character_creation
import start_menu
import entities
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
    player = entities.Player()
    player_instance = character_creation.create_character(player)
    input("Press enter to see your character results!")
    utility.test_character_creation(player_instance)


# Start Program
initiliaze()


