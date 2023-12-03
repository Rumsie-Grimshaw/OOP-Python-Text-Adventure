import utility
from npc import Brewswig

def opening_scene():
    utility.draw_long()
    print("You have travelled for many days and nights, finally arriving at the grand oaken building that stands")
    print("before you. A wooden sign hangs from the balcony above a set of finely crafted wooden doors. It reads:")
    utility.green_text()
    print("                                 ╔══════════════════════════════╗                                          ")
    print("                                 ║──────────────────────────────║                                          ")
    print("                                 ║───The─Snarling─Warg─Tavern───║                                          ")
    print("                                 ║──────────────────────────────║                                          ")
    print("                                 ╚══════════════════════════════╝                                          ")
    utility.white_text()
    print("As you pull on the door handles, you are greeted with the warmth of a blazing hearth, and the sweet smell")
    print("of ale.")
    print("")
    print("The tavern appears to be empty, save for one man who seems to be occupied with cleaning fine glass mug as")
    print("he hums to himself. He notices you as you step through the doorway and head towards the bar... ")
    print("")
    utility.green_text()
    utility.press_enter_to_continue()

def brewswig_greet_player(player):
    print('\33[32m'"Brewswig the Innkeeper:"'\33[32m')
    print(f"Greetings {player.name} the {player.race}!")

def brewswig_tell_me_your_name():
    utility.clear()
    print('\33[32m'"Brewswig the Innkeeper:"'\33[32m')
    utility.gold_text()
    print("\"Well 'ello there adventurer! Allow me to introduce myself.\""'\33[0m')
    print("\nHe places the freshly cleaned glass mug in front of you, and proudly throws the cleaning rag over his")
    print("shoulder; clearing his throat as he does so.")
    utility.gold_text()
    print("**Ahem!**")
    print("\n\"The names Brewswig, an' this fine den ye find yeself in this even'in is none other than the ")
    print('\33[35m'"The Snarling Warg Tavern\33[33m.\"")
    print("\"Sit down, make yourself at 'ome. I'll fetch ye a pint. You look like ye been on the road for a while.\"")
    utility.white_text()
    print("Taking the glass mug in front of you; Brewswig turns toward a oaken barrel resting on a shelf next to him.")
    print("The foamy ale quickly fills the glass mug, and once filled; Brewswig places it down in front of you.")
    utility.gold_text()
    print("\"There ya go, this ones on the house. So... ah... what did you say your name was?\"\n")
    utility.purple_text()

def brewswig_query_name(player):
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print(f"\"\33[35m{player.name}\33[33m, eh? Strange name.. None too common in these parts.\"\n")
    print(f"\"You did say \33[35m{player.name},\33[33m right?\"")
    print("")

def brewswig_no_name_given():
    print('\33[32m'"Brewswig the Innkeeper:'\33[33m'")
    print("Look, i've been in the business a long time; and my gut tells me that ain't your name.")
    print("I got plenty of glasses to clean while I wait for you to give me a proper answer."'\33[32m')
    print()


def brewswig_incorrect_name():
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print("\"I did think that was a strange name... My apologies, I don't hear quite so well these days.\"")
    print("\n\"What did you say your name was again?\"")
    utility.purple_text()

def brewswig_tell_me_your_race(player):
    utility.clear()
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print(f"\"Well I must say it is nice to meet you \33[35m{player.name}\33[33m. It's been a while since someone new "
          f"and interesting came through\n those doors.\"")

    utility.white_text()
    print("\33[35mBrewswig\33[0m chuckles to himself before removing a clean glass mug from underneath the bar and "
          "turns to the same barrel \nhe had filled yours from, producing a nice foamy ale; that he quickly gulps "
          "down.\n")
    print("**Gulp...Gulp...Gulp\n")
    print("He wipes the foam stuck to his bushy mustache with a satisfied look on his face.\n"
          "Smiling once more, he turns to you.\n")

    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print(f"\"So\33[35m {player.name}\33[33m, while we're gettin to know each other, how 'bout tellin me a little bit "
          f"about yourself?\"\n")
    print("\"I must say, with all that adventuring gear on, I can't tell where you hail from?\"\n")
    print("\"Are you from the \33[35mHuman\33[33m settlements to the North?\"")
    print("\"Or maybe the \33[35mElven\33[33m forests to the West?\"")
    print("\"Perhaps you come from the grand underground kingdom of the \33[35mDwarves\33[33m to the East?\"\33[32m")
    print()
    utility.press_enter_to_continue()
    utility.clear()

def choose_race_options():
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print("\"Tell me of your home and kin... theres another ale in it for you!!\""'\33[32m\n')
    print("\33[31mChoose your Race:")
    print("\33[36m--Available Races--\33[32m\n")
    print("[a] Human:\33[0m\n"
          "While not especially unique, Humans are well rounded and effective adventurers:")

    print("HP:25,  STR: 10,  DEF: 10\n"'\33[32m')

    print("[b] Elf:\33[0m\nAncient and generally peaceful people, what they lack in strength, "
          "they make up in speed.")
    print("HP:20,  STR: 5,  DEF: 10\n"'\33[32m')

    print("[c] Dwarf\33[0m:\nProud and stubborn folk, though their size limits their speed,they are fierce warriors.")
    print("HP:30,  STR: 15,  DEF: 10\n"'\33[32m')









