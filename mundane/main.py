import before.menu_loader as menu_loader
import before.cfg_player_opartions as cfg_player_opartions
import configparser

import levels.intro.intro as intro

from before.cfg_edit import config_read
from os.path import abspath, dirname


""" GAME LIFE CYCLE
- load menu and wait for operation [x]
- load player data to player [x]
- load game data to game [x]
- load the current state of the game [x]
- position the player at the latest checkpoint []
"""

CHAPTERS = ['CHAPTER1']
PATH_PLAYERS = f"{dirname(abspath(__file__))}/config/players/"

class Player:
    def __init__(self, file):
        self.name = config_read(file, 'CONSTANTS', 'player_name')
        self.health = config_read(file, 'VARIABLES', 'health')
        self.mana = config_read(file, 'VARIABLES', 'mana')
        self.strength = config_read(file, 'VARIABLES', 'strength')
    
    def get_stats(self):
        print(self.name, self.health, self.mana, self.strength)


class Game:
    def __init__(self, file):
        self.data = {}
        self.checkpoint_file_location = ""
        
        # loading player progression data   
        game_config = configparser.ConfigParser()
        game_config.read(PATH_PLAYERS + file)
        
        for chapter in CHAPTERS:
            self.data[chapter] = {}
            for key, value in game_config.items(chapter):
                self.data[chapter][key] = value
                          
    def get_checkpoint_current(self): # returns the current, uncompleted checkpoint
        for chapter in self.data:        
            for section in self.data[chapter]:
                if self.data[chapter][section] == "False":
                    self.checkpoint_file_location = f"{dirname(abspath(__file__))}/levels/{chapter.lower()}/{section}" # chapter and sections directories have to follow a naming format!
                    return chapter.lower(), section # for example 'chapter1' 'c2' -> this is how directories have to be named
                
    def set_checkpoint_enabled(self, chapter, section):
        pass
      
    
def player_data_injector(o):
    if o == 0:
        username = intro.load_intro_dialog()
        cfg_player_opartions.create_player(username)
        player_file = username + '.ini'
    else:
        player_file = cfg_player_opartions.load_player()
        
    global player
    player = Player(player_file) # creating player object with player data from config
    
    global game
    game = Game(player_file) # creating game object with game state data from config
    
    
def main():
    operation = menu_loader.load_menu() # loading the menu and wait for player operation
    player_data_injector(operation) # create / load player config file based on operation -> initiates player and game class objects and loads player data
    chapter, section = game.get_checkpoint_current()


if __name__ == '__main__':
    main()
    