from configparser import ConfigParser
from os.path import (dirname, abspath)

# maybe move this file somewhere else

FILEPATH = f"{dirname(abspath(__file__))}/../players"



"""
This file would be used to easily read and write data from and to the player config files
"""



# writes values to keys of selected section
def config_write(name, section, key, value):
    cfg = ConfigParser()
    cfg.read(f"{FILEPATH}/{name}.ini")
    cfg.set(section, key, value)

    with open(f"{FILEPATH}/{name}.ini", 'w+') as cfgfile:
        cfg.write(cfgfile)
        cfgfile.flush()


def config_read(name, section, key):
    cfg = ConfigParser()
    cfg.read(f"{FILEPATH}/{name}.ini")

    return cfg.get(section, key)


# this is how you would read values from existing files, you submit a name, section and key
player_name = config_read('tester', 'CONSTANTS', 'player_name')
print(player_name)

# config_write(name, section, key, value) is how you would write stuff to existing files, changing variables on the way