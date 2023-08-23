

from dataclasses import dataclass


@dataclass
class Cell:
    line: int
    column: int
    value: any

    
class Board:

    def __init__(self, rows, columns, empty_value="_"):
        self.__rows = rows
        self.__columns = columns
        self.__empty_value = empty_value

        self.__cells = self.__create_board()

    def __create_board(self):
        """
        creates board
        :return: [description]
        """        
        return [[Cell(row, column, self.__empty_value) for column in range(self.__columns)]
                for row in range(self.__rows)]

    def set_value(self, row, column, value):
        """
        sets value for given position
        :param row: row
        :param column: column
        :param value: value
        """        
        self.__cells[row][column].value = value

    def get_row_values(self, row):
        """
        get values from row
        :param row: row
        :return: values form row
        """        
        return [cell.value for cell in self.__cells[row]]

    def get_column_values(self, column):
        """
        get values from column
        :param column: column
        :return: values from column
        """        
        return [row[column].value for row in self.__cells]
    
    def get_next_free_row(self, column):
        """
        gets the position of the next free row
        :param column: column
        :return: position of free row in that column
        """        
        if self.__cells[0][column].value != "_":
            return -1
        for i in range(5,-1,-1):
            if self.__cells[i][column].value == "_":
                return i
        return -1

    def get_cell_value(self, row, column):
        """
        gets value of a given cell
        :param row: row
        :param column: column
        :return: the value from that cell
        """        
        return self.__cells[row][column].value
    
    def get_empty_cells(self):
        """
        sets the empty cells
        :return: empty cells
        """        
        l = []
        for cell in self.__get_all_cells_as_list():
            if cell.value == self.__empty_value:
                l.append(cell)
        return l

    def __get_all_cells_as_list(self):
        """
        gets all cells as list
        :return: cells as a list
        """        
        l = []
        for row in range(0,len(self.__cells)):
            for cell in self.__cells[row]: 
                l.append(cell)
        return l

    def check_column(self, column):
        """
        checks if the collumn is full
        :param column: collumn
        :return: 0 if the collumn is full
        """        
        if self.__cells[0][column].value == "_":
            return 1
        return 0

    def get_main_diagonal(self, row, column):
        """
        checks four positions on diagonal
        :param row: row
        :param column: column
        :return: main diagonal
        """        
        first_value = self.get_cell_value(row, column)
        second_value = self.get_cell_value(row + 1, column + 1)
        third_value = self.get_cell_value(row + 2, column + 2)
        forth_value = self.get_cell_value(row + 3, column + 3)
        main_diagonal = [first_value, second_value, third_value, forth_value]
        return main_diagonal

    def get_secondary_diagonal(self, row, column):
        """
        checks four positions on diagonal
        :param row: row
        :param column: column
        :return: secondary diagonal
        """
        first_value = self.get_cell_value(row, column)
        second_value = self.get_cell_value(row + 1, column - 1)
        third_value = self.get_cell_value(row + 2, column - 2)
        forth_value = self.get_cell_value(row + 3, column - 3)
        secondary_diagonal = [first_value, second_value, third_value, forth_value]
        return secondary_diagonal

    def __str__(self):
        board = ""
        for row in self.__cells:
            row = " ".join([str(cell.value) for cell in row]) + "\n"
            board += row
        return board
