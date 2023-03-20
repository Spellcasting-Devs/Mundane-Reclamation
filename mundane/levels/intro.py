import time
import sys
import os
from os.path import abspath, dirname

# FIXME: fuse load_intro_dialog and load_text_dialog later

TEXT_FILE_PATH = f"{dirname(abspath(__file__))}/text/"


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")
    

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def load_intro_dialog(txt):
    clear_screen()
    with open(TEXT_FILE_PATH + txt) as f:
        for line in f.read().splitlines():
            line += "\n"
            if line.startswith("\n"):
                input("\n\nCONTINUE...")
                clear_screen()
            type_text(line)
            
        username = create_username()
        return username
  
        
def load_text_dialog(txt):
    clear_screen()
    with open(TEXT_FILE_PATH + txt) as f:
        for line in f.read().splitlines():
            line += "\n"
            if line.startswith("\n"):
                input("\n\nCONTINUE...")
                clear_screen()
            type_text(line)
        
        
def create_username():
    print("\nSo, what name will thou have?")
   
    while True:
        username = str(input(": "))
        
        if len(username) in range(3, 20):
            break
        else:
            print("This username can not be taken, please try again.")
            
    return username


def c1():
    load_text_dialog('intro_0.txt')
    
    # do intro checkpoint stuff here 
    # if done, mark checkpoint as completed, then load next