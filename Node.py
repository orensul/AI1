

class Node:
    """
    This class of Node contains the information of node in the search tree.
    each node contains board_state, his parent, children and of course the heuristic cost.
    """
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

    def get_board(self):
        return self._board

    def get_children(self):
        return self._children

    def get_parent(self):
        return self._parent

    def get_move(self):
        return self._move

    def get_total_cost(self):
        return self._cost_so_far + self._est_cost_to_goal

    def is_nodes_same(self, other_node):
        return self._board.is_board_states_same(other_node.get_board())

    def expand_white_moves(self):
        """
        Set the children attribute of the class all of the children of this node according to the optional new moves
        we can take, each new move will produce a new node which is a new board state.
        :return:
        """
        white_moves = self._board.get_white_moves()
        for move in white_moves:
            new_board_state = self._board.update(move)
            new_board_state.delete_white_surrounded()
            new_board_state.delete_black_surrounded()

            # each move is a cost of 1 so each child node has a cost_so_far 1 more than their parent
            self._children.append(Node(new_board_state, self, move, self._cost_so_far + 1))

    def __str__(self):
        """
        toString for Node class
        :return: string representation of Node
        """
        message = 'Node white pieces location: '
        for loc in self._board.get_white_pieces_loc():
            message += str(loc)
        message += ' Node black pieces location: '
        for loc in self._board.get_black_pieces_loc():
            message += str(loc)
        message += ' priority: ' + str(self.get_total_cost())
        return message
