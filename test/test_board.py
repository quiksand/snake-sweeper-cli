# internal dependencies
from app import board

# external dependencies
import unittest

class TestBoard(unittest.TestCase):

	def test_board(self):
		test = board.Board(15,30,99)
		print("")
		print(test.board)
		self.assertEqual("abc","def")
    # def set_up(self):
    #     self.board = Board

if __name__ == '__main__':
	unittest.main()