import dialogue
import utility


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
            utility.clear()
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

        while not correct_race:
            dialogue.choose_race_options()
            print()
            race = input('\33[0m'"Answer: "'\33[35m').lower()

            if race == "i" or race == "1":
                dialogue.brewswig_human_details()
                player_race = self.get_player_race_human(player)
            elif race == "ii" or race == "2":
                dialogue.brewswig_elf_details()
                player_race = self.get_player_race_elf(player)
            elif race == "iii" or race == "3":
                dialogue.brewswig_dwarf_details()
                player_race = self.get_player_race_dwarf(player)
            else:
                print("\n\33[31mInvalid Selection: Please try again\n")
                utility.press_enter_to_continue()
                utility.clear()
                continue

            answer = utility.confirm_option()
            if answer == "1":
                return player_race
            else:
                utility.clear()
                continue

    # ----- Character Race Options ----- #
    @staticmethod
    def get_player_race_human(player):
        player.race = "Human"
        player.health = 25
        player.max_health = player.health
        player.strength = 10
        player.defense = 5
        return player

    @staticmethod
    def get_player_race_elf(player):
        player.race = "Elf"
        player.health = 20
        player.max_health = player.health
        player.strength = 5
        player.defense = 10
        return player

    @staticmethod
    def get_player_race_dwarf(player):
        player.race = "Dwarf"
        player.health = 30
        player.max_health = player.health
        player.strength = 15
        player.defense = 10
        return player

    def tell_me_your_profession(self, player):
        utility.clear()
        correct_profession = False
        dialogue.brewswig_tell_me_your_specialty(player)
        while not correct_profession:
            dialogue.choose_class()
            profession = input('\33[0m'"Answer: "'\33[35m').lower()

            if profession == "i" or profession == "1":
                dialogue.brewswig_fighter_details()
                player_profession = self.get_player_profession_fighter(player)
            elif profession == "ii" or profession == "2":
                dialogue.brewswig_ranger_details()
                player_profession = self.get_player_profession_ranger(player)
            else:
                print("\n\33[31mInvalid Selection: Please try again\n")
                utility.press_enter_to_continue()
                utility.clear()
                continue

            answer = utility.confirm_option()
            if answer == "1":
                return player_profession
            else:
                utility.clear()
                continue

    @staticmethod
    def get_player_profession_fighter(player):
        player.profession = "Fighter"
        player.weapon = "Sword"
        player.strength += 5
        player.max_health += 5
        player.health = player.max_health
        player.gold += 50
        player.health_potion = 1
        return player

    @ staticmethod
    def get_player_profession_ranger(player):
        player.profession = "Ranger"
        player.weapon = "Bow"
        player.defense += 2
        player.max_health += 10
        player.health = player.max_health
        player.gold += 100
        return player


# ----- CREATE CHARACTER ----- #
def create_character(player):
    character_object = CharacterCreation()
    character_object.tell_me_your_name(player)
    utility.clear()
    character_object.tell_me_your_race(player)
    utility.clear()
    character_object.tell_me_your_profession(player)
    utility.clear()
    dialogue.brewswig_quest_dialogue()
    utility.press_enter_to_continue()

    return player
