import curses

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # get screen size
    sh, sw = stdscr.getmaxyx()

    # create player character
    player = '@'
    player_y = sh // 2
    player_x = sw // 2

    # draw player character
    stdscr.addstr(player_y, player_x, player)

    # game loop
    while True:
        # get user input
        key = stdscr.getch()

        # move player character based on user input
        if key == curses.KEY_UP:
            player_y = max(player_y - 1, 0)
        elif key == curses.KEY_DOWN:
            player_y = min(player_y + 1, sh - 1)
        elif key == curses.KEY_LEFT:
            player_x = max(player_x - 1, 0)
        elif key == curses.KEY_RIGHT:
            player_x = min(player_x + 1, sw - 1)

        # redraw player character
        stdscr.clear()
        stdscr.addstr(player_y, player_x, player)

        # refresh screen
        stdscr.refresh()

# run the game
curses.wrapper(main)

if __name__ == '__main__':
    main()