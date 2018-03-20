import copy
from Tile import Tile
from Coordinate import Coordinate
from Move import Move
class BoardState:
    def __init__(self, board):
        self.layout=board       #list of lists representing the board. Hold Tile objects
        self.white_pieces_loc = []  #list of coordinates pointing to white pieces on the layout. Useful in other methods
        self.black_pieces_loc = []  #list of coordinates pointing to black pieces on the layout. Useful in other methods

        for i in range(len(self.layout)):
            for j in range(len(self.layout)):
                if self.layout[i][j] == Tile.WHITE_PIECE:
                    self.white_pieces_loc.append(Coordinate(i,j))
                if board[i][j] == Tile.BLACK_PIECE:
                    self.black_pieces_loc.append(Coordinate(i,j))   #build lists of coordinates


    def update(self, move):         #produces a new BoardState object created by applying input move to this current board. Used for making new child Nodes of Node object
        new_board = copy.deepcopy(self.layout)

        temp_tile = new_board[move.get_begin().get_row()][move.get_begin().get_column()]
        new_board[move.get_begin().get_row()][move.get_begin().get_column()]=new_board[move.get_end().get_row()][move.get_end().get_column()]
        new_board[move.get_end().get_row()][move.get_end().get_column()] = temp_tile

        ### call to delete_surrounded should be here once it is implemented
        return BoardState(new_board)

    def delete_surrounded(self):
        pass


        #### still needs definition

    def is_goal(self):
        pass

        #### needs implementation




    def man_distance(self):     #calcs sum of all white piece manhatten distances to nearest black piece. Used for heuristic estimated cost to goal state in A* search
        total_man_dist=0
        for w_piece in self.white_pieces_loc:
            min_man_dist=2*len(self.layout)
            for b_piece in self.black_pieces_loc:
                if(abs(w_piece.get_row()-b_piece.get_row())+abs(w_piece.get_column()-b_piece.get_column())<min_man_dist):
                    min_man_dist=abs(w_piece.get_row()-b_piece.get_row())+abs(w_piece.get_column()-b_piece.get_column())
            total_man_dist +=min_man_dist
        return total_man_dist





    def __str__(self):
        message = ''
        for i in range(len(self.layout)):
            for j in range(len(layout)):
                message=message+self.layout[i][j].name+' '
            message=message+'/n'
        return message


    def get_white_moves(self):      #gets a list of Move objects representing the possible moves the white pieces can make on this layout
        white_moves=[]
        for piece in self.white_pieces_loc:
            row=piece.get_row()
            col=piece.get_column()
            left_move=self.check_left_move(row,col)
            if(not (left_move is None)):
                white_moves.append(left_move)
            up_move=self.check_up_move(row,col)
            if(not (up_move is None)):
                white_moves.append(up_move)
            right_move=self.check_right_move(row,col)
            if(not (right_move is None)):
                white_moves.append(right_move)
            down_move=self.check_down_move(row,col)
            if(not (down_move is None)):
                white_moves.append(down_move)
        return white_moves

    def get_black_moves(self):  #gets a list of Move objects representing the possible moves the black pieces can make on this layout
        black_moves=[]
        for piece in self.black_pieces_loc:
            row=piece.get_row()
            col=piece.get_column()
            left_move=self.check_left_move(row,col)
            if(not (left_move is None)):
                black_moves.append(left_move)
            up_move=self.check_up_move(row,col)
            if(not (up_move is None)):
                black_moves.append(up_move)
            right_move=self.check_right_move(row,col)
            if(not (right_move is None)):
                black_moves.append(right_move)
            down_move=self.check_down_move(row,col)
            if(not (down_move is None)):
                black_moves.append(down_move)
        return black_moves


    def check_left_move(self,row, col):
        if col > 0:
            if self.layout[row][col - 1] == Tile.EMPTY_TILE:
                left_move=Move(row,col,row,col-1)
                return left_move
            elif self.layout[row][col - 1] in (Tile.BLACK_PIECE, Tile.WHITE_PIECE):
                if col - 1 > 0:
                    if self.layout[row][col - 2] == Tile.EMPTY_TILE:
                        left_move=Move(row,col,row, col - 2)
                        return left_move
        else:
            return None


    def check_up_move(self,row, col):
        if row > 0:
            if self.layout[row-1][col] == Tile.EMPTY_TILE:
                up_move=Move(row,col,row-1,col)
                return up_move
            elif self.layout[row-1][col] in (Tile.BLACK_PIECE, Tile.WHITE_PIECE):
                if row - 1 > 0:
                    if self.layout[row-2][col] == Tile.EMPTY_TILE:
                        up_move=Move(row,col,row-2, col)
                        return up_move
        else:
            return None

    def check_right_move(self, row, col):
        if col <len(self.layout)-1 :
            if self.layout[row][col +1] == Tile.EMPTY_TILE:
                right_move=Move(row,col,row,col+1)
                return right_move
            elif self.layout[row][col +1] in (Tile.BLACK_PIECE, Tile.WHITE_PIECE):
                if col +1 <len(self.layout)-1:
                    if self.layout[row][col + 2] == Tile.EMPTY_TILE:
                        right_move=Move(row,col,row, col + 2)
                        return right_move
        else:
            return None

    def check_down_move(self,row, col):
        if row <len(self.layout)-1 :
            if self.layout[row+1][col] == Tile.EMPTY_TILE:
                down_move=Move(row,col,row+1,col)
                return down_move
            elif self.layout[row+1][col] in (Tile.BLACK_PIECE, Tile.WHITE_PIECE):
                if row +1 <len(self.layout)-1:
                    if self.layout[row+2][col] == Tile.EMPTY_TILE:
                        down_move=Move(row,col,row, col + 2)
                        return down_move
        else:
            return None
