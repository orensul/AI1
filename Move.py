from Coordinate import Coordinate


class Move:
    """
    Move class is a collection of two Coordinate Objects representing the abstract idea of a move on the board_state
    created and used within the BoardState class
    """
    def __init__(self, a, b, c, d):
        self._begin = Coordinate(a, b)
        self._end = Coordinate(c, d)

    def get_begin(self):
        return self._begin

    def get_end(self):
        return self._end

    def __str__(self):
        message = str(self._begin) + ' -> ' + str(self._end)
        return message