

class Node:
    def __init__(self, board_state, parent, move, cost):
        # current state of the board this node represents
        self._board = board_state
        # cost it has taken to get down to this node on the tree so far
        self._cost_so_far = cost
        # parent node, used to traverse up sequence of nodes once goal state found
        self._parent = parent
        # heuristic score for A* search
        self._est_cost_to_goal = self._board.sum_man_distance()
        # Collection of child nodes produced by moving white pieces, only filled when node is expanded in A* search
        self._children = []
        # Move that translates parent node state to this current node state. Useful in output of massacre method.
        self._move = move

    def get_children(self):
        return self._children

    def expand_white_moves(self):
        white_moves = self._board.get_white_moves()
        for move in white_moves:
            new_board_state = self._board.update(move)
            # each move is a cost of 1 so each child node has a cost_so_far 1 more than their parent
            self._children.append(Node(new_board_state, self._board, move, self._cost_so_far + 1))

    def __str__(self):
        message = 'Node white pieces location: '
        for loc in self._board.get_white_pieces_loc():
            message += str(loc)
        message += ' Node black pieces location: '
        for loc in self._board.get_black_pieces_loc():
            message += str(loc)
        message += ' node heuristic: ' + str(self._est_cost_to_goal)
        return message
