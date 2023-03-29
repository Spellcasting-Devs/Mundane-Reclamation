import configparser
import before.menu as menu
import before.player as player
import levels.intro as intro
from os.path import abspath, dirname


CHAPTERS = ['INTRO', 'CHAPTER1']
PATH_PLAYERS = f"{dirname(abspath(__file__))}/config/players/"
config = configparser.ConfigParser()


class Player:
    def __init__(self, file):
        config.read(PATH_PLAYERS + file)
        
        self.config_file = PATH_PLAYERS + file
        self.name = config.get('CONSTANTS', 'player_name')
        self.race = config.get('CONSTANTS', 'player_race')
        self.health = config.get('VARIABLES', 'health')
        self.mana = config.get('VARIABLES', 'mana')
        self.strength = config.get('VARIABLES', 'strength')
    
    def get_stats(self):
        print(self.name, self.race, self.health, self.mana, self.strength)


class Game:
    def __init__(self, file):
        config.read(PATH_PLAYERS + file)
        
        self.config_file = PATH_PLAYERS + file
        self.data = {}
        self.checkpoint_file_location = ""
                
        for chapter in CHAPTERS:
            self.data[chapter] = {}
            for key, value in game_config.items(chapter):
                self.data[chapter][key] = value
                          
    def get_checkpoint_current(self): # returns the current, uncompleted checkpoint
        for chapter in self.data:        
            for section in self.data[chapter]:
                if self.data[chapter][section] == "False":
                    self.checkpoint_file_location = f"{dirname(abspath(__file__))}/levels/{chapter.lower()}/{section}" # chapter and sections directories have to follow a naming format!
                    return chapter.upper(), section # for example 'CHAPTER1' 'c2' -> this is how directories have to be named
                
    def set_checkpoint_enabled(self, chapter, section):
        config.read(self.config_file)
        config[chapter][section] = "True"
        
        with open(self.config_file, "w") as configfile:
            config.write(configfile)
        
      
    
def player_data_injector(o):
    if o == 0: # new game
        username = intro.dialog('intro.txt', True)
        race = intro.set_player_race()
        player.create_player(username, race)
        player_file = username + '.ini'
    else: # load game
        player_file = player.load_player()
        
    return player_file
   
    
def main():
    operation = menu.load_menu() # loading the menu and wait for player operation
    player_file = player_data_injector(operation) # create / load player config file based on operation -> initiates player and game class objects and loads player data
    
    global player
    player = Player(player_file) # creating player object with player data from config
    
    global game
    game = Game(player_file) # creating game object with game state data from config
    
    chapter, checkpoint = game.get_checkpoint_current() # chapter and section represent the revelvant checkpoint for the player

    # TODO: Put the player at his current checkpoint
    # I though about creating a file structure like levels/chapter1/c1 representing the current chapter and checkpoint
    # We could store any relevant ressources for each chapter in a dedicated location 
    # This would provide a structure and enables us to pull the content that is needed from the directories
    # To makes this work, all files would have to follow a strict naming convention
  
    
if __name__ == '__main__':
    main()
