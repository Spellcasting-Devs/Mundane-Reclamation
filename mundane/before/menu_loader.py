import curses
import os

from cfg_create_player import create_player


WIPE = os.system("clear") if os.name == "posix" else os.system("cls")
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
              


def load_menu():
    load_title_screen()
    return_code = curses.wrapper(main)
    WIPE
    
    if return_code == 0:
        create_player()
    else:
        pass


def load_title_screen():
    WIPE
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
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the MENU
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(MENU)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                return 0
            elif current_row == 1:
                return 1
            elif current_row == len(MENU)-1:
                break 
            
        print_menu(stdscr, current_row)
        
load_menu()
