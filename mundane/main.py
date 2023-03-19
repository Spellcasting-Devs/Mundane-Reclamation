import before.menu_loader as menu_loader
import before.cfg_player_opartions as cfg_player_opartions
import configparser
from before.cfg_edit import config_read
from os.path import abspath, dirname


""" GAME LIFE CYCLE
- load menu and wait for operation
- load player data to player 
- load game data to game
- load the current state of the game 
"""


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
        game_config = configparser.ConfigParser()
        game_config.read(PATH_PLAYERS + file)
        
        # storing chapter progression data in self.data
        chapters = ['CHAPTER1']
        self.data = {}
        for chapter in chapters:
            self.data[chapter] = {}
            for key, value in game_config.items(chapter):
                self.data[chapter][key] = value
      
    
def player_data_injector(o):
    if o == 0:
        player_name = cfg_player_opartions.create_player()
        player_file = player_name + '.ini'
    else:
        player_file = cfg_player_opartions.load_player()
        
    global player
    player = Player(player_file) # creating player object with player data from config
    
    global game
    game = Game(player_file) # creating game object with game state data from config
    
    
def player_progression_loader():
    pass
    
    
def main():
    operation = menu_loader.load_menu() # loading the menu and wait for player operation
    player_data_injector(operation) # create / load player config file based on operation -> initiates player and game class objects and loads player data


if __name__ == '__main__':
    main()
    