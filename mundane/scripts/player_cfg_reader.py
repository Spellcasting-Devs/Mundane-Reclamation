from configparser import ConfigParser
from os.path import (dirname, abspath)


FILEPATH = f"{dirname(abspath(__file__))}/../players"



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


player_name = config_read('tester', 'CONSTANTS', 'player_name')
print(player_name)