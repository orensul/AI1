#Move class is a collection of two Coordinate Objects representing the abstract idea of a move on the board_state
#created and used within the BoardState class
from Coordinate import Coordinate
class Move:
    def __init__(self, a,b,c,d):
        self.begin=Coordinate(a,b)
        self.end=Coordinate(c,d)

    def get_begin(self):
        return self.begin

    def get_end(self):
        return self.end

    def __str__(self):
        message='From: '+str(self.begin)+' to '+str(self.end)
        return message
