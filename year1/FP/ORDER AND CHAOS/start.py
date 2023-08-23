from board import Board
from game import Game
from ui import Ui


if __name__ == '__main__':
    ui = Ui(Game(Board(6, 6)))
    ui.start_game()
