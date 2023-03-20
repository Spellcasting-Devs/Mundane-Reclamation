import curses
import os
import sys

MENU = ['New Game', 'Load Game', 'Exit']


mundane = """ ███▄ ▄███▓ █    ██  ███▄    █ ▓█████▄  ▄▄▄       ███▄    █ ▓█████ 
▓██▒▀█▀ ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▒████▄     ██ ▀█   █ ▓█   ▀ 
▓██    ▓██░▓██  ▒██░▓██  ▀█ ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒███   
▒██    ▒██ ▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄ 
▒██▒   ░██▒▒▒█████▓ ▒██░   ▓██░░▒████▓  ▓█   ▓██▒▒██░   ▓██░░▒████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░
░  ░      ░░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░
░      ░    ░░░ ░ ░    ░   ░ ░  ░ ░  ░   ░   ▒      ░   ░ ░    ░   
       ░      ░              ░    ░          ░  ░         ░    ░  ░
                                ░                                  """
                                
reclamation = """ ██▀███  ▓█████  ▄████▄   ██▓    ▄▄▄       ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▓██▒   ▒████▄    ▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░██████▒▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░ ░ ░  ░  ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░░   ░    ░   ░          ░ ░    ░   ▒   ░      ░     ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
   ░        ░  ░░ ░          ░  ░     ░  ░       ░         ░  ░         ░      ░ ░           ░ 
                ░     """
              


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")

def load_menu():
    load_title_screen()
    return_code = curses.wrapper(main)
    
    clear_screen()
    
    return return_code # the return code defines the operation which has to be performed -> 0: create new player, 1: load player data


def load_title_screen():
    clear_screen()
    print(f"\n{mundane}\n{reclamation}\n")
    print("PRESS ENTER TO START...\n")
    input()
    
    
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(MENU):
        x = w//2 - len(row)//2
        y = h//2 - len(MENU)//2 + idx
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
        elif key == curses.KEY_DOWN and current_row < len(MENU)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(MENU)-1:
                sys.exit(1)
            
            elif current_row == 0:
                return 0
            else:
                return 1
            
        print_menu(stdscr, current_row)