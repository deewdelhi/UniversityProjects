from board import Board
import unittest


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(['a','n','a'], ['a', '_','a'])
        return super().setUp()
        


    def test_set_hangman(self):
        self._board.set_hangman(['l'])
        self.assertEqual( self._board.hangman , ['l'])

    def test_set_hangman_sentence(self):
        self._board.set_hangman_sentence(['l'])
        self.assertEqual( self._board.hangman_sentence , ['l'])
        



if __name__ == '__main__':
    unittest.main()