import unittest
from board import Board
from game import Game

class TestGame(unittest.TestCase):

    
                
    def test_set_hangman(self): 
        self._game = Game(Board(['a','n','a'], ['a', '_','a']))
        self._game.set_hangman()
        hangman = self._game.get_hangman()
        self.assertEqual(hangman,['h'])

    def test_set_hangman_sentence(self):
        self._game = Game(Board(['a','n','a'], ['a', '_','a']))
        sentence = self._game.set_hangman_sentence('n')
        self.assertEqual(sentence,['a', 'n','a'] )

    def test_deal_with_letter_1(self):
        self._game = Game(Board(['a','n','a'], ['a', '_','a']))
        hangman_sentence,hangman,done = self._game.deal_with_letter('n')
        self.assertEqual( hangman_sentence, ['a', 'n','a'])

    def test_deal_with_letter_2(self):
        self._game = Game(Board(['a','n','a'], ['a', '_','a']))
        hangman_sentence,hangman,done= self._game.deal_with_letter('p')
        self.assertEqual( hangman, ['h'])




if __name__ == '__main__':
    unittest.main()