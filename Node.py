#Node class is used for the search tree in A* search for 'massacre'
from BoardState import BoardState
class Node:
    def __init__(self, board_state,parent,move,cost):
        self.board = board_state        #current state of the board this node represents
        self.cost_so_far=cost       #cost it has taken to get down to this node on the tree so far
        self.parent=parent          #parent node, used to traverse up sequence of nodes once goal state found
        self.est_cost=self.board.man_distance()     #heuristic score for A* search
        self.children=[]                            #Collection of child nodes produced by moving white pieces, only filled when node is expanded in A* search
        self.move=move              #Move that translates parent node state to this current node state. Useful in output of massacre method.

    def expand_white_moves(self):
        white_moves=self.board.get_white_moves()
        for move in white_moves:
            self.children.append(Node(self.board.update(move),self.board,move,self.cost_so_far+1))  #each move is a cost of 1 so each child node has a cost_so_far 1 more than their parent

    def __str__(self):
        message = ''
        print("Node white pieces location: ")
        for loc in self.board.white_pieces_loc:
            message += str(loc)+' '
        message += '\nNode black pieces location: \n'
        for loc in self.board.black_pieces_loc:
            message += str(loc)+' '
        return message
