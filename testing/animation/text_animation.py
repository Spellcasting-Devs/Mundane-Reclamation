from time import sleep
from os import system, name as sysname

with open("forest_animation.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
f.close()

ascii_lines = lines[2:26]

truncated_ascii_lines = [line[:80] for line in ascii_lines]
system("clear") if sysname == "posix" else system("cls")

for line in truncated_ascii_lines:
    print(line)

sleep(5)

for x in range(220):
    print("\033[26A", end= "")
    print("\033[2K", end = "") # erase old line, return cursor to beginning
    truncated_ascii_lines = [line[x+1:80+x+1] for line in ascii_lines]
    sleep(0.04)
    for line in truncated_ascii_lines:
        print(line)
sleep(5)