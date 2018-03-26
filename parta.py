import sys
import os
import Game


class parta:
    """
        main class which gets input from command line and calls game to start the game.
    """

    def main():

        file_name = os.path.abspath(sys.argv[1])
        Game.Game(file_name)

    if __name__ == "__main__":
        main()