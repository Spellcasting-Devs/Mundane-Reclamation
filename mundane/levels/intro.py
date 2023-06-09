import time
import sys
import os
import curses
from os.path import abspath, dirname


TEXT_PATH = f"{dirname(abspath(__file__))}/text/intro/"
ROLES = [
    'Human',
    'Elven',
    'Halfling',
    'Dwarven',
    'Berserkers',
    'Tiefling',
    'Fennak',
    'Tabaxi',
    'Kobold',
    'Dragonborn',
    'Exit'
]



def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")
    

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def dialog(txt, intro=False):
    clear_screen()
    with open(TEXT_PATH + txt) as f:
        for line in f.read().splitlines():
            line += "\n"
            if line.startswith("\n"):
                input("\n\nCONTINUE...")
                clear_screen()
            type_text(line)
            
        if intro:
            username = set_name()
            return username

  
def set_name():
    print("\nSo, what name will thou have? ('exit' to close the game)")
   
    while True:
        username = str(input(": "))
        
        if username.lower() == 'exit':
            sys.exit(1)
        elif len(username) in range(3, 20):
            break
        else:
            print("This username can not be taken, please try again.")
            
    return username
  

def set_role():
    dialog('intro_roles.txt')
    role = curses.wrapper(main)
    
    if role == 10:
        sys.exit(1)
  
    return ROLES[role]


def intro_end(username, role):
    print(f"So, your name is... {username}.\nAnd your race is... {role}.\n")
    input("CONTINUE...")
    dialog('intro_0.txt')


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(ROLES):
        x = w//2 - len(row)//2
        y = h//2 - len(ROLES)//2 + idx
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
        elif key == curses.KEY_DOWN and current_row < len(ROLES)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(ROLES)-1:
                sys.exit(1)
            else:
                return current_row
            
        print_menu(stdscr, current_row)
