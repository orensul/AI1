from Tile import Tile

class CornerTile(Tile):
    def __init__(self, location):
        super().__init__(location)

    def __str__(self):
        return 'corner tile in location: ' + super().__str__()



