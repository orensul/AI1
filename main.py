from PieceTile import PieceTile
from CornerTile import CornerTile
from EmptyTile import EmptyTile
from WrongNumberOfTilesException import WrongNumberOfTilesException
from WrongSymbolException import WrongSymbolException
from WrongInput import WrongInput
from Node import Node
import copy

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
                    row_input = '- - - - - O - -'
                elif i == 3:
                    row_input = '- - - - @ O - -'
                elif i == 4:
                    row_input = '- - - - - - O -'
                elif i == 5:
                    row_input = '- - - - - O @ -'
                elif i == 6:
                    row_input = '- - - - - - - @'
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
                        white_piece = PieceTile((counter_of_tiles_in_row, i), PieceTile.WHITE_COLOR)
                        row.append(white_piece)
                    elif tile == BLACK_PIECE_SYM:
                        black_piece = PieceTile((counter_of_tiles_in_row, i), PieceTile.BLACK_COLOR)
                        row.append(black_piece)
                    elif tile == CORNER_SYM:
                        corner = CornerTile((counter_of_tiles_in_row, i))
                        row.append(corner)
                    elif tile == EMPTY_SYM:
                        empty = EmptyTile((counter_of_tiles_in_row, i))
                        row.append(empty)
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
            print(board)
            build_search_tree()

    except WrongNumberOfTilesException:
        print ("Wrong number of tiles, you should supply " + str(ROW_LEN) + ' tiles')
    except WrongSymbolException:
        print("Wrong symbol of a tile, you should supply only one of these: X - O @")
    except WrongInput:
        print("Wrong input")

def build_search_tree():
    node = Node(board)


    for row in board:
        for tile in row:
            if isinstance(tile, PieceTile):
                if tile.get_color() == PieceTile.WHITE_COLOR:
                    count, legal_new_pos = count_legal_moves_pos(tile.get_location())
                    for new_pos in legal_new_pos:
                        create_child(tile.get_location(), new_pos)


def create_child(old_pos, new_pos):
    old_pos_row = old_pos[1]
    old_pos_col = old_pos[0]
    new_pos_row = new_pos[1]
    new_pos_col = new_pos[0]

    copy_board = copy.deepcopy(board)

    temp_tile = copy_board[new_pos_row][new_pos_col]
    copy_board[new_pos_row][new_pos_col] = copy_board[old_pos_row][old_pos_col]
    copy_board[old_pos_row][old_pos_col] = temp_tile

    copy_board[old_pos_row][old_pos_col].set_location((old_pos_row, old_pos_col))
    copy_board[new_pos_row][new_pos_col].set_location((new_pos_row, new_pos_col))

    print("original board old loc")
    print(old_pos_row)
    print(old_pos_col)
    print(board[old_pos_row][old_pos_col])
    print("\n")
    print("new board old loc")
    print(copy_board[old_pos_row][old_pos_col])
    print("\n")


    print("original board new loc")
    print(board[new_pos_row][new_pos_col])
    print("\n")


    print("mew board new loc")
    print(copy_board[new_pos_row][new_pos_col])

def count_moves():
    count_white_moves = 0
    count_black_moves = 0
    for row in board:
        for tile in row:
            if isinstance(tile, PieceTile):
                if tile.get_color() == PieceTile.WHITE_COLOR:
                    count, move_new_pos = count_legal_moves_pos(tile.get_location())
                    count_white_moves += count
                else:
                    count, move_new_pos = count_legal_moves_pos(tile.get_location())
                    count_black_moves += count
    return count_white_moves, count_black_moves


def check_left_move(loc):

    left_move_new_pos = []
    legal_moves = 0
    row = loc[1]
    col = loc[0]
    if col > 0:
        if isinstance(board[row][col - 1], EmptyTile):
            left_move_new_pos.append((col - 1, row))
            legal_moves += 1
        elif isinstance(board[row][col - 1], PieceTile):
            if col - 1 > 0:
                if isinstance(board[row][col - 2], EmptyTile):
                    left_move_new_pos.append((col - 2, row))
                    legal_moves += 1
    return legal_moves, left_move_new_pos

def check_up_move(loc):
    up_move_new_pos = []
    legal_moves = 0
    row = loc[1]
    col = loc[0]
    if row > 0:
        if isinstance(board[row - 1][col], EmptyTile):
            up_move_new_pos.append((col, row - 1))
            legal_moves += 1
        elif isinstance(board[row - 1][col], PieceTile):
            if row - 1 > 0:
                if isinstance(board[row - 2][col], EmptyTile):
                    up_move_new_pos.append((col, row - 2))
                    legal_moves += 1
    return legal_moves, up_move_new_pos


def check_right_move(loc):

    right_move_new_pos = []
    legal_moves = 0
    row = loc[1]
    col = loc[0]
    if col < ROW_LEN - 1:
        if isinstance(board[row][col + 1], EmptyTile):
            right_move_new_pos.append((col + 1, row))
            legal_moves += 1
        elif isinstance(board[row][col + 1], PieceTile):
            if col + 1 < ROW_LEN - 1:
                if isinstance(board[row][col + 2], EmptyTile):
                    right_move_new_pos.append((col + 2, row))
                    legal_moves += 1
    return legal_moves, right_move_new_pos

def check_down_move(loc):
    down_move_new_pos = []
    legal_moves = 0
    row = loc[1]
    col = loc[0]
    if row < ROW_LEN - 1:
        if isinstance(board[row + 1][col], EmptyTile):
            legal_moves += 1
            down_move_new_pos.append((col, row + 1))
        elif isinstance(board[row + 1][col], PieceTile):
            if row + 1 < ROW_LEN - 1:
                if isinstance(board[row + 2][col], EmptyTile):
                    legal_moves += 1
                    down_move_new_pos.append((col, row + 1))
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