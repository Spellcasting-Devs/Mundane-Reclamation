from configparser import ConfigParser
from os.path import (dirname, abspath)


# TODO: Create list of config paths for different settings / config files
PATH_PLAYERS = f"{dirname(abspath(__file__))}/../config/players/"


# TODO: Create path check
def config_write(name, section, key, value):
    cfg = ConfigParser()
    cfg.read(f"{PATH_PLAYERS}{name}.ini")
    cfg.set(section, key, value)

    with open(f"{PATH_PLAYERS}{name}.ini", 'w+') as cfgfile:
        cfg.write(cfgfile)
        cfgfile.flush()


def config_read(name, section, key):
    cfg = ConfigParser()
    cfg.read(f"{PATH_PLAYERS}{name}.ini")

    return cfg.get(section, key)
