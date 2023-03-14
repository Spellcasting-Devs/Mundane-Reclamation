import before.menu_loader as menu_loader
import before.cfg_create_player as cfg_create_player


def menu_operations():
    operation = menu_loader.load_menu()
    
    if operation == 0:
        cfg_create_player.create_player() # create new player config 
        # start game dialog after this?
    else:
        pass
    
    
def main():
    menu_operations()


if __name__ == '__main__':
    main()