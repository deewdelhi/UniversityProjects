from board_game.board import Board
import random


class Game:
    def __init__(self, board: Board):
        self._board = board

    def get_board_as_string(self):
        return self._board.__str__()

    def verify_move_validity(self, row, column):
        if self._board.get_cell_value(row, column) != "_":
            return False
        if row < 0 or column < 0 or row >= 6 or column >= 7:
            return False
        if row != 5 and self._board.get_cell_value(row + 1, column) == "_":
            return False
        return True

    def verify_if_board_is_full(self):
        empty_cells = self._board.get_empty_cells()
        if len(empty_cells) == 0:
            return True
        return False

    def human_player_move(self, row, column):
        player_symbol = "o"
        self._board.set_value(row, column, player_symbol)

    def get_next_position(self, column):
        return self._board.get_next_free_row(column)

    def computer_move(self):
        player_symbol = "x"
        if self.horizontal_possible_win() is not False:
            row, column = self.horizontal_possible_win()
        elif self.vertical_possible_win() is not False:
            row, column = self.vertical_possible_win()
        elif self.oblique_possible_win() is not False:
            row, column = self.oblique_possible_win()
        else:
            column = random.randint(0, 6)
            row = self.get_next_position(column)

        while self.verify_move_validity(row, column) is False:
            column = random.randint(0, 6)
            row = self.get_next_position(column)
        self._board.set_value(row, column, player_symbol)

    def verify_if_someone_has_won(self):
        if self.horizontal_win() is not False:
            return self.horizontal_win()
        if self.vertical_win() is not False:
            return self.vertical_win()
        if self.oblique_win() is not False:
            return self.oblique_win()
        return False

    def horizontal_possible_win(self):
        """
        chewcks for possible win on horizonntal
        :return: false if there is no possibility
        """        
        for i in range(6):
            row = self._board.get_row_values(i)
            for j in range(4):
                if row[j] == "_" and row[j+1] == row[j+2] == row[j+3] and row[j+1] != "_":
                    return i, j
                if row[j+1] == "_" and row[j] == row[j+2] == row[j+3] and row[j] != "_":
                    return i, j+1
                if row[j+2] == "_" and row[j] == row[j+1] == row[j+3] and row[j] != "_":
                    return i, j+2
                if row[j+3] == "_" and row[j] == row[j+1] == row[j+2] and row[j] != "_":
                    return i, j+3
        return False

    def vertical_possible_win(self):
        """
        checks for possible vertical win for computer
        :return: false if there is no possibility of winning
        """        
        for j in range(7):
            column = self._board.get_column_values(j)
            for i in range(3):
                if column[i] == "_" and column[i + 1] == column[i + 2] == column[i + 3] and column[i + 1] != "_":
                    return i, j
                if column[i + 1] == "_" and column[i] == column[i + 2] == column[i + 3] and column[i] != "_":
                    return i+1, j
                if column[i + 2] == "_" and column[i] == column[i + 1] == column[i + 3] and column[i] != "_":
                    return i+2, j
                if column[i + 3] == "_" and column[i] == column[i + 1] == column[i + 2] and column[i] != "_":
                    return i+3, j
        return False

    def oblique_possible_win(self):
        """
        checks for possible oblique win for computer
        :return: false if there is no possibility of winning
        """            
        for i in range(3):
            for j in range(4):
                left_diagonal = self._board.get_main_diagonal(i, j)
                if left_diagonal[0] == "_" and left_diagonal[1] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[1] != "_":
                    return i, j
                if left_diagonal[1] == "_" and left_diagonal[0] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[0] != "_":
                    return i+1, j+1
                if left_diagonal[2] == "_" and left_diagonal[0] == left_diagonal[1] == left_diagonal[3] and \
                   left_diagonal[0] != "_":
                    return i+2, j+2
                if left_diagonal[3] == "_" and left_diagonal[0] == left_diagonal[1] == left_diagonal[2] and \
                   left_diagonal[0] != "_":
                    return i+3, j+3
            for j in range(3, 7):
                right_diagonal = self._board.get_secondary_diagonal(i, j)
                if right_diagonal[0] == "_" and right_diagonal[1] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[1] != "_":
                    return i, j
                if right_diagonal[1] == "_" and right_diagonal[0] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[0] != "_":
                    return i+1, j-1
                if right_diagonal[2] == "_" and right_diagonal[0] == right_diagonal[1] == right_diagonal[3] and \
                   right_diagonal[0] != "_":
                    return i+2, j-2
                if right_diagonal[3] == "_" and right_diagonal[0] == right_diagonal[1] == right_diagonal[2] and \
                   right_diagonal[0] != "_":
                    return i+3, j-3
        return False

    def horizontal_win(self):
        for i in range(6):
            row = self._board.get_row_values(i)
            for j in range(4):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] and row[j] != "_":
                    return self._board.get_cell_value(i, j)
        return False

    def vertical_win(self):
        for j in range(7):
            column = self._board.get_column_values(j)
            for i in range(3):
                if column[i] == column[i+1] == column[i+2] == column[i+3] and column[i+1] != "_":
                    return self._board.get_cell_value(i, j)
        return False

    def oblique_win(self):
        for i in range(3):
            for j in range(4):
                left_diagonal = self._board.get_main_diagonal(i, j)
                if left_diagonal[0] == left_diagonal[1] == left_diagonal[2] == left_diagonal[3] and \
                   left_diagonal[0] != "_":
                    return self._board.get_cell_value(i, j)
            for j in range(3, 7):
                right_diagonal = self._board.get_secondary_diagonal(i, j)
                if right_diagonal[0] == right_diagonal[1] == right_diagonal[2] == right_diagonal[3] and \
                   right_diagonal[0] != "_":
                    return self._board.get_cell_value(i, j)
        return False
