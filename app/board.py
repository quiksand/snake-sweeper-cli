# internal dependencies
import random

class Board(object):
    """a mine sweeper board"""
    EMPTY_SPACE = "0"
    MINE_SPACE = "*"
    DEFAULT_ROWS = 9
    DEFAULT_COLS = 9
    DEFAULT_MINES = 10

    def __init__(self, rows = DEFAULT_ROWS, columns = DEFAULT_COLS, mines = DEFAULT_MINES):
        self.board = ""
        self.mines = mines
        self.rows = rows
        self.columns = columns
        self.generate_new_board()
        self.calc_hints()
        self.print_board()

    def generate_new_board(self):
        '''generates the board with mines and placeholders for numbers'''
        # create local variables for better readability
        rows = self.rows
        cols = self.columns
        mines = self.mines
        # generate a string of all zeroes
        self.board = ((rows*cols)-mines) * self.EMPTY_SPACE
        # seed the zero string with mines
        while(mines):
            index = random.randint(0,len(self.board))
            self.board = self.board[:index] + self.MINE_SPACE + self.board[index:]
            mines -= 1
        # break the string into rows
        new_arr = []
        k = 0
        for i in range(rows):
            new_arr.append([])
            for j in range(cols):
                new_arr[i] += self.board[k]
                k += 1

        self.board = new_arr

    def print_board(self, zeroes = EMPTY_SPACE, mines = MINE_SPACE):
        '''pretty-prints the board'''
        new_arr = []
        for row in self.board:
            new_arr.append(' '.join(row).replace(self.EMPTY_SPACE, zeroes).replace(self.MINE_SPACE, mines))
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