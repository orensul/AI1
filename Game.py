
from BoardState import BoardState
from Node import Node
from TileEnum import TileEnum
from queue import PriorityQueue


BOARD_SIZE = 8
WHITE_PIECE_SYM = 'O'
BLACK_PIECE_SYM = '@'
CORNER_SYM = 'X'
EMPTY_SYM = '-'
SPACE = ' '
NODE_IDX = 2
PRIO_IDX = 0



class Game:
    """
    This class drives the game
    """

    def __init__(self, file_name):
        """
        :param file_name:
        """
        self._file_name = file_name
        self._board, self._instruction = self.read_file()
        self._initial_board_state = BoardState(self._board)

        if self._instruction == 'Moves':
            white_moves = self._initial_board_state.get_white_moves()
            black_moves = self._initial_board_state.get_black_moves()
            print(str(len(white_moves)))
            print(str(len(black_moves)))
        else:
            start_state = Node(self._initial_board_state, None, None, 0)
            # start search from root node representative of initial board state
            self.a_star_search(start_state)

    def read_file(self):
        """
        read the file and return the board which is built by converting the symbols in the file.
        In addition, returns the instruction ("Moves" or "Massacre")
        :return:
        """
        board = []

        count_lines = 0
        file = open(self._file_name, 'r').read().splitlines()

        for row_input in file:
            row = []
            if count_lines < BOARD_SIZE:
                count_lines += 1
                for tile in row_input:
                    if tile == WHITE_PIECE_SYM:
                        row.append(TileEnum.WHITE_PIECE)
                    elif tile == BLACK_PIECE_SYM:
                        row.append(TileEnum.BLACK_PIECE)
                    elif tile == CORNER_SYM:
                        row.append(TileEnum.CORNER_TILE)
                    elif tile == EMPTY_SYM:
                        row.append(TileEnum.EMPTY_TILE)
                    elif tile == SPACE:
                        continue
            else:
                instruction = row_input
                return board, instruction

            board.append(row)



    def a_star_search(self, start):
        """
        Implementing the A* by using priority queue.
        :param start: start node
        :return:
        """
        # holds visited nodes so we will know to skip them if we will encounter them again
        visited_nodes = []

        leaves = PriorityQueue()
        leaves.put((0, 0, start))
        visited_nodes.append(start)
        count_nodes = 0
        while not leaves.empty():
            current = leaves.get()
            # if we arrived to the goal, we will backtracking on the tree to print all of the moves we made
            if current[NODE_IDX].get_board().is_goal():
                sequence = []
                traceback = current[NODE_IDX]
                while not traceback.get_parent() is None:
                    sequence.append(traceback.get_move())
                    traceback = traceback.get_parent()
                for move in sequence[::-1]:
                    print(str(move))
                return 0

            # expand tree to include children of current node representing board configurations after all
            # possible white moves
            current[NODE_IDX].expand_white_moves()
            visited_nodes.append(current[NODE_IDX])
            for child in current[NODE_IDX].get_children():
                if not self.is_already_visited(visited_nodes, child):
                    count_nodes += 1
                    # add these children into the priority queue using internal heuristic man_distance value
                    leaves.put((child.get_total_cost(), count_nodes, child))

    def is_already_visited(self, visited_nodes, current_node):
        """
        :param visited_nodes:
        :param current_node:
        :return: True if a node has been already visited, otherwise, False.
        """
        for node in visited_nodes:
            if current_node.is_nodes_same(node):
                return True
        return False


