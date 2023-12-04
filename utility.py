import os
import string
import dialogue

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


def colour_word(word):
    colour_code = ''
    punct = string.punctuation
    trailing_punct = ''

    for symbol in punct:
        if symbol in word:
            trailing_punct = symbol
            word = word.replace(symbol, '')
    if word.lower() in ["so", "goes", "name", "innkeeper", "test", "code"]:
        colour_code = GREEN
    if word.lower() in ["brewswig", "innkeeper"]:
        colour_code = PURPLE
    if word.lower() in ["hello", "adventurer", "the snarling", "warg", "tavern", ]:
        colour_code = AQUA

    return colour_code + word + WHITE + trailing_punct

def test_colour(input_string):
    words = input_string.split()
    formatted_words = [colour_word(w) for w in words]
    formatted_string = ' '.join(formatted_words)
    print(formatted_string)

