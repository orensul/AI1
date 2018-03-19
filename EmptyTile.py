from Tile import Tile

class EmptyTile(Tile):
    def __init__(self, location):
        super().__init__(location)

    def __str__(self):
        return 'empty tile in location: ' + super().__str__()



