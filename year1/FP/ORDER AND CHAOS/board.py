from dataclasses import dataclass

@dataclass
class Cell:
    line: int
    column: int
    value: any


class Board:
    def __init__(self,rows,columns,empty_value = "."):
        self.__rows = rows
        self.__columns = columns
        self.__empty_value = empty_value
        self.__cells = self.create_board()


    def create_board(self):
        """
        creates board
        :return: [description]
        """        
        return [[Cell(row, column, self.__empty_value) for column in range(self.__columns)]
                for row in range(self.__rows)]
        

    def board_to_string(self):
        board = ""
        for row in self.__cells:
            row = " ".join([str(cell.value)for cell in row]) + "\n"
            board += row
    
        return board

    def board_to_list(self):
        board = []
        for row in range (self.__columns):
            board.append(self.__cells[row])

        return board

    def board_to_list_new(self):
        board = []
       
        for r in self.__cells:
            row = ([str(cell.value)for cell in r])
            board.append(row)    
        return board

    def set_board_value(self,row,column,value):

        self.__cells[row][column].value = value


    def get_row(self,row_number):
        row = []
        for column in range (self.__columns):
            row.append(self.__cells[row_number][column].value)

        return row

    def get_column(self,column_number):
        column = []
        for row in range (self.__rows):
            column.append(self.__cells[row][column_number].value)

        return column

    def get_cell_value(self,row,column):
        return self.__cells[row][column].value