from configparser import ConfigParser
from os.path import (dirname, abspath)
from os import system

FILEPATH = f"{dirname(abspath(__file__))}/players"


"""
This is an example of how the creation of new player files could look like. A new .ini file with starter values is being initialized.
System commands must yet be configured for differemt operating systems.
"""
def new_game():
    name = str(input("enter your player name:"))
    system(f"cd {FILEPATH} && touch {name}.ini")
    
    cfg = ConfigParser()
    
    cfg['CONSTANTS'] = {
        'player_name': name
    }
    
    cfg['VARIABLES'] = { # starter values defined here
        'health': 100,
        'mana': 100,
        'strength': 50
    }

    with open(f"{FILEPATH}/{name}.ini", 'w') as cfg_player:
        cfg.write(cfg_player)
        cfg_player.flush()



# and this is where we would load existing game files. I'm thinking of a way to properly load them into the game.
def load_game():
    print("loaded")



def main():
    dec = int(input("New Game [1]\nLoad Game[2]\n\n:"))
    new_game() if dec == 1 else load_game()
    
    
    
main()