from WrongNumberOfTilesException import WrongNumberOfTilesException
from WrongSymbolException import WrongSymbolException
from WrongInput import WrongInput
from BoardState import BoardState
from Coordinate import Coordinate
from Move import Move
from Node import Node
from TileEnum import TileEnum
import copy
from queue import PriorityQueue

BOARD_SIZE = 8
WHITE_PIECE_SYM = 'O'
BLACK_PIECE_SYM = '@'
CORNER_SYM = 'X'
EMPTY_SYM = '-'
SPACE = ' '

NODE_IDX = 2
PRIO_IDX = 0


def main():
    # separated console input retrieval into separate method. Build BoardState object from the list of lists
    board = BoardState(getBoardInput())

    try:
        row_input = input('please specify "moves" or "massacre": ')
        if row_input != 'moves' and row_input!= 'massacre':
            raise WrongInput

        if row_input == 'moves':
            white_moves = board.get_white_moves()
            black_moves = board.get_black_moves()
            print(str(len(white_moves)))
            print(str(len(black_moves)))
        else:
            start_state = Node(board, None, None, 0)
            # start search from root node representative of initial board state
            a_star_search(start_state)
    except WrongInput:
        print("Wrong input")

def a_star_search(start):

    visited_nodes = []
    # print(str(start))
    # start.expand_white_moves()
    # count_child = 1
    # for node in start.get_children():
    #     print(str(count_child), str(node), node.get_total_cost())
    #     count_child += 1

    leaves = PriorityQueue()
    leaves.put((0, 0, start))
    visited_nodes.append(start)
    count_nodes = 0
    while not leaves.empty():
        current = leaves.get()

        print("black pieces")
        print(len(current[NODE_IDX].get_board().get_black_pieces_loc()))
        if current[NODE_IDX].get_board().is_goal():
            sequence = []
            traceback = current[NODE_IDX]
            while not traceback.get_parent() is None:
                sequence.append(traceback.get_move())
                traceback = traceback.get_parent()
            print("list")
            for move in sequence[::-1]:
                print(str(move))
            return 0

        # expand tree to include children of current node representing board configurations after all
        # possible white moves
        current[NODE_IDX].expand_white_moves()
        visited_nodes.append(current[NODE_IDX])
        for child in current[NODE_IDX].get_children():
            if not is_already_visited(visited_nodes, child):
                count_nodes += 1
                # add these children into the priority queue using internal heuristic man_distance value
                leaves.put((child.get_total_cost(), count_nodes, child))
                print(child)
        #print(leaves.qsize())


def is_already_visited(visited_nodes, current_node):
    for node in visited_nodes:
        if current_node.is_nodes_same(node):
            return True
    return False

def getBoardInput():
    try:
        board = []
        debug = 1
        for i in range(BOARD_SIZE):
            row = []
            counter_of_tiles_in_row = 0
            if debug:
                if i == 0:
                    row_input = 'X - - - - - - X'
                elif i == 1:
                    row_input = '- - - - - - - -'
                elif i == 2:
                    row_input = '- - - - - - - -'
                elif i == 3:
                    row_input = '- - - 0 - 0 - -'
                elif i == 4:
                    row_input = '- - - - - - - -'
                elif i == 5:
                    row_input = '- - - - 0 - - -'
                elif i == 6:
                    row_input = '- - - - - - - -'
                else:
                    row_input = 'X - - - 0 - - X'

            else:
                row_input = input('row no. ' + str(i) + ' : please write a text of row of ' + str(
                    BOARD_SIZE) + ' tiles which contains only - O X @ :')
            if len(row_input) < BOARD_SIZE:
                raise WrongNumberOfTilesException
            else:
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
                        raise WrongSymbolException
                    counter_of_tiles_in_row += 1
            board.append(row)
        return board

    except WrongNumberOfTilesException:
        print("Wrong number of tiles, you should supply " + str(BOARD_SIZE) + ' tiles')
    except WrongSymbolException:
        print("Wrong symbol of a tile, you should supply only one of these: X - O @")


main()