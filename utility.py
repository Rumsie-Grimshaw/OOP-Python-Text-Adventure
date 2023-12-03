import os

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