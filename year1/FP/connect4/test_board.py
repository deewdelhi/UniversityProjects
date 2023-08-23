import unittest
from board_game.board import Board
from ui.ui import Ui
from game.game import Game




class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(6, 7)

    def test_set_value__initial_board__one_set_element(self):
        self._board.set_value(1, 5, "x")
        self.assertEqual(self._board.get_cell_value(1, 5), "x")

    def test_get_row_values__initial_board__correct_list(self):
        self._board.set_value(0, 0, "x")
        self._board.set_value(0, 1, "o")
        self.assertEqual(self._board.get_row_values(0), ["x", "o", "_", "_", "_", "_", "_"])

    def test_get_column_value__initial_board__correct_list(self):
        self._board.set_value(5, 0, "x")
        self._board.set_value(4, 0, "o")
        self.assertEqual(self._board.get_column_values(0), ['_', '_', '_', '_', 'o', 'x'])

    def test_get_empty_cells__initial_board__41_element_list(self):
        self._board.set_value(5, 6, "_")
        self.assertEqual(len(self._board.get_empty_cells()), 42)


if __name__ == '__main__':
    unittest.main()
