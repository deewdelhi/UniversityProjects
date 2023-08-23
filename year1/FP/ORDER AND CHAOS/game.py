
from board import Board
import random


class Game:
    def __init__(self,board:Board):
        self._board = board

    def string_board(self):
        return self._board.board_to_string()


    def set_board_value(self,row, column,value):
        self._board.set_board_value(row,column,value)


    def get_cell_value(self,row,column):
            return self._board.get_cell_value(row,column)


    def get_computer_move_possible_win(self,symbol):   ##!!!! doar pentru orizontala si verticala pana acum
        win_row = 0
        win_column =0        
       
        #  orizontala
        for r in range (0,6):
            row = self._board.get_row(r)
            if row[0] == row[1]== row[2]== row[3] == symbol  and row[4] == ".":
                win_row = r
                win_column =4 
                
                return win_row,win_column

            if row[1] == row[2]== row[3]== row[4] ==symbol  and row[5] ==".":
                win_row = r
                win_column =5 
                
                
                return win_row,win_column

            if row[1] == row[2]== row[3]== row[4] ==symbol  and row[0] ==".":
                win_row = r
                win_column =0 
                
                
                return win_row,win_column

            # verticala

            for r in range (0,6):
                column = self._board.get_column(r)
                if column[0] == column[1]== column[2]== column[3] ==symbol  and column[4] ==".":
                    win_row = 4
                    win_column = r
                   
                    return win_row,win_column

                if column[1] == column[2]== column[3]== column[4] ==symbol  and column[5] ==".":
                    win_row = 5
                    win_column =r 
                   
                    
                    return win_row,win_column

                if column[1] == column[2]== column[3]== column[4] ==symbol   and column[0] ==".":
                    win_row = 0
                    win_column =r
                   
                    
                    return win_row,win_column

        return win_row,win_column


    def check_if_full_board(self):

        full = True

        for row in range (0,6):
            for column in range(0,6):
                value = self.get_cell_value(row,column)
                if value == ".":
                    full = False

        return full

    def check_for_win(self):

        win = False


        for r in range (0,6):
            row = self._board.get_row(r)
            if (row[0] == row[1]== row[2]== row[3] == row[4] == 'x'  or row[0] == row[1]== row[2]== row[3] ==row[4] =="0"):
                win = True

            if (row[1] == row[2]== row[3]== row[4] == row[5]=='x'  or row[1] == row[2]== row[3]== row[4] == row [5] =="0"):
                win =True

            for r in range (0,6):
                column = self._board.get_column(r)
                if (column[0] == column[1]== column[2]== column[3] == column[4] =='x'  or column[0] == column[1]== column[2]== column[3] == column[4] == '0') :
                   win = True

                if (column[1] == column[2]== column[3]== column[4] == column[5] == 'x'  or column[1] == column[2]== column[3]== column[4] == column[5] =="0"):
                  win = True

        return win        



    ##############################################3

    def get_board_as_list(self):
        board = self._board.board_to_list_new()
        return board


    def get_position_for_computer(self,value):
        board = self.get_board_as_list()
        
        number_of_surrounding_values_actual = int(0)
        number_of_surrounding_values_max = int(0)
        row_computer = int(0)
        column_computer = int(0)


        for row in range (1,5):
            for column in range (1,5):
                cell_value = self.get_cell_value(row,column)
                if cell_value == ".":
                    if board[row-1][column -1] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row-1][column] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row-1][column +1] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row][column +1] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row+1][column+1 ] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row+1][column ] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row+1][column -1] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1

                    if board[row][column -1] ==value:
                        number_of_surrounding_values_actual = number_of_surrounding_values_actual +1



                    if number_of_surrounding_values_actual > number_of_surrounding_values_max:
                        number_of_surrounding_values_max = number_of_surrounding_values_actual
                        row_computer = row
                        column_computer = column


                number_of_surrounding_values_actual = int(0)

        return row_computer, column_computer


    def computer_move(self):

        

    
        valid_move = False
        while valid_move ==False:

            number_of_x_in_matrix = int(0)
            number_of_0_in_matrix = int(0)

            for row in range (0,6):
                for column in range (0,6):
                    cell_value = self._board.get_cell_value(row,column)
                    if cell_value == 'x':
                        number_of_x_in_matrix = number_of_x_in_matrix + 1
                    if cell_value == '0':
                        number_of_0_in_matrix = number_of_0_in_matrix + 1

            if number_of_0_in_matrix > number_of_x_in_matrix:
                symbol = '0'
            else:
                if number_of_0_in_matrix < number_of_x_in_matrix:
                    symbol = 'x'
                else: 
                    symbol = random.randint(1,2)
                    if symbol ==1:
                        symbol = 'x'
                    else:
                        symbol = '0'
                        

            row,column= self.get_computer_move_possible_win(symbol)  

            if row == column  == 0:        
                row,column = self.get_position_for_computer(symbol)   
                if row == column == 0:          
                    row= random.randint(0,5)
                    column = random.randint(0,5)
            value = self.get_cell_value(row,column)
            if value == '.':
                valid_move = True

        self._board.set_board_value(row,column,symbol)

        






