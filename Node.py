from PieceTile import PieceTile


class Node:
    def __init__(self, board):
        self._whites_loc = []
        self._blacks_loc = []
        self._children = []
        for row in board:
            for tile in row:
                if isinstance(tile, PieceTile):
                    if tile.get_color() == PieceTile.WHITE_COLOR:
                        self._whites_loc.append(tile.get_location())
                    else:
                        self._blacks_loc.append(tile.get_location())

    def set_child(self, child_node):
        self._children.append(child_node)

    def get_node(self):
        tup = (0, 0)
        tup[0] = self._whites_loc
        tup[1] = self._blacks_loc
        return tup

    def __str__(self):
        message = ''
        print("Node white pieces location:")
        for loc in self._whites_loc:
            message += '(' + str(loc[0]) + ', ' + str(loc[1]) + '), '
        message = message[:-2]
        message += '\nNode black pieces location: \n'
        for loc in self._blacks_loc:
            message += '(' + str(loc[0]) + ', ' + str(loc[1]) + '), '
        message = message[:-2]
        return message
