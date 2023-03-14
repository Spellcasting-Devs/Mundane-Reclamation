import os
import sys
from configparser import ConfigParser
from os.path import (dirname, abspath)


PATH_PLAYERS = f"{dirname(abspath(__file__))}/../config/players/"


def create_player():
    name = str(input("Enter your player name: "))
    if len(name) in range(1, 20):
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
            
        return name
    else:
        print("You did not provide a valid name. Please try again.")
        sys.exit(1)


def load_player():
    player_files = os.listdir(PATH_PLAYERS)
    if player_files != None:
        print("SELECT YOUR PLAYER FILE\n")
        
        for i, p in enumerate(player_files):
            print(f"[{i+1}] - {p[:-4]}")
            
        player_name_selection = int(input("\n: "))
        
        if player_name_selection in range(1, len(player_files)+1):
            return player_files[player_name_selection-1]
        else:
            print("Unknown operation")
            sys.exit(1)
    else:
        print("No existing player files")
        sys.exit(1) # implement better game logic
