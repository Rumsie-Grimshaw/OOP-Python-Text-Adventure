import character_creation
import start_menu
import entities
from npc import *

run_program = False

def initiliaze():
    utility.clear()
    menu_select = start_menu.interact()
    if menu_select == "1":
        start_game()
    elif menu_select == "2":
        print("The adventure continues")

def start_game():
    utility.clear()
    dialogue.opening_scene()
    # Create an instance of the Player Class
    player = entities.Player()
    player_instance = character_creation.create_character(player)
    input("Press enter to see your character results!")
    utility.test_character_creation(player_instance)
    utility.save_game(player)

def continue_game():
    pass


# Start Program
initiliaze()


