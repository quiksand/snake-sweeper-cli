# internal dependencies
import random

class Board(object):
    """a mine sweeper board"""
    EMPTY_SPACE = "0"
    MINE_SPACE = "*"

    def __init__(self, rows, columns):
        self.board = ""
        self.actual_mines = 0
        self.rows = rows
        self.columns = columns
        self.possible_mines = random.randint(1, (rows * 2))
        self.generate_new_board()
        self.calc_hints()
        self.print_board()

    def generate_new_board(self):
        '''generates the board with mines and placeholders for numbers'''
        new_board_arr = []
        possible_mines = self.possible_mines
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if round(random.random(), 2) >= 0.4:
                    row.append(self.EMPTY_SPACE)
                else:
                    if possible_mines:
                        row.append(self.MINE_SPACE)
                        possible_mines -= 1
                    else:
                        row.append(self.EMPTY_SPACE)
            new_board_arr.append(row)
        self.board = new_board_arr

    def print_board(self):
        '''pretty-prints the board'''
        new_arr = []
        for row in self.board:
            new_arr.append(' '.join(row))
        for row_str in new_arr:
            print(row_str)
        
    def calc_hints(self):
        '''generate numbers after a board is generated'''
        for i in range(self.rows):
            for j in range(self.columns):
                #when a mine is selected do the following
                if(self.board[i][j] == self.MINE_SPACE):
                    # k and l loops to access surrounding array indices
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            #test for edges, continue if inaccessible
                            if(i+k < 0 or j+l < 0 or i+k > self.rows-1 or j+l > self.columns-1):
                                continue
                            if (self.board[i+k][j+l] != self.MINE_SPACE):
                                self.board[i+k][j+l] = str(int(self.board[i+k][j+l]) + 1)
                else:
                    continue
