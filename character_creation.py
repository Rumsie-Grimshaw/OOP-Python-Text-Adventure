import dialogue
import utility

class CharacterCreation:
    def tell_me_your_name(self, player):
        correct_name = False
        dialogue.brewswig_tell_me_your_name()
        player.name = input('\33[0m'"Answer: "'\33[35m')
        utility.clear()
        while not correct_name:
            if player.name == "":
                utility.clear()
                dialogue.brewswig_no_name_given()
                player.name = input('\33[0m'"Answer: "'\33[35m')
                continue
            dialogue.brewswig_query_name(player)
            answer = utility.confirm_option()
            if answer == "1":
                correct_name = True
            else:
                utility.clear()
                dialogue.brewswig_incorrect_name()
                print()
                player.name = input('\33[0m'"Answer: "'\33[35m')
                utility.clear()
                continue

        utility.clear()
        return player.name


    # Look at simplifying this code
    def tell_me_your_race(self, player):
        correct_race = False
        dialogue.brewswig_tell_me_your_race(player)
        dialogue.choose_race_options()
        race = input('\33[0m'"Answer: "'\33[35m').lower()
        while not correct_race:
            if race == "i" or race == "1":
                player.get_player_race_human(player)
                dialogue.brewswig_human_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True
                else:
                    utility.clear()
                    correct_race = False
                    dialogue.choose_race_options()
                    race = input('\33[0m'"Answer: "'\33[35m').lower()
                    continue

            elif race == "ii" or race == "2":
                player.get_player_race_elf(player)
                dialogue.brewswig_elf_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True
                else:
                    utility.clear()
                    correct_race = False
                    dialogue.choose_race_options()
                    race = input('\33[0m'"Answer: "'\33[35m').lower()
                    continue

            elif race == "iii" or race == "3":
                player.get_player_race_dwarf(player)
                dialogue.brewswig_dwarf_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True
                else:
                    utility.clear()
                    correct_race = False
                    dialogue.choose_race_options()
                    race = input('\33[0m'"Answer: "'\33[35m').lower()
                    continue

            else:
                print("\n\33[31mInvalid Selection: Please try again\n")
                utility.press_enter_to_continue()
                utility.clear()
                dialogue.choose_race_options()
                continue

