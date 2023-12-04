import start_menu
import utility
import dialogue
from character_creation import CharacterCreation
from npc import *
from player import *

def initiliaze():
    utility.clear()
    start_menu.interact()
    start_game()

def start_game():
    utility.clear()
    # Create an instance of the Player Class
    player_instance = Player("", "", "", 0, 0, 0)
    dialogue.opening_scene()
    character_creation(player_instance)

def character_creation(player):
    create_character = CharacterCreation()
    create_character.tell_me_your_name(player)
    utility.clear()
    create_character.tell_me_your_race(player)
    utility.clear()
    create_character.tell_me_your_specialty(player)

    input("Press enter to see your character results!")
    utility.test_character_creation(player)


# Test colour
print("\n\n")
test = "The following text is a text to test the colour code. Brewswig the Innkeeper:\n" \
       "So your a -race- who goes by the name -Name?. Well met friend.\n" \
       "Here... another ale as promised.\n"
utility.test_colour(test)


# Start Program
#initiliaze()

