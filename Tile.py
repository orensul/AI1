class Tile:
    def __init__(self, location):
        self._loc = location

    def __str__(self):
        return '(' + str(self._loc[0]) + ", " + str(self._loc[1]) + ')'

    def set_location(self, location):
        self._loc = location

    def get_location(self):
        return self._loc

