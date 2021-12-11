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

all_digits = frozenset([str(digit) for digit in range(1, 10)])

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
        self.assertEqual(sudo.at((0,0)), "1")

    def test_at_bottom_right_corner(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.at((8,8)), "8")

    def test_empty_at_top_left_corner(self):
        sudo = Sudoku()
        self.assertEqual(sudo.at((0,0)), " ")

    def test_empty_at_top_left_corner(self):
        sudo = Sudoku()
        self.assertEqual(sudo.at((8,8)), " ")

    def test_row_to_string(self):
        self.assertEqual(row_to_string("123456789"),"1 2 3 4 5 6 7 8 9")

    def test_top_left_square_niner(self):
        sudo = Sudoku()
        niner = sudo.square_niner(0,0)
        self.assertEqual(niner,[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])

    def test_square_niner_1_2(self):
        sudo = Sudoku()
        niner = sudo.square_niner(1,2)
        self.assertEqual(niner,[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)])

    def test_row_niner_3(self):
        sudo = Sudoku()
        self.assertEqual(sudo.row_niner(3),[(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)])

    def test_column_niner_5(self):
        sudo = Sudoku()
        self.assertEqual(sudo.column_niner(5),[(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5)])

    def test_first_row_is_empty(self):
        emptySudo = Sudoku()
        self.assertEqual(emptySudo.niner_set(emptySudo.row_niner(0)), set())

    def test_first_row_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.niner_set(sudo.row_niner(0)), all_digits)

    def test_last_row_is_empty(self):
        emptySudo = Sudoku()
        self.assertEqual(emptySudo.niner_set(emptySudo.row_niner(8)), set())

    def test_last_row_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.niner_set(sudo.row_niner(8)), all_digits)

    def test_first_row_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.row_niner(0)), {"1", "4", "5", "6", "8"})

    def test_last_row_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.row_niner(8)), {"1", "5", "6", "7", "9"})

    def test_first_column_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.column_niner(0)), {"1", "3", "4", "6", "8"})

    def test_last_column_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.column_niner(8)), {"1", "5", "6", "7", "8"})

    def test_top_left_square_is_empty(self):
        sudo = Sudoku()
        self.assertEqual(sudo.niner_set(sudo.square_niner(0,0)), set())

    def test_top_left_square_is_full(self):
        sudo = Sudoku(fullInitializer)
        self.assertEqual(sudo.niner_set(sudo.square_niner(0,0)), all_digits)

    def test_top_left_square_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.square_niner(0,0)), {"1", "3", "4", "8"})

    def test_bottom_right_square_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.niner_set(sudo.square_niner(2,2)), {"1", "5", "7", "9"})

    def test_possible_at_top_left_of_empty(self):
        sudo = Sudoku()
        self.assertEqual(sudo.possible_at((0,0)), all_digits)

    def test_possible_at_top_left_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.possible_at((0,0)), {"1"})

    def test_possible_at_bottom_right_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.possible_at((8,8)), {"7"})

    def test_possible_at_0_1_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.possible_at((0,1)), {"2", "7", "9"})

    def test_possible_at_1_1_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.possible_at((1,1)), {"2", "5", "9"})

    def test_where_is_1_possbile_in_row_0_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.where_is_digit_possible_in_niner("1", sudo.row_niner(0)), {(0,0)})

    def test_where_is_4_possbile_in_row_0_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.where_is_digit_possible_in_niner("4", sudo.row_niner(0)), {(0,2)})

    def test_where_is_7_possbile_in_row_0_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.where_is_digit_possible_in_niner("7", sudo.row_niner(0)), {(0,1)})

    def test_where_is_6_possbile_in_row_3_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        self.assertEqual(sudo.where_is_digit_possible_in_niner("6", sudo.row_niner(3)), {(3,4)})

    def test_fill_only_possible_by_row_0_of_puzzle1(self):
        sudo = Sudoku(puzzle1)
        filled = Sudoku( "1 7 4   8 6 5    "
                         "8             7 6"
                         "3       7        "
                         "  8 7   6   3    "
                         "6 4 2 7   5 1 9 8"
                         "    3   4   7 6  "
                         "        2       1"
                         "4 6             5"
                         "    5 6 1   9   7")
        sudo.fill_only_possible_by_niner(sudo.row_niner(0))
        self.assertEqual(str(sudo), str(filled))

    def test_fill_only_possible_by_column_0_of_puzzle1(self):
        sudo =    Sudoku( "1 7 4   8 6 5    "
                         "8             7 6"
                         "3       7        "
                         "  8 7   6   3    "
                         "6 4 2 7   5 1 9 8"
                         "    3   4   7 6  "
                         "        2       1"
                         "4 6             5"
                         "    5 6 1   9   7")
        filled = Sudoku( "1 7 4   8 6 5    "
                         "8             7 6"
                         "3       7        "
                         "  8 7   6   3    "
                         "6 4 2 7   5 1 9 8"
                         "    3   4   7 6  "
                         "7       2       1"
                         "4 6             5"
                         "2   5 6 1   9   7")
        sudo.fill_only_possible_by_niner(sudo.column_niner(0))
        self.assertEqual(str(sudo), str(filled))

if __name__ == '__main__':
    unittest.main()
