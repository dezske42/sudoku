def row_to_string(row):
    return " ".join([digit for digit in row])

class Sudoku:
    all_digits = frozenset([str(digit) for digit in range(1,10)])

    def __init__(self, s = None):
        self.rows = []
        for i in range(9):
            if s:
                self.rows.append(s[i*17:i*17+17:2])
            else:
                self.rows.append("         ")

    def __str__(self):
        s = ""
        for i in range(9):
            s += row_to_string(self.rows[i]) + '\n'
        return s

    def at(self, row, column):
        return self.rows[row][column]

    def row_set(self, row):
        return set([digit for digit in self.rows[row]]) - {' '}

    def column_set(self, column):
        return set([self.rows[row][column] for row in range(0,9)]) - {' '}

    def square_set(self, row, column):
        square = set()
        for r in range(3):
            square.update([digit for digit in self.rows[row*3+r][column*3:column*3+3]])
        return square - {' '}

    def possible_at(self, row, column):
        cell = self.at(row, column)
        if cell == " ":
            return self.all_digits - self.row_set(row) - self.column_set(column) - self.square_set(row//3,column//3)
        else:
            return set(cell)

    def where_is_digit_possible_in_row(self, digit, row):
        # just to speed up
        index = self.rows[row].find(digit)
        if index != -1:
            return set([index])

        # this is sufficient to pass unit tests
        where = set()
        for column in range(0, 9):
            if digit in self.possible_at(row,column):
                where.add(column)
        return where

    def where_is_digit_possible_in_column(self, digit, column):
        where = set()
        for row in range(0, 9):
            if digit in self.possible_at(row,column):
                where.add(row)
        return where

    def fill_only_possible_by_row(self, row):
        for digit in self.all_digits - self.row_set(row):
            digit_is_possible_at = self.where_is_digit_possible_in_row(digit, row)
            if len(digit_is_possible_at) == 1:
                column = next(iter(digit_is_possible_at))
                self.rows[row]= self.rows[row][0:column] + digit + self.rows[row][column+1:]

    def fill_only_possible_by_column(self, column):
        progress = False
        for digit in self.all_digits - self.column_set(column):
            digit_is_possible_at = self.where_is_digit_possible_in_column(digit, column)
            if len(digit_is_possible_at) == 1:
                row = next(iter(digit_is_possible_at))
                self.rows[row]= self.rows[row][0:column] + digit + self.rows[row][column+1:]
                progress = True
        return progress

if __name__ == '__main__':
    puzzle = ("1   4   8 6 5    "
              "8             7 6"
              "3       7        "
              "  8 7   6   3    "
              "6 4 2 7   5 1 9 8"
              "    3   4   7 6  "
              "        2       1"
              "4 6             5"
              "    5 6 1   9   7")
    sudo = Sudoku(puzzle)
    print(str(sudo) + "\n")
    anyProgress = True
    while anyProgress:
        anyProgress = False
        for row in range(0, 9):
            progress = sudo.fill_only_possible_by_row(row)
            if progress:
                print(str(sudo) + "\n")
                anyProgress = True
        for column in range(0, 9):
            progress = sudo.fill_only_possible_by_column(column)
            if progress:
                print(str(sudo) + "\n")
                anyProgress = True