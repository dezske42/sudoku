import unittest

from sudoku import Sudoku
from sudoku import row_to_string

fullInitializer = ("1 2 3 4 5 6 7 8 9"
                   "4 5 6 7 8 9 1 2 3"
                   "7 8 9 1 2 3 4 5 6"
                   "2 3 4 5 6 7 8 9 1"
                   "3 4 5 6 7 8 9 1 2"
                   "5 6 7 8 9 1 2 3 4"
                   "6 7 8 9 1 2 3 4 5"
                   "8 9 1 2 3 4 5 6 7"
                   "9 1 2 3 4 5 6 7 8")

puzzle1 = ( "1   4   8 6 5    "
            "8             7 6"
            "3       7        "
            "  8 7   6   3    "
            "6 4 2 7   5 1 9 8"
            "    3   4   7 6  "
            "        2       1"
            "4 6             5"
            "    5 6 1   9   7")

class MyTestCase(unittest.TestCase):
    def test_can_print_board(self):
        sudoString =      ("1 2 3 4 5 6 7 8 9\n"
                           "4 5 6 7 8 9 1 2 3\n"
                           "7 8 9 1 2 3 4 5 6\n"
                           "2 3 4 5 6 7 8 9 1\n"
                           "3 4 5 6 7 8 9 1 2\n"
                           "5 6 7 8 9 1 2 3 4\n"
                           "6 7 8 9 1 2 3 4 5\n"
                           "8 9 1 2 3 4 5 6 7\n"
                           "9 1 2 3 4 5 6 7 8\n")
        sudo = Sudoku(fullInitializer)
        self.assertEqual(str(sudo), sudoString)

    def test_at_top_left_corner(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.at(0,0), "1")

    def test_at_bottom_right_corner(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.at(8,8), "8")

    def test_empty_at_top_left_corner(self):
        sudo = Sudoku()
        self.assertEqual(sudo.at(0,0), " ")

    def test_empty_at_top_left_corner(self):
        sudo = Sudoku()
        self.assertEqual(sudo.at(8,8), " ")

    def test_row_to_string(self):
        self.assertEqual(row_to_string("123456789"),"1 2 3 4 5 6 7 8 9")

    def test_first_row_is_empty(self):
        emptySudo = Sudoku()
        self.assertEqual(emptySudo.row_set(0), set())

    def test_first_row_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.row_set(0), set([str(digit) for digit in range(1,10)]))

    def test_last_row_is_empty(self):
        emptySudo = Sudoku()
        self.assertEqual(emptySudo.row_set(0), set())

    def test_last_row_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.row_set(0), set([str(digit) for digit in range(1,10)]))

    def test_first_row_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.row_set(0), {"1", "4", "5", "6", "8"})

    def test_last_row_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.row_set(8), {"1", "5", "6", "7", "9"})

    def test_first_column_is_empty(self):
        emptySudo = Sudoku()
        self.assertEqual(emptySudo.column_set(0), set())

    def test_first_column_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.column_set(0), set([str(digit) for digit in range(1,10)]))

    def test_first_column_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.column_set(0), {"1", "3", "4", "6", "8"})

    def test_last_column_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.column_set(8), {"1", "5", "6", "7", "8"})

    def test_top_left_square_is_empty(self):
        sudo = Sudoku()
        self.assertEqual(sudo.square_set(0,0), set())

    def test_top_left_square_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.square_set(0,0), set([str(digit) for digit in range(1,10)]))

    def test_top_left_square_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.square_set(0,0), {"1", "3", "4", "8"})

    def test_bottom_right_square_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.square_set(2,2), {"1", "5", "7", "9"})

if __name__ == '__main__':
    unittest.main()
