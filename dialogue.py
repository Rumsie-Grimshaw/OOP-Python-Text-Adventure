import utility


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
    print("")


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
                        "\"Perhaps you come from the grand underground kingdom of the Dwarves to the East?\"\n\n"
                        "\"Tell me of your home and kin... theres another ale in it for "
                        "you!!\"")
    print()
    utility.press_enter_to_continue()
    utility.clear()


def choose_race_options():
    print("\33[96m--Available Races--\33[92m\n")

    utility.test_colour("\33[92m[I] Human:\n"
                        "While not especially unique, Humans are well rounded and effective adventurers:\n"
                        "\33[96mHP:25,  STR: 10,  DEF: 10\n\n"

                        "\33[92m[II] Elf:\n"
                        "Ancient and generally peaceful people, what they lack in strength, they make up in speed.\n"
                        "\33[96mHP:20,  STR: 5,  DEF: 10\n\n"

                        "\33[92m[III] Dwarf\n"
                        "Proud and stubborn folk, though their size limits their speed,they are fierce warriors.\n"
                        "\33[96mHP:30,  STR: 15,  DEF: 10")
    print("\n\33[92mChoose your Race:")


def brewswig_human_details():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"Human, ay..? I thought so, but it's always better to know than to assume.\"\n\n"
                        "\"I have met my fair share of your kin from this side of the bar over the years. Many a story "
                        "has been recounted on that very stool you sit upon.\"\n"
                        "\"Funny though, I don't really recall anything great or exceptional about them.\"\n"
                        "\"Although I have a feeling you might be an exception...\"\n\n"
                        "\"I know of a Human settlement to the North of here, but the name of the place escapes me.\""
                        "\"Its name was just so... so... unexceptional...\"\n\n"
                        "\33[96mBase Stats (Human\33[96m):\nHP:25,  STR: 10,  DEF: 10\n\33[0m\n"
                        "\"Oh... sorry... I got caught up in my story. You did say Human, right?\"")


def brewswig_elf_details():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"An Elf you say..?! Fascinating! I can't say I was expectin that!\""
                        "\"I can't recall the last time I spoke too or even saw an Elf!\"\n"
                        "\"If I'm not mistaken; your kin are known for their agility and wisdom not for their "
                        "strength.\"\n"
                        "\"I'm yet to see anyone best a Elf with speed alone, 'cept when they've had a tad too much "
                        "ale o'course\"\n\n"
                        "\"You can find the Elven settlement to the West of here, deep in the forest.\"\n"
                        "\"I personally would not go there, these old legs can't carry me from danger like they could "
                        "when I was younger. However, you look more agile than most... you might be okay...\"\n\n"
                        '\33[96m'"Base Stats: (Elf\33[96m):\nHP:25,  STR: 10,  DEF: 10\n\33[0m\n"
                        "\"Oh... sorry... I got caught up in my story. You did say Elf, right?\"")


def brewswig_dwarf_details():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n"
                        "\"Really? A Dwarf..!? You're much... taller... than I would have expected.\"\n\n"
                        "\"I remember that last Dwarf I saw... Wouldn't stop boasting about his 'natural' "
                        "strength...\"\n"
                        "\"Shame his strength didnt help him run out of the way of that mad pack mule... "
                        "That wasn't pretty...\"\n\n"
                        "\"You can find the underground Dwarven kingdom in the mountains to the East if your "
                        "interested.\"\n"
                        "\"Personally, I have never been curious to know what lurks in the depths of the earth.\"\n"
                        "\"You however... well... you look like you can handle that sort of curiosity.\"\n\n"
                        '\33[96m'"Base Stats: (Dwarf\33[96m):\nHP:30,  STR: 15,  DEF: 10\n\33[0m\n"
                        "\"Oh... sorry... I got caught up in my story. You did say Dwarf, right?\"\n")


def brewswig_tell_me_your_specialty(player):
    utility.clear()
    player_name = f"\33[35m{player.name}\33[0m"
    utility.test_colour("Brewswig the Innkeeper:\n"
                        f"\"So your a {player.race} who goes by the name {player_name}, huh? Well met friend.\"\n"
                        "\"I still think your name is stange, but alas... as promised I'll fetch ye another ale.\"\n\n"
                        
                        "Brewswig takes your mug and once again fills it with ale. Frothy foam drips down the side of "
                        "the glass as he places it\ndown in front of you.\n\n"
                        
                        f"\"So {player_name}, you must have travelled quite a distance to get all the way out here.\"\n"
                        "\"You don't dress like a commoner, and you have a rough look about you. Tell me...\""
                        "\"Have you experienced much trouble on the road?\"\n\n"
                        "\"What is your profession?\"\n")
    print()
    utility.press_enter_to_continue()
    utility.clear()


def choose_class():
    print("\33[96m--Available Class--\33[92m\n\n")
    utility.test_colour("\33[92m[I] Fighter:\33[0m\n"
                        "Favouring melee weapons and brute strength, fighters are not afraid to close the distance "
                        "between themselves and their\nfoes; in order to get close and personal.\n\n"
                        "\33[92mStarting Inventory:\33[0m\n- Weapon: Sword\n- Gold: 50gp\n"
                        "\33[96m---Bonuses---\33[0m\n"
                        "- Proficient with melee weapons\n"
                        "- +5 HP, +5 STR"
                        "- Starts with a Health Potion\n\n\n"

                        "\33[92m[I] Ranger:\33[0m\n"
                        "Favouring ranged weapons, rangers are skilled at utilising distance and keen senses to "
                        "notice weaknesses from afar.\n\n"
                        "\33[92mStarting Inventory:\33[0m\n- Weapon: Bow\n- Gold: 100gp\n"
                        "\33[96m---Bonuses---\33[0m\n"
                        "- Proficient with ranged weapons\n"
                        "- +10 HP, +2 DEF\n"
                        "- .75x Gold multiplier from loot.\n\n")
    print("\n\33[92mChoose your Profession:")
    print()

def brewswig_fighter_details():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n\n"
                        "A fighter you say? I know you only just arrived, but I was wondering if perhaps you might \n"
                        "be willing to do a small task for me?\n"
                        "I must admit; it's a little bit of a sad affair for me, although I think you'll be able to"
                        "handle it. There will be a reward in it for you of course.\n\n"
                        "But enough of that...before I give you the details... You did say a fighter right?")

def brewswig_ranger_details():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n\n"
                        "\"Did you say a ranger! I don't suppose I could trouble you to run a little errand for me, "
                        "could I?\"\n"
                        "\"With the keen senses of a ranger, it should be no trouble for you at all!\"\n\n"
                        "\"Before I give you the details though... You did say a ranger right?\"")

def brewswig_quest_dialogue():
    utility.clear()
    utility.test_colour("Brewswig the Innkeeper:\n\n"
                        "\"I need you to uh-hh... I need you too...\"\n\n"
                        "Brewswig takes in a deep breathe, averting his gaze as he does so; exhaling slowly. In a \n"
                        "single motion, Brewswig downs the remnants of the ale in his mug and fills it once more.\n"
                        "You notice a saddened glistening in his eye as he stands facing the barrel.\n"
                        "He turns to you, meeting your gaze.\n\n"
                        
                        "\"I need you to go out to the paddock and kill Bubbles... my cow...\"\n\n"
                        
                        "As the words escape his mouth, you witness the grief that is befalling this man, his \n"
                        "knuckles paling from the clenching of his fists atop the bar.\n\n"
                        
                        "\"She's gone mad you see... I don't know how, or why... but she hasn't been the same for \n"
                        "about a month now."
                        "Once, she was the sweetest little cow you've ever met, but lately she wont let anyone near \n"
                        "her. Hell, she even tried to kill one of the young boys who used to pet her.\n"
                        "Even tried to kill me just yesterday! It's like she doesn't even recognise me...\"\n\n"
                        "\"So what do you say? Are you willing help old Brewswig? Can you put Bubbles out of her \n"
                        "misery?\"")

