import time
import sys
import os
from os.path import abspath, dirname



FILE_PATH = dirname(abspath(__file__))


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")
    

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def load_intro_dialog():
    clear_screen()
    with open(FILE_PATH + "/text/intro.txt") as f:
        for line in f.read().splitlines():
            line += "\n"
            if line.startswith("\n"):
                input("\n\nCONTINUE...")
                clear_screen()
            type_text(line)
            
        username = create_username()
        return username
        
        
def create_username():
    print("\nSo, what name will thou have?")
   
    while True:
        username = str(input(": "))
        
        if len(username) in range(3, 20):
            break
        else:
            print("This username can not be taken, please try again.")
            
    return username