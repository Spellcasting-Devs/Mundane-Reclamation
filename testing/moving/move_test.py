import curses



def main(stdscr):
    # Initialize screen
    screen = curses.initscr()

    # Turn off cursor visibility
    curses.curs_set(0)

    # Enable keypad mode
    screen.keypad(1)

    # Create game window
    game_win = curses.newwin(20, 40, 0, 0) # change map dimensions here

    # Set window attributes
    game_win.nodelay(True)  # Set non-blocking mode
    game_win.box()

    # Create character object
    char = {'y': 10, 'x': 20, 'char': '@'} # change player starting position here

    # Draw initial game window
    game_win.addstr(char['y'], char['x'], char['char'])
    game_win.refresh()

    # Enter game loop
    while True:
        # Read input
        key = game_win.getch()
        if key == ord('w') and char['y'] > 1:
            char['y'] -= 1
        elif key == ord('s') and char['y'] < 18:
            char['y'] += 1
        elif key == ord('a') and char['x'] > 1:
            char['x'] -= 1
        elif key == ord('d') and char['x'] < 38:
            char['x'] += 1
        
        # Check if player made a move
        if key != -1:
            # Clear and redraw game window
            game_win.clear()
            game_win.box()
            game_win.addstr(char['y'], char['x'], char['char'])
            game_win.refresh()
        
        # Exit loop if player reaches end of game
        if char['x'] == 39:
            break

    # End game
    curses.endwin()
    
curses.wrapper(main)