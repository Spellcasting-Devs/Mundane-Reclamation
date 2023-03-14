import before.menu_loader as menu_loader
import before.cfg_player_opartions as cfg_player_opartions
from before.cfg_edit import (config_read)




class Player:
    def __init__(self, file):
        self.name = config_read(file, 'CONSTANTS', 'player_name')
        self.health = config_read(file, 'VARIABLES', 'health')
        self.mana = config_read(file, 'VARIABLES', 'mana')
        self.strength = config_read(file, 'VARIABLES', 'strength')
    
    def get_stats(self):
        print(self.name, self.health, self.mana, self.strength)
        
    
def player_data_injector(o):
    if o == 0:
        player_name = cfg_player_opartions.create_player()
        player_file = player_name + '.ini'
    else:
        player_file = cfg_player_opartions.load_player()
        
    global player
    player = Player(player_file) # the current player object with injected game data
    
    
def main():
    operation = menu_loader.load_menu() # starts the menu
    player_data_injector(operation)
    player.get_stats()


if __name__ == '__main__':
    main()