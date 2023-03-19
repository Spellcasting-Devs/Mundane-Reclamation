import time
import sys
from os.path import abspath, dirname
import os


FILE_PATH = dirname(abspath(__file__))


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")
    

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def load_dialog():
    with open(FILE_PATH + "/text/intro.txt") as f:
        for line in f.read().splitlines():
            line += "\n"
            if line.startswith("\n"):
                input("\n\nCONTINUE...")
                clear_screen()
            type_text(line)
        

def main():
    load_dialog()



main()