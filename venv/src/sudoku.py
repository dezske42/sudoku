def row_to_string(row):
    return " ".join([digit for digit in row])

class Sudoku:
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