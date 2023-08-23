import unittest
from board_game.board import Board
from ui.ui import Ui
from game.game import Game


class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game(Board(6, 7))

    def test_verify_move_validity__valid_move__True(self):
        self.assertTrue(self._game.verify_move_validity(5, 0))

    def test_verify_move_validity__invalid_move__False(self):
        self.assertFalse(self._game.verify_move_validity(4, 3))

    def test_verify_if_board_is_full__full_board__True(self):
        for i in range(6):
            for j in range(7):
                self._game.human_player_move(i, j)
        self.assertTrue(self._game.verify_if_board_is_full())

    def test_verify_if_board_is_full__board_not_full__False(self):
        self._game.human_player_move(0, 0)
        self.assertFalse(self._game.verify_if_board_is_full())

    def test_human_player_move__empty_board__value_placed_correctly(self):
        self._game.human_player_move(0, 0)
        self.assertEqual(self._game._board.get_cell_value(0, 0), "o")

    def test_computer_move__human_player_about_to_win__blocked_human_player_win(self):
        self._game.human_player_move(5, 0)
        self._game.human_player_move(5, 1)
        self._game.human_player_move(5, 2)
        self._game.computer_move()
        self.assertEqual(self._game._board.get_cell_value(5, 3), "x")

    def test_verify_if_someone_has_won__human_player_won__human_player_symbol(self):
        self._game.human_player_move(0, 0)
        self._game.human_player_move(0, 1)
        self._game.human_player_move(0, 2)
        self._game.human_player_move(0, 3)
        self.assertEqual(self._game.verify_if_someone_has_won(), "o")

    def test_verify_if_someone_has_won__computer_won__computer_symbol(self):
        self._game._board.set_value(0, 0, "x")
        self._game._board.set_value(0, 1,"x")
        self._game._board.set_value(0, 2, "x")
        self._game._board.set_value(0, 3, "x")
        self.assertEqual(self._game.verify_if_someone_has_won(), "x")

    def test_verify_if_someone_has_won__nobody_won__False(self):
        self._game.human_player_move(0, 0)
        self._game.computer_move()
        self._game.human_player_move(0, 2)
        self._game.human_player_move(0, 3)
        self.assertFalse(self._game.verify_if_someone_has_won())

   


if __name__ == '__main__':
    unittest.main()
