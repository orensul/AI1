
from Tile import Tile


class PieceTile(Tile):
    WHITE_COLOR = 'white'
    BLACK_COLOR = 'black'

    def __init__(self, location, color):
        """
        Constructor for a new piece in the board.
        :param location: tuple (x,y) location of the piece in the board, y = row, x = column
        :param color: empty or black or white
        """
        super().__init__(location)
        self._color = color

    def __str__(self):
        return 'piece tile in location: ' + super().__str__() + '  color: ' + self._color


    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def move(self):
        pass
