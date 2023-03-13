from configparser import ConfigParser
from os.path import (dirname, abspath)
from os import system

FILEPATH = f"{dirname(abspath(__file__))}/players"



def new_game():
    name = str(input("enter your player name:"))
    system(f"cd {FILEPATH} && touch {name}.ini")
    
    cfg = ConfigParser()
    
    cfg['CONSTANTS'] = {
        'player_name': name,
    }
    
    cfg['VARIABLES'] = { # starter values defined here
        'health': 100,
        'mana': 100,
        'strength': 50,
    }

    with open(f"{FILEPATH}/{name}.ini", 'w') as cfg_player:
        cfg.write(cfg_player)
        cfg_player.flush()



def load_game():
    print("loaded")



def main():
    dec = int(input("New Game [1]\nLoad Game[2]\n\n:"))
    new_game() if dec == 1 else load_game()
    
    
    
main()