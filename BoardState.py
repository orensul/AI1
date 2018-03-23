import copy
from TileEnum import TileEnum
from Coordinate import Coordinate
from Move import Move


class BoardState:
    """
    Class of a state of the board.
    """

    def __init__(self, board):
        """
        constructor for BoardState which initialize the white and black pieces lists
        :param board:
        """
        # list of lists representing the board. Hold Tile objects
        self._board = board
        # list of coordinates pointing to white pieces on the layout. Useful in other methods
        self._white_pieces_loc = []
        # list of coordinates pointing to black pieces on the layout. Useful in other methods
        self._black_pieces_loc = []

        # initialize white and black pieces lists
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] == TileEnum.WHITE_PIECE:
                    self._white_pieces_loc.append(Coordinate(i, j))
                if board[i][j] == TileEnum.BLACK_PIECE:
                    self._black_pieces_loc.append(Coordinate(i, j))

    def is_board_states_same(self, other_board_state):
        """
        :param other_board_state: other board.
        :return: True if current board and other board are the same state, False otherwise.
        """
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if not self._board[i][j] == other_board_state.get_board()[i][j]:
                    return False
        return True

    def get_board(self):
        return self._board

    def get_white_pieces_loc(self):
        return self._white_pieces_loc

    def get_black_pieces_loc(self):
        return self._black_pieces_loc

    def update(self, move):
        """
        produces a new BoardState object created by applying input move to this current board.
        Used for making new child Nodes of Node object
        :param move: move object contains source and destination of the move
        :return:
        """
        new_board = copy.deepcopy(self._board)
        original_loc_row = move.get_begin().get_row()
        original_loc_col = move.get_begin().get_column()
        new_loc_row = move.get_end().get_row()
        new_loc_col = move.get_end().get_column()

        temp_tile = new_board[original_loc_row][original_loc_col]
        new_board[original_loc_row][original_loc_col] = new_board[new_loc_row][new_loc_col]
        new_board[new_loc_row][new_loc_col] = temp_tile

        return BoardState(new_board)

    def delete_black_piece(self, delete_black_piece_loc):
        """
         Help method which delete black piece from the board
         :param delete_black_piece_loc:
         :return:
         """
        for b_piece in delete_black_piece_loc:
            self._board[b_piece.get_row()][b_piece.get_column()] = TileEnum.EMPTY_TILE
            self._black_pieces_loc.remove(b_piece)

    def delete_white_piece(self, delete_white_piece_loc):
        """
        Help method which delete white piece from the board
        :param delete_white_piece_loc:
        :return:
        """
        for w_piece in delete_white_piece_loc:
            self._board[w_piece.get_row()][w_piece.get_column()] = TileEnum.EMPTY_TILE
            self._white_pieces_loc.remove(w_piece)

    def delete_white_surrounded(self):
        """
        Check for white pieces which are surrounded by black pieces and remove them from the board.
        :return:
        """
        delete_white_piece_loc = []
        for w_piece in self._white_pieces_loc:
            if w_piece.get_row() == 0 or w_piece.get_row() == len(self._board) - 1:
                if self._board[w_piece.get_row()][w_piece.get_column() - 1] \
                        in (TileEnum.BLACK_PIECE, TileEnum.CORNER_TILE) and \
                        self._board[w_piece.get_row()][w_piece.get_column() + 1] \
                        in (TileEnum.BLACK_PIECE, TileEnum.CORNER_TILE):
                    delete_white_piece_loc.append(w_piece)
            elif w_piece.get_column() == 0 or w_piece.get_column() == len(self._board) - 1:
                if self._board[w_piece.get_row() - 1][w_piece.get_column()] \
                        in (TileEnum.BLACK_PIECE, TileEnum.CORNER_TILE) and \
                        self._board[w_piece.get_row() + 1][w_piece.get_column()] \
                        in (TileEnum.BLACK_PIECE, TileEnum.CORNER_TILE):
                    delete_white_piece_loc.append(w_piece)
            else:
                if (self._board[w_piece.get_row()][w_piece.get_column() - 1] == TileEnum.BLACK_PIECE and \
                    self._board[w_piece.get_row()][w_piece.get_column() + 1] == TileEnum.BLACK_PIECE) \
                        or (self._board[w_piece.get_row() - 1][w_piece.get_column()] == TileEnum.BLACK_PIECE and \
                            self._board[w_piece.get_row() + 1][w_piece.get_column()] == TileEnum.BLACK_PIECE):
                    delete_white_piece_loc.append(w_piece)
        self.delete_white_piece(delete_white_piece_loc)

    def delete_black_surrounded(self):
        """
        Check for black pieces which are surrounded by white pieces and remove them from the board.
        :return:
        """
        delete_black_piece_loc = []
        for b_piece in self._black_pieces_loc:
            if b_piece.get_row() == 0 or b_piece.get_row() == len(self._board) - 1:
                if self._board[b_piece.get_row()][b_piece.get_column() - 1] \
                        in(TileEnum.WHITE_PIECE, TileEnum.CORNER_TILE) and \
                        self._board[b_piece.get_row()][b_piece.get_column() + 1] \
                        in(TileEnum.WHITE_PIECE, TileEnum.CORNER_TILE):
                    delete_black_piece_loc.append(b_piece)
            elif b_piece.get_column() == 0 or b_piece.get_column() == len(self._board) - 1:
                if self._board[b_piece.get_row() - 1][b_piece.get_column()] \
                    in(TileEnum.WHITE_PIECE, TileEnum.CORNER_TILE) and \
                    self._board[b_piece.get_row() + 1][b_piece.get_column()] \
                        in(TileEnum.WHITE_PIECE, TileEnum.CORNER_TILE):
                    delete_black_piece_loc.append(b_piece)
            else:
                if (self._board[b_piece.get_row()][b_piece.get_column() - 1] == TileEnum.WHITE_PIECE and \
                    self._board[b_piece.get_row()][b_piece.get_column() + 1] == TileEnum.WHITE_PIECE) \
                    or (self._board[b_piece.get_row() - 1][b_piece.get_column()] == TileEnum.WHITE_PIECE and \
                        self._board[b_piece.get_row() + 1][b_piece.get_column()] == TileEnum.WHITE_PIECE):
                    delete_black_piece_loc.append(b_piece)
        self.delete_black_piece(delete_black_piece_loc)

    def is_goal(self):
        """
        :return: True if we reached the goal (all black pieces have been eliminated) otherwise, False.
        """
        return len(self._black_pieces_loc) == 0

    def sum_man_distance(self):
        """
        calculates average manhattan distance from black piece to the other white pieces and multiply by 2
        because we need to white pieces to kill black piece
        Used for heuristic estimated cost to goal state in A* search
        :return: heuristic estimated cost to goal state in A* search
        """
        total_man_dist = 0
        for b_piece in self._black_pieces_loc:
            count_w_pieces = 1
            avg = 0
            for w_piece in self._white_pieces_loc:
                avg += self.man_distance(b_piece, w_piece) - 1
                count_w_pieces += 1
            avg /= count_w_pieces
            total_man_dist += avg
        return total_man_dist*2

    @staticmethod
    def man_distance(coord_white, coord_black):
        """
        Calculate the manhattan distance between white and black piece
        :param coord_white: coordinate object of white piece
        :param coord_black: coordinate object of black piece
        :return:
        """
        return abs(coord_white.get_row() - coord_black.get_row()) + \
               abs(coord_white.get_column() - coord_black.get_column())

    def __str__(self):
        """
        toString method of BoardState which prints the board state
        :return: string which represents whe board state
        """
        message = ''
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                message = message + self._board[i][j].name + ' '
            message = message + '/n'
        return message

    def get_white_moves(self):
        """
        gets a list of Move objects representing the possible moves the white pieces can make on this board
        :return: list of optional white moves
        """
        white_moves = []
        for piece in self._white_pieces_loc:
            row = piece.get_row()
            col = piece.get_column()

            left_move = self.check_left_move(row, col)
            if left_move is not None:
                white_moves.append(left_move)

            up_move = self.check_up_move(row, col)
            if up_move is not None:
                white_moves.append(up_move)

            right_move = self.check_right_move(row, col)
            if right_move is not None:
                white_moves.append(right_move)

            down_move = self.check_down_move(row, col)
            if down_move is not None:
                white_moves.append(down_move)

        return white_moves

    def get_black_moves(self):
        """
        gets a list of Move objects representing the possible moves the black pieces can make on this board
        :return: list of optional black moves
        """
        black_moves = []
        for piece in self._black_pieces_loc:
            row = piece.get_row()
            col = piece.get_column()

            left_move = self.check_left_move(row, col)
            if left_move is not None:
                black_moves.append(left_move)

            up_move = self.check_up_move(row, col)
            if up_move is not None:
                black_moves.append(up_move)

            right_move = self.check_right_move(row, col)
            if right_move is not None:
                black_moves.append(right_move)

            down_move = self.check_down_move(row, col)
            if down_move is not None:
                black_moves.append(down_move)

        return black_moves

    def check_left_move(self, row, col):
        """
        check for move left, if exist return move object
        :param row: row of tile we are moving from
        :param col: column of tile we are moving from
        :return: move
        """
        if col > 0:
            if self._board[row][col - 1] == TileEnum.EMPTY_TILE:
                left_move = Move(row, col, row, col - 1)
                return left_move
            elif self._board[row][col - 1] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
                if col - 1 > 0:
                    if self._board[row][col - 2] == TileEnum.EMPTY_TILE:
                        left_move = Move(row, col, row, col - 2)
                        return left_move

    def check_up_move(self, row, col):
        """
        check for move up, if exist return move object
        :param row: row of tile we are moving from
        :param col: column of tile we are moving from
        :return: move
        """
        if row > 0:
            if self._board[row-1][col] == TileEnum.EMPTY_TILE:
                up_move = Move(row, col, row - 1, col)
                return up_move
            elif self._board[row - 1][col] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
                if row - 1 > 0:
                    if self._board[row - 2][col] == TileEnum.EMPTY_TILE:
                        up_move = Move(row, col, row - 2, col)
                        return up_move

    def check_right_move(self, row, col):
        """
        check for move right, if exist return move object
        :param row: row of tile we are moving from
        :param col: column of tile we are moving from
        :return: move
        """
        if col < len(self._board) - 1:
            if self._board[row][col + 1] == TileEnum.EMPTY_TILE:
                right_move = Move(row, col, row, col + 1)
                return right_move
            elif self._board[row][col + 1] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
                if col + 1 < len(self._board) - 1:
                    if self._board[row][col + 2] == TileEnum.EMPTY_TILE:
                        right_move = Move(row, col, row, col + 2)
                        return right_move

    def check_down_move(self, row, col):
        """
        check for move down, if exist return move object
        :param row: row of tile we are moving from
        :param col: column of tile we are moving from
        :return: move
        """
        if row < len(self._board) - 1:
            if self._board[row + 1][col] == TileEnum.EMPTY_TILE:
                down_move = Move(row, col, row + 1, col)
                return down_move
            elif self._board[row + 1][col] in (TileEnum.BLACK_PIECE, TileEnum.WHITE_PIECE):
                if row + 1 < len(self._board) - 1:
                    if self._board[row + 2][col] == TileEnum.EMPTY_TILE:
                        down_move = Move(row, col, row + 2, col)
                        return down_move
