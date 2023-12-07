import player
import utility
from npc import Brewswig


def opening_scene():
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
    print("he hums to himself. He notices you as you step through the doorway and head towards the bar... \n")
    utility.press_enter_to_continue()


def brewswig_greet_player(player):
    print('\33[32m'"Brewswig the Innkeeper:"'\33[32m')
    print(f"Greetings {player.name} the {player.race}!")


def brewswig_tell_me_your_name():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"Well hello there adventurer! Allow me to introduce myself.\"\n\n"
                        "He places the freshly cleaned glass mug in front of you, and proudly throws the cleaning\n"
                        "rag over his shoulder; clearing his throat as he does so.")
    print()
    utility.test_colour("**Ahem!**\n\n"
                        "Brewswig the Innkeeper:\n"
                        "\"The names Brewswig, an' this fine den ye find yeself in this even'in is none other than The "
                        "Snarling Warg Tavern.\"\n"
                        "\"Sit down and make yourself at 'ome while I fetch ye a pint."
                        "You look like ye been on the road for a while.\"")
    print()
    utility.test_colour("Taking the glass mug in front of you; Brewswig turns toward a oaken barrel resting on a "
                        "shelf next to him.\n"
                        "The foamy ale quickly fills the glass mug, and once filled; Brewswig places it down in front "
                        "of you.\n\n"
                        "Brewswig the Innkeeper:\n"
                        "\"There ya go, this ones on the house.\"\n"
                        "\"So... ah... what did you say your name was?\"")
    print()


def brewswig_query_name(player):
    player_name = f"\33[35m{player.name}\33[0m"
    utility.test_colour('Brewswig the Innkeeper:\n'
                        f"\"{player_name}, eh? Strange name.. None too common in these parts.\"\n\n"
                        f"\"You did say \33[35m{player_name}, right?\"")


def brewswig_no_name_given():
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"Look, i've been in the business a long time; and my gut tells me that ain't your name.\"\n"
                        "\"I got plenty of glasses to clean while I wait for you to give me a proper answer.\"")
    print()


def brewswig_incorrect_name():
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"I did think that was a strange name... My apologies, I don't hear quite so well these "
                        "days.\"\n""\"What did you say your name was again?\"")
    utility.purple_text()


def brewswig_tell_me_your_race(player):
    utility.clear()
    player_name = f"\33[35m{player.name}\33[0m"
    utility.test_colour("Brewswig the Innkeeper:\n"
                        f"\"Well I must say it is nice to meet you {player_name}. It's been a while since someone new "
                        f"and interesting came through\n those doors.\"")
    print()
    utility.test_colour("Brewswig chuckles to himself before removing a clean glass mug from underneath the bar and "
                        "turns to the same barrel \nhe had filled yours from, producing a nice foamy ale; "
                        "that he quickly gulps down.\n\n"
                        
                        "**Gulp... Gulp... Gulp...**\n\n"
                        
                        "He wipes the foam stuck to his bushy mustache with satisfied look on his face.\n"
                        "Smiling once more, he turns to you.")
    print()
    utility.test_colour("Brewswig the Innkeeper:\n"
                        f"\"So {player_name}, while we're getting to know each other, how 'bout tellin me a little bit "
                        f"about yourself?\"\n"
                        "\"I must say, with all that adventuring gear on, I can't tell where you hail from?\"\n\n"
                        "\"Are you from the Human settlements to the North?\"\n"
                        "\"Or maybe the Elven forests to the West?\"\n"
                        "\"Perhaps you come from the grand underground kingdom of the Dwarves to the East?\"")
    print()
    utility.press_enter_to_continue()
    utility.clear()


def choose_race_options():
    utility.test_colour("Brewswig the Innkeeper:\n""\"Tell me of your home and kin... theres another ale in it for "
                        "you!!\"")

    print("\33[96m--Available Races--\33[92m")
    print("Choose your Race:\n")

    utility.test_colour("\33[92m[I] Human:\n"
                        "While not especially unique, Humans are well rounded and effective adventurers:\n"
                        "\33[96mHP:25,  STR: 10,  DEF: 10\n\n"
                        
                        "\33[92m[II] Elf:\n"
                        "Ancient and generally peaceful people, what they lack in strength, they make up in speed.\n"
                        "\33[96mHP:20,  STR: 5,  DEF: 10\n\n"
                        
                        "\33[92m[III] Dwarf\n"
                        "Proud and stubborn folk, though their size limits their speed,they are fierce warriors.\n"
                        "\33[96mHP:30,  STR: 15,  DEF: 10")


def brewswig_human_details():
    utility.clear()
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print("\"\33[35mHuman\33[33m, ay..? I thought so, but it's always better to know than to assume.\"")
    print("\"I have met my fair share of your kin from this side of the bar over the years. Many a story has been ")
    print("recounted on that very stool you sit upon.\"\n")
    print("\"Funny though, I don't really recall anything great or exceptional about them.\"\n")
    print("\"Although I have a feeling you might be an exception...\"\n")
    print("\"I know of a \33[35mHuman\33[33m settlement to the North of here, but the name of the place escapes me.\"")
    print("\"Its name was just so... so... unexceptional...\"\n")
    print('\33[36m'"Human Base Stats:\nHP:25,  STR: 10,  DEF: 10\n\33[33m")
    print("\"Oh... sorry... I got caught up in my story. You did say \33[35mHuman\33[33m, right?\"")


def brewswig_elf_details():
    utility.clear()
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print("\"An \33[35mElf\33[33m you say..?! Fascinating! I can't say I was expectin that!\"")
    print("\"I can't recall the last time I spoke too or even saw an \33[35mElf\33[33m!\"\n")
    print("\"If I'm not mistaken; your kin are known for their agility and wisdom not for their strength.\"")
    print("\"I'm yet to see anyone best a \33[35mElf\33[33m with speed alone, 'cept when they've had a tad too much "
          "ale o'course\"\n")
    print("\"You can find an \33[35mElf\33[33m settlement to the West of here, deep in the forest.\"")
    print("\"I personally would not go there, these old legs can't carry me from danger like they could when I ")
    print("was younger. However, you look more agile than most... you might be okay...\"\n")
    print('\33[36m'"Elf Base Stats:\nHP:25,  STR: 10,  DEF: 10\n\33[33m")
    print("\"Oh... sorry... I got caught up in my story. You did say \33[35mElf\33[33m, right?\"\n")


def brewswig_dwarf_details():
    utility.clear()
    print('\33[32m'"Brewswig the Innkeeper:"'\33[33m')
    print("\"Really? A \33[35mDwarf\33[33m..? You're much... taller... than I would have expected.\"")
    print("\"I remember that last Dwarf I saw... Boasted on and on about how strong he was.\"")
    print("\"Shame his strength didnt help him run out of the way of that mad pack mule... That wasn't pretty...\"\n")
    print("\"You can find the \33[35mDwarf\33[33m kingdom in the mountains to the East if your interested.\"")
    print("\"But personally, I like to keep myself above ground. I have never been curious to know what lurks")
    print("in the depths below the surface.\"\n")
    print("You however... well... you look like you can handle that sort of adventure.\"\n")
    print("\"Oh... sorry... I got caught up in my story. You did say \33[35mDwarf\33[33m, right?\"\n")


def brewswig_tell_me_your_specialty(player):
    utility.clear()
    print('\33[32mBrewswig the Innkeeper:\33[33m')
    print(f"\"So your a \33[35m{player.race}\33[33m who goes by the name \33[35m{player.name}\33[33m? Well met "
          f"friend.\nHere... another ale as promised.\"\n")
    print("\33[35mBrewswig\33[0m takes your mug and once again fills it with ale. Frothy foam drips down the side of")
    print("the glass as he places it down in front of you.\n")
    print("So traveller, you must have travelled a while to get here. Tell me... What is your role in the world?\"")
