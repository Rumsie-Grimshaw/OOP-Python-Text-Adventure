def get_tutorial_quest(player):
    if player.race == "Fighter":
        fighter_tutorial_quest()
        return
    else:
        if player.race == "Ranger":
            ranger_tutorial_quest()
            return

def fighter_tutorial_quest():
    pass
def ranger_tutorial_quest():
    pass