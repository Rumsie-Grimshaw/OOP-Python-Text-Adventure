import dialogue
import utility
import player

class CharacterCreation:
    def tell_me_your_name(self, player):
        correct_name = False
        dialogue.brewswig_tell_me_your_name()
        player.name = input('\33[0m'"Answer: "'\33[35m')
        utility.clear()
        while not correct_name:
            if player.name.strip() == "":
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
                self.get_player_race_human(player)
                dialogue.brewswig_human_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True

            if race == "ii" or race == "2":
                self.get_player_race_elf(player)
                dialogue.brewswig_elf_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True

            if race == "iii" or race == "3":
                self.get_player_race_dwarf(player)
                dialogue.brewswig_dwarf_details()
                answer = utility.confirm_option()
                if answer == "1":
                    correct_race = True

                else:
                    print("\n\33[31mInvalid Selection: Please try again\n")
                    utility.press_enter_to_continue()
                    utility.clear()
                    dialogue.choose_race_options()
                    continue

    def tell_me_your_specialty(self, player):
        utility.clear()
        dialogue.brewswig_tell_me_your_specialty(player)
        input()

### Character Race Options ###
    def get_player_race_human(self, player):
        player.race = "Human"
        player.health = 25
        player.strength = 10
        player.defense = 10
        return player.race, player.health, player.strength, player.defense

    def get_player_race_elf(self, player):
        player.race = "Elf"
        player.health = 20
        player.strength = 5
        player.defense = 10
        return player.race, player.health, player.strength, player.defense

    def get_player_race_dwarf(self, player):
        player.race = "Dwarf"
        player.health = 30
        player.strength = 15
        player.defense = 10
        return player.race, player.health, player.strength, player.defense

