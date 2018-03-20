from PieceTile import PieceTile
from TileEnum import TileEnum

class Node:
    def __init__(self, board):
        self._whites_loc = []
        self._blacks_loc = []
        self._children = []
        self._state_heuristic = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == TileEnum.WHITE_PIECE:
                    self._whites_loc.append((i, j))
                elif board[i][j] == TileEnum.BLACK_PIECE:
                    self._blacks_loc.append((i, j))

    def get_white_loc(self):
        return self._whites_loc

    def get_black_loc(self):
        return self._blacks_loc

    def set_child(self, child_node):
        self._children.append(child_node)

    def get_children(self):
        return self._children

    def get_state_heuristic(self):
        return self._state_heuristic

    def set_state_heuristic(self, heuristic):
        self._state_heuristic = heuristic

    def get_node(self):
        tup = (0, 0)
        tup[0] = self._whites_loc
        tup[1] = self._blacks_loc
        return tup

    def __str__(self):
        message = 'Node white pieces location: '
        for loc in self._whites_loc:
            message += '(' + str(loc[0]) + ', ' + str(loc[1]) + '), '
        message = message[:-2]
        message += ' Node black pieces location: '
        for loc in self._blacks_loc:
            message += '(' + str(loc[0]) + ', ' + str(loc[1]) + '), '
        message = message[:-2]
        message += ' node heuristic: ' + str(self._state_heuristic)
        return message
