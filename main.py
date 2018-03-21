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
    board_max_man_dist = 2 * BOARD_SIZE * len(start.get_board().get_white_pieces_loc())

    print(str(start))
    start.expand_white_moves()
    count_child = 1
    for node in start.get_children():
        print(str(count_child), str(node), board_max_man_dist-node.get_total_cost())
        count_child += 1
#    frontier=PriorityQueue()
#    frontier.put((0,start))
#    while not frontier.empty():
#        current=frontier.get()
#        if(current[1].board.is_goal()):      ##isgoal needs implementation
            ###game is won. Break, backtrack and print.
#        current.expand_white_moves(current[2].board.get_white_moves())  #expand tree to include children of current node representing board configurations after all possible white moves
#        for child in current.get_children():
#            frontier.put((child.cost_so_far+child.est_cost,child))  #add these children into the priority queue using internal heuristic man_distance value


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
                    row_input = '- - - - - O O -'
                elif i == 3:
                    row_input = '- - - - @ O - -'
                elif i == 4:
                    row_input = '- - - - - - - -'
                elif i == 5:
                    row_input = '- - - - - O - -'
                elif i == 6:
                    row_input = '- - - - @ - @ @'
                else:
                    row_input = 'X - - - - - - X'
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