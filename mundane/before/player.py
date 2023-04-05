import os
import sys
import curses
from configparser import ConfigParser
from os.path import dirname, abspath


PLAYER_PATH = f"{dirname(abspath(__file__))}/../config/players/"
CONFIG_PATH = f"{dirname(abspath(__file__))}/../config/"



def create_player(name, role):
    if os.name == 'posix':
        os.system(f"cd {PLAYER_PATH} && touch {name}.ini")
    else:
        os.system(f"cd {PLAYER_PATH} && type NUL > {name}.ini")
        
    role_stats = get_role_stats(role)
    
    config = ConfigParser()
    
    config['CHARACTER'] = {
        'player_name': name,
        'player_role': role,
    }
    
    config['BASE_STATS'] = {
        'health': role_stats[0],
        'mana': role_stats[1],
        'strength': role_stats[2],
        'barter': role_stats[3],
    }
    
    config['LEVEL1'] = {
        'c1': False,
        'c2': False,
        'c3': False,
    }

    with open(f"{PLAYER_PATH}{name}.ini", 'w') as player_config:
        config.write(player_config)
        player_config.flush()
      
      
def get_role_stats(role):
    config = ConfigParser()
    config.read(CONFIG_PATH + "roles.ini")

    roles = config.items(role.upper())        
    role_stats = []
    for _, s in roles:
        role_stats.append(s)
        
    return role_stats


def load_player() -> str:
    global player_files
    player_files = os.listdir(PLAYER_PATH)
    
    if len(player_files) > 0:
        player_file_index = curses.wrapper(main)
        player_file_index += 1

        return player_files[player_file_index-1]
    
    return "0"


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