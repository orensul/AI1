from PieceTile import PieceTile
from CornerTile import CornerTile
from EmptyTile import EmptyTile
from WrongNumberOfTilesException import WrongNumberOfTilesException
from WrongSymbolException import WrongSymbolException
from WrongInput import WrongInput
from Node import Node
from TileEnum import TileEnum
import copy
import math
import numpy

NUMBER_OF_ROWS = 8
ROW_LEN = 8
WHITE_PIECE_SYM = 'O'
BLACK_PIECE_SYM = '@'
CORNER_SYM = 'X'
EMPTY_SYM = '-'
SPACE = ' '


board = []

def main():
    try:
        debug = 1
        for i in range(NUMBER_OF_ROWS):
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
                    ROW_LEN) + ' tiles which contains only - O X @ :')
            if len(row_input) < ROW_LEN:
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

        row_input = input('please specify "moves" or "massacre": ')
        if (row_input != 'moves' and row_input!= 'massacre'):
            raise WrongInput
        if (row_input == 'moves'):
            legal_white_moves , legal_black_moves = count_moves()
            print(legal_white_moves, legal_black_moves)
        else:
            build_search_tree()

    except WrongNumberOfTilesException:
        print ("Wrong number of tiles, you should supply " + str(ROW_LEN) + ' tiles')
    except WrongSymbolException:
        print("Wrong symbol of a tile, you should supply only one of these: X - O @")
    except WrongInput:
        print("Wrong input")

def build_search_tree():
    node = Node(board)

    print("root node: ")
    print(node)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == TileEnum.WHITE_PIECE:
                count, legal_new_pos = count_legal_moves_pos((i, j))
                for new_pos in legal_new_pos:
                    child_node = create_child((i, j), new_pos)
                    child_node.set_state_heuristic(1+calc_heuristic_for_board_state(create_board_state_node(child_node)))
                    node.set_child(child_node)
                    print(child_node)





def create_board_state_node(node):
    board_state = []
    for i in range(ROW_LEN):
        row_list = []
        for j in range(ROW_LEN):
            row_list.append(0)
        board_state.append(row_list)


    for pos in node.get_white_loc():
        i = pos[0]
        j = pos[1]
        board_state[i][j] = TileEnum.WHITE_PIECE

    for pos in node.get_black_loc():
        i = pos[0]
        j = pos[1]
        board_state[i][j] = TileEnum.BLACK_PIECE

    board_state[0][0] = TileEnum.CORNER_TILE
    board_state[0][ROW_LEN-1] = TileEnum.CORNER_TILE
    board_state[ROW_LEN-1][0] = TileEnum.CORNER_TILE
    board_state[ROW_LEN-1][ROW_LEN-1] = TileEnum.CORNER_TILE

    for i in range(ROW_LEN):
        for j in range(ROW_LEN):
            if not board_state[i][j] in (TileEnum.WHITE_PIECE, TileEnum.BLACK_PIECE, TileEnum.CORNER_TILE):
                board_state[i][j] = TileEnum.EMPTY_TILE


    return board_state

def get_list_black_pos(board_state):
    black_pos = []
    for i in range(len(board_state)):
        for j in range(len(board_state)):
            if board_state[i][j] == TileEnum.BLACK_PIECE:
                black_pos.append((i, j))
    return black_pos


def calc_heuristic_for_board_state(board_state):
    total_heuristic = 0
    for i in range(len(board_state)):
        for j in range(len(board_state)):
            if board_state[i][j] == TileEnum.WHITE_PIECE:
                min_manhattan_distance = ROW_LEN + ROW_LEN
                for black_pos in get_list_black_pos(board_state):
                    curr_distance = manhattan_distance((i, j), black_pos)
                    if min_manhattan_distance >= curr_distance:
                        min_manhattan_distance = curr_distance
                total_heuristic += min_manhattan_distance
    return total_heuristic



def manhattan_distance(source_pos, dest_pos):
    return math.fabs(source_pos[0] - dest_pos[0]) + math.fabs(source_pos[1] - dest_pos[1])


def create_child(old_pos, new_pos):
    old_pos_row = old_pos[0]
    old_pos_col = old_pos[1]
    new_pos_row = new_pos[0]
    new_pos_col = new_pos[1]

    copy_board = copy.deepcopy(board)

    temp_tile = copy_board[new_pos_row][new_pos_col]

    copy_board[new_pos_row][new_pos_col] = copy_board[old_pos_row][old_pos_col]
    copy_board[old_pos_row][old_pos_col] = temp_tile

    return Node(copy_board)



def count_moves():
    count_white_moves = 0
    count_black_moves = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == TileEnum.WHITE_PIECE:
                count, move_new_pos = count_legal_moves_pos((i, j))
                count_white_moves += count
            elif board[i][j] == TileEnum.BLACK_PIECE:
                count, move_new_pos = count_legal_moves_pos((i, j))
                count_black_moves += count

    return count_white_moves, count_black_moves


def check_left_move(loc):

    left_move_new_pos = []
    legal_moves = 0
    row = loc[0]
    col = loc[1]
    if col > 0:
        if board[row][col - 1] == TileEnum.EMPTY_TILE:
            left_move_new_pos.append((row, col - 1))
            legal_moves += 1
        elif board[row][col - 1] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
            if col - 1 > 0:
                if board[row][col - 2] == TileEnum.EMPTY_TILE:
                    left_move_new_pos.append((row, col - 2))
                    legal_moves += 1
    return legal_moves, left_move_new_pos

def check_up_move(loc):
    up_move_new_pos = []
    legal_moves = 0
    row = loc[0]
    col = loc[1]
    if row > 0:
        if board[row - 1][col] == TileEnum.EMPTY_TILE:
            up_move_new_pos.append((row - 1, col))
            legal_moves += 1
        elif board[row - 1][col] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
            if row - 1 > 0:
                if board[row - 2][col] == TileEnum.EMPTY_TILE:
                    up_move_new_pos.append((row - 2, col))
                    legal_moves += 1
    return legal_moves, up_move_new_pos


def check_right_move(loc):

    right_move_new_pos = []
    legal_moves = 0
    row = loc[0]
    col = loc[1]
    if col < ROW_LEN - 1:
        if board[row][col + 1] == TileEnum.EMPTY_TILE:
            right_move_new_pos.append((row, col + 1))
            legal_moves += 1
        elif board[row][col + 1] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
            if col + 1 < ROW_LEN - 1:
                if board[row][col + 2] == TileEnum.EMPTY_TILE:
                    right_move_new_pos.append((row, col + 2))
                    legal_moves += 1
    return legal_moves, right_move_new_pos

def check_down_move(loc):
    down_move_new_pos = []
    legal_moves = 0
    row = loc[0]
    col = loc[1]
    if row < ROW_LEN - 1:
        if board[row + 1][col] == TileEnum.EMPTY_TILE:
            legal_moves += 1
            down_move_new_pos.append((row + 1, col))
        elif board[row + 1][col] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
            if row + 1 < ROW_LEN - 1:
                if board[row + 2][col] == TileEnum.EMPTY_TILE:
                    legal_moves += 1
                    down_move_new_pos.append((row + 2, col))
    return legal_moves, down_move_new_pos

def count_legal_moves_pos(loc):
    legal_moves = 0
    move_new_pos = []

    count_right_moves, right_move_new_pos = check_right_move(loc)
    legal_moves += count_right_moves

    count_left_moves, left_move_new_pos = check_left_move(loc)
    legal_moves += count_left_moves

    count_up_moves, up_move_new_pos = check_up_move(loc)
    legal_moves += count_up_moves

    count_down_moves, down_move_new_pos = check_down_move(loc)
    legal_moves += count_down_moves

    move_new_pos = right_move_new_pos + left_move_new_pos + up_move_new_pos + down_move_new_pos

    return legal_moves, move_new_pos

main()