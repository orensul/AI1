
class Coordinate:
    """
    Coordinate class simply represents a location on the board. Used to simplify storage of locations
    """
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def __str__(self):
        message = '(col, row): (' + str(self._column) + ' ,' + str(self._row) + ') '
        return message