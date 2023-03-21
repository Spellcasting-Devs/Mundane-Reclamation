import os
import sys
import curses
from configparser import ConfigParser
from os.path import dirname, abspath


PATH_PLAYERS = f"{dirname(abspath(__file__))}/../config/players/"


def create_player(name, race):
    if os.name == 'posix':
        os.system(f"cd {PATH_PLAYERS} && touch {name}.ini")
    else:
        os.system(f"cd {PATH_PLAYERS} && type NUL > {name}.ini")
        
    race_stats = get_race_stats(race)
    
    cfg = ConfigParser()
    
    cfg['CONSTANTS'] = {
        'player_name': name,
        'player_race': race,
    }
    
    cfg['VARIABLES'] = {
        'health': 100,
        'mana': 100,
        'strength': 50,
    }
    
    cfg['INTRO'] = {
        'c1': False,
    }
    
    cfg['CHAPTER1'] = {
        'c1': False,
        'c2': False,
        'c3': False,
    }

    with open(f"{PATH_PLAYERS}{name}.ini", 'w') as cfg_player:
        cfg.write(cfg_player)
        cfg_player.flush()
      
      
def get_race_stats(race):
    race_stats = {
        'Human': {
            'health': 100,
            'strength': 50,
        },
        'Elves': {
            'health': 120,
            'strength': 90,
        }
    }
        

def load_player():
    global player_files
    player_files = os.listdir(PATH_PLAYERS)
    if player_files != None:
        player_name_selection = curses.wrapper(main)
        player_name_selection += 1
        
        if player_name_selection in range(1, len(player_files)+1):
            return player_files[player_name_selection-1]
        else:
            print("Unknown operation")
            sys.exit(1)
    else:
        print("No existing player files")
        sys.exit(1) # implement better game logic


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(player_files):
        x = w//2 - len(row)//2
        y = h//2 - len(player_files)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(player_files)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return player_files.index(player_files[current_row])
            
        print_menu(stdscr, current_row)