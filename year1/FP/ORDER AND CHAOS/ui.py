from game import Game

class Ui:
    def __init__(self, game:Game):
        self._game= game


    def string_board(self):
        board = self._game.string_board()
        print (board)

    def start_game(self):
        
        done = False
        while done == False:
            correct_input = False
            self._game.computer_move()
            full = self._game.check_if_full_board()
            win = self._game.check_for_win()

            if win == True:
                print("ORDER WINS")
                done = True
            
            if full == True:
                print("CHAOS WINS")
                done = True
            if done == True:
                self.string_board()
                break  

            self.string_board()
            while correct_input == False:
                human_row = input("enter row")
                human_column  =input( " enter column")
                human_symbol = input ( " enter symbol")
                if not human_row.isdecimal() or not human_column.isdecimal():
                    print("wrong input")
                else:
                    human_column= int(human_column)
                    human_row = int(human_row)
                    if human_row < 0 or human_column >5 or (human_symbol !='x' and human_symbol !='0'):
                        print("invalid input")
                        correct_input = False
                    else:
                        correct_input = True

                value = self._game.get_cell_value(human_row,human_column)
                if value != ".":
                    print("not a free space")
                    correct_input = False

            self._game.set_board_value(human_row, human_column, human_symbol)

            full = self._game.check_if_full_board()
            win = self._game.check_for_win()

            if win == True:
                print("ORDER WINS")
                done = True
            
            if full == True:
                print("CHAOS WINS")
                done = True
            

           
            

        

            

        


                

