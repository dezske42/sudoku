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

    def at(self, pos):
        return self.rows[pos[0]][pos[1]]

    def row_niner(self, row):
        return [(row,column) for column in range(0,9)]

    def column_niner(self, column):
        return [(row,column) for row in range(0,9)]

    def square_niner(self, row, column):
        niner = []
        for r in range(3):
            niner.extend([(row*3+r,column*3+c) for c in range(0,3)])
        return niner

    def all_enclosing_niners(self, row, column):
        return self.row_niner(row) + self.column_niner(column) +self.square_niner(row//3,column//3)

    def niner_set(self, niner):
        return set([self.at(pos) for pos in niner]) - {' '}

    def excluded_at(self, anchor):
        row, column = anchor
        return set([self.at(pos) for pos in self.all_enclosing_niners(row, column)]) - {self.at(anchor)}

    def possible_at(self, pos):
        cell = self.at(pos)
        if cell == " ":
            return self.all_digits - self.excluded_at(pos)
        else:
            return set(cell)

    def where_is_digit_possible_in_niner(self, digit, niner):
        return set([pos for pos in niner if digit in self.possible_at(pos)])

    def set_digit(self, pos, digit):
        row, column = pos
        self.rows[row] = self.rows[row][0:column] + digit + self.rows[row][column + 1:]

    def fill_only_possible_by_niner(self, niner):
        progress = False
        existing_digits = set([self.at(pos) for pos in niner]) - {' '}
        for digit in self.all_digits - existing_digits:
            digit_is_possible_at = self.where_is_digit_possible_in_niner(digit, niner)
            if len(digit_is_possible_at) == 1:
                pos = next(iter(digit_is_possible_at))
                self.set_digit(pos,digit)
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

    all_niners = []
    for index in range(0,9):
        all_niners.append(sudo.row_niner(index))
        all_niners.append(sudo.column_niner(index))

    anyProgress = True
    while anyProgress:
        anyProgress = False
        for niner in all_niners:
            progress = sudo.fill_only_possible_by_niner(niner)
            if progress:
                print(str(sudo) + "\n")
                anyProgress = True
