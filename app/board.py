# internal dependencies
import random

class Board(object):
    """a mine sweeper board"""
    EMPTY_SPACE = "."
    MINE_SPACE = "*"

    def __init__(self, rows, columns):
        self.board = ""
        self.actual_mines = 0
        self.rows = rows
        self.columns = columns
        self.possible_mines = random.randint(1, (rows * 2))


# recommend replacing logic here with more straightwforward  sweeper
    def generate_new_board(self):
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

            row_str = "".join(row)
            new_board_arr.append(row_str)

        # new_board_str = new
        # self.actual_mines = sum()

        self.board = new_board_arr
        print(self.board)

    def print_board(self):
        board_arr = self.board
        board_string = "\n".join(self.board)

        print(board_string)


# TEST STUFF
test_board = Board(4,4)
test_board.generate_new_board()
test_board.print_board()

