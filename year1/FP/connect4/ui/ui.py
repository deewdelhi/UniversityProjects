from game.game import Game


class Ui:
    def __init__(self, game: Game):
        self._game = game

    @staticmethod
    def print_menu():
        print("\nYou are player 1, your pieces will be displayed as 'o' on the board.\n"
              "You are playing against the computer, whose moves will be displayed as 'x' on the board.\n"
              "The game started.\n")

    def print_board(self):
        board = self._game.get_board_as_string()
        print(board)

    def start_menu(self):
        """
        printing menu and messages if you win lose or it s a draw
        """        
        winner = 0
        game_over = False
        full_board = False
        self.print_menu()
        while game_over is False and full_board is False:
            print("It's your turn! Enter the column where you want to place your piece")
            try:
                column = int(input("Enter column\n>"))
            except:
                column=-1
            row = self._game.get_next_position(column)
            while self._game.verify_move_validity(row, column) is False:
                print("This place is not available")
                try:
                    column = int(input("Enter column\n>"))
                except:
                    column=-1
                row = self._game.get_next_position(column)
            self._game.human_player_move(row, column)
            self._game.computer_move()
            self.print_board()
            if self._game.verify_if_someone_has_won() is not False:
                winner = self._game.verify_if_someone_has_won()
                game_over = True
            full_board = self._game.verify_if_board_is_full()

        if winner == "o":
            print("You won!")
        elif winner == "x":
            print("The computer won.")
        else:
            print("The end.")
