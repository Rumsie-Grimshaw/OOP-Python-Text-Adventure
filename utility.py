import os
import re

# Clear Terminal
def clear():
    os.system("cls")

# Draw box at top of 'Terminal'
def draw_long():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                                         ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def draw_short():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def green_text():
    print('\33[32m')

def white_text():
    print('\33[0m')

def gold_text():
    print('\33[33m')

def purple_text():
    print('\33[35m')

def press_enter_to_continue():
    input('\33[32m'"Press any key to continue...")

def confirm_option():
    print('\33[32m'"1) Agree     2) Disagree"'\33[35m')
    print()
    answer = input('\33[0m'"Answer: "'\33[35m')
    return answer

def test_character_creation(player):
    print(f"Name: {player.name}\n"
          f"Race: {player.race}\n"
          f"Profession: {player.profession}\n"
          f"Weapon: {player.weapon}\n"
          f"Max Health: {player.max_health}\n"
          f"HP: {player.health}\n"
          f"Str: {player.strength}\n"
          f"Def: {player.defense}\n"
          f"Gold: {player.gold}\n"
          f"Potions: {player.health_potion}\n")


def highlight_phrases(sentence, target_phrases_list):
    # Set colours of the lists in target_phrases_list in order.
    color_codes = ('91', '92', '33', '94', '95', '96', '97')
    # Equals the sentence from test_colour()
    highlighted_sentence = sentence

    # Iterate the index (i) and tuples (key, value) representing target phrases in target_phrases_list
    for i, target_phrases in enumerate(target_phrases_list):
        # Sort list of strings by len(x), where x is temp key, discard key and order desc
        target_phrases = sorted(target_phrases, key=lambda x: len(x), reverse=True)
        # Iterate though color_code and assign color_code index to list index
        color_code = color_codes[i % len(color_codes)]

        for target_phrase in target_phrases:
            target_phrase_lower = re.escape(target_phrase.lower())
            pattern = re.compile(fr'\b({target_phrase_lower})\b', re.IGNORECASE)
            highlighted_sentence = pattern.sub(f'\033[{color_code}m\\1\033[0m', highlighted_sentence)

    return highlighted_sentence.strip()

def test_colour(input_string):
    sentence = input_string
    target_phrases_list = [
        # Enemies - Red
        ["goblin", "goblins", "trolls", "wolf", "bubbles"],

        # Interactions / Options - Green
        ["brewswig the innkeeper"],

        # Treasures / Valuables - Yellow
        ["treasure", 'gp', 'gold', 'coins', 'jewels'],

        # Directions - Blue
        ["North", "South", "East", "West", "the snarling warg tavern"],

        # Names / Important - Purple
        ["brewswig", 'dwarf', 'dwarven', 'dwarves', 'elf', 'elven', 'elves', 'human',
         'humans', 'fighter', 'ranger'],

        # Items / Equipment - Aqua
        ["sword", "shield", "potion", "dagger", "ale"],
    ]
    highlighted_result = highlight_phrases(sentence, target_phrases_list)
    print(highlighted_result)

def save_game(player):
    player_state = [player.name,
                    player.race,
                    player.profession,
                    player.weapon,
                    player.max_health,
                    player.health,
                    player.strength,
                    player.defense,
                    player.gold,
                    player.health_potion]
    with open("load.txt", "w") as save_file:
        for field in player_state:
            save_file.write(str(field) + "\n")
        save_file.close()

def load_game(player):
    with open("load.txt", "r") as load_file:
        lines = load_file.readlines()

        # Assign values to player properties based on file content
        player.name = lines[0].strip()
        player.race = lines[1].strip()
        player.profession = lines[2].strip()
        player.weapon = lines[3].strip()
        player.max_health = int(lines[4].strip())
        player.health = int(lines[5].strip())
        player.strength = int(lines[6].strip())
        player.defense = int(lines[7].strip())
        player.gold = int(lines[8].strip())
        player.health_potion = int(lines[9].strip())

        return player





