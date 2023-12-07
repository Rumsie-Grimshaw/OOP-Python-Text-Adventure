import os
import re


WHITE = '\33[0m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
PURPLE = '\33[35m'
AQUA = '\033[36m'


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
          f"HP: {player.health}\n"
          f"Str: {player.strength}\n"
          f"Def: {player.defense}\n")


def highlight_phrases(sentence, target_phrases_list):
    # Set colours of the lists in target_phrases_list in order.
    color_codes = ('91', '92', '33', '94', '35', '36', '97')
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
            highlighted_sentence = pattern.sub(
                f'\033[{color_code}m\\1\033[0m', highlighted_sentence
            )

    return highlighted_sentence.strip()

def test_colour(input_string):
    sentence = input_string
    target_phrases_list = [
        # Enemies - Red
        ["goblin", "goblins", "trolls", "wolf"],

        # Interactions / Options - Green
        ["brewswig the innkeeper"],

        # Treasures / Valuables - Yellow
        ["treasure", 'gp', 'gold', 'coins', 'jewels'],

        # Directions - Blue
        ["North", "South", "East", "West"],

        # Names / Important - Purple
        ["brewswig", "the snarling warg tavern", 'dwarf', 'dwarven', 'dwarves', 'elf', 'elven', 'elves', 'human',
         'humans'],

        # Items / Equipment - Aqua
        ["sword", "shield", "potion", "dagger", "ale"],
    ]
    highlighted_result = highlight_phrases(sentence, target_phrases_list)
    print(highlighted_result)


