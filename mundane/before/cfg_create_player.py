import os
from configparser import ConfigParser
from os.path import (dirname, abspath)


PATH_PLAYERS = f"{dirname(abspath(__file__))}/../config/players/"


def create_player():
    name = str(input("Enter your player name: "))
    
    if os.name == 'posix':
        os.system(f"cd {PATH_PLAYERS} && touch {name}.ini")
    else:
        os.system(f"cd {PATH_PLAYERS} && type NUL > {name}.ini")
    
    cfg = ConfigParser()
    
    cfg['CONSTANTS'] = {
        'player_name': name
    }
    
    cfg['VARIABLES'] = { # starter values defined here
        'health': 100,
        'mana': 100,
        'strength': 50
    }

    with open(f"{PATH_PLAYERS}{name}.ini", 'w') as cfg_player:
        cfg.write(cfg_player)
        cfg_player.flush()
