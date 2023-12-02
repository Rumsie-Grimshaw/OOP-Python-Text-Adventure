import utility

class Brewswig:
    def __init__(self):
        pass

    def greet_player(self, player_name):
        print("Brewswig the Innkeeper:")
        print(f"Greetings {player_name}!")
        
    def tell_me_your_name(self):
        utility.clear()
        print('\"Brewswig the Innkeeper:')
        print("\"Welcome adventurer! Allow me to introduce myself.\" \n**Ahem!**")
        print(
            "\n\"The names Brewswig, an' this fine den you find yourself in this even'in, is The Snarling Warg Tavern.\"")
        print(
            "\"Sit down, make yourself at 'ome. I'll fetch ye a pint. Yer look like ye been on the road for a while.\"")
        print("\n**clink**\n**liquid pouring**\n")
        print("Brewswig the Innkeeper:")
        print("\"There ya go... ah... what should I call you?\"\n")

# Create an instance of Brewswig
brewswig = Brewswig()