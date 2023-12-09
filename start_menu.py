import sys

import entities
import utility

# Draw main menu on start-up
def draw_main_menu():
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                     ╔═══════════════════════════════╗                                     ")
    print("                                     ║  ¥    M A I N - M E N U    ¥  ║                                     ")
    print("                                     ╠═══════════════════════════════╣                                     ")
    print("                                     ║     1.  N E W  G A M E        ║                                     ")
    print("                                     ║     2. L O A D   G A M E      ║                                     ")
    print("                                     ║     3.     A B O U T          ║                                     ")
    print("                                     ║     4. Q U I T   G A M E      ║                                     ")
    print("                                     ╚═══════════════════════════════╝                                     ")
    print("                                                                                                           ")
    print("                                           Please choose a option:                                         ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")
    print("                                                                                                           ")

# Give functionality to options in main menu
def interact():
    while True:
        draw_main_menu()
        menu_choice = input("")
        if menu_choice == "1":
            return menu_choice

        elif menu_choice in ("2", "3", "4"):
            if menu_choice == "2":
                player = entities.Player()
                utility.load_game(player)
                print(player.name, player.gold)
                return menu_choice

            if menu_choice == "3":
                utility.clear()
                about()
            elif menu_choice == "4":
                print("Thanks for playing. You can now safely close the window.")
                sys.exit()
            else:
                print("Please enter a valid option!")

        else:
            print("Please select a valid option.")
            input('\33[32m'"Press any key to continue."'\33[0m')

def about():
    utility.clear()
    print("This game is a basic text base adventure program developed by Rumsie Grimshaw as a test concept.")
    print()
    print("The purpose of the game is to implement and better understand Object Orientated Programming concepts by ")
    print("utilising them in a interactive adventure game.")
    print("** further information to be added**!\n")
    print()
    input('\33[32m'"Press any key to continue."'\33[0m')
    return