import CourseraPoc2.util.poc_simpletest as simpletest
import poc_fifteen_puzzle as puzzle

suite = simpletest.TestSuite()


def run_lower_row_invariant():

    puzz = puzzle.Puzzle(4, 4)
    suite.run_test(puzz.lower_row_invariant(0, 0), True, "Test #1:")

    puzz = puzzle.Puzzle(3, 3, [[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    suite.run_test(puzz.lower_row_invariant(1, 1), True, "Test #2:")

    puzz = puzzle.Puzzle(3, 3, [[1, 2, 0], [3, 4, 5], [6, 7, 8]])
    suite.run_test(puzz.lower_row_invariant(1, 1), False, "Test #3:")

    puzz = puzzle.Puzzle(3, 3, [[1, 2, 0], [3, 4, 5], [6, 7, 8]])
    suite.run_test(puzz.lower_row_invariant(0, 2), True, "Test #4:")

    puzz = puzzle.Puzzle(4, 5, [[15, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [12, 16, 17, 18, 19]])
    suite.run_test(puzz.lower_row_invariant(2, 2), False, "Test #5:")

    suite.report_results()


def run_solve_interior_tile():

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 1), "l", "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 9], [8, 0, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 1), "urrulldrullddruld", "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [9, 6, 7, 5], [8, 0, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 1), "uldruld", "Test #3:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 9], [5, 6, 7, 4], [8, 0, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 1), "uurrdllurdlludrulddruld", "Test #4:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [10, 9, 0, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 2), "llurdludrruldruld", "Test #5:")

    puzz = puzzle.Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    suite.run_test(puzz.solve_interior_tile(2, 2), "uulldrruldrulddruld", "Test #6:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 10, 7], [8, 9, 0, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_interior_tile(2, 2), "uld", "Test #7:")

    suite.report_results()


def run_solve_col0_tile():

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_col0_tile(2), "urrurdlurdllurdlludruldrulddrulurddlurrr", "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [8, 6, 7, 5], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_col0_tile(2), "urrr", "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[8, 2, 3, 4], [1, 6, 7, 5], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_col0_tile(2), "uurdlrulddrulurddlurrr", "Test #3:")

    puzz = puzzle.Puzzle(4, 4, [[2, 8, 3, 4], [1, 6, 7, 5], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_col0_tile(2), "uudruldrulddrulurddlurrr", "Test #4:")

    puzz = puzzle.Puzzle(4, 4, [[2, 4, 3, 8], [1, 6, 7, 5], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_col0_tile(2), "uurrrdllurdlludruldrulddrulurddlurrr", "Test #5:")

    suite.report_results()


def run_row0_invariant():

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row0_invariant(3), False, "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row0_invariant(3), False, "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 0, 3], [5, 4, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row0_invariant(2), True, "Test #3:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 0], [4, 6, 5, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row0_invariant(3), True, "Test #4:")

    suite.report_results()


def run_row1_invariant():

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row1_invariant(3), False, "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row1_invariant(3), True, "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 9, 0], [8, 7, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.row1_invariant(3), False, "Test #3:")

    suite.report_results()


def run_solve_row1_tile():

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row1_tile(3), "lur", "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[7, 2, 3, 4], [5, 6, 1, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row1_tile(3), "ullldrruldrruldru", "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[5, 2, 3, 4], [7, 6, 1, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row1_tile(3), "lllurdludrruldrruldru", "Test #3:")

    puzz = puzzle.Puzzle(4, 4, [[5, 2, 3, 7], [4, 6, 1, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row1_tile(3), "u", "Test #4:")

    puzz = puzzle.Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
    suite.run_test(puzz.solve_row1_tile(2), "uldru", "Test #5:")

    suite.report_results()


def run_solve_row0_tile():

    puzz = puzzle.Puzzle(3, 3, [[2, 1, 0], [4, 3, 5], [6, 7, 8]])
    suite.run_test(puzz.solve_row0_tile(2), "lldruldurdlurrdluldrruld", "Test #1:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 3, 0], [4, 6, 5, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row0_tile(3), "ld", "Test #2:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 5, 0], [4, 6, 3, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row0_tile(3), "lldurdlurrdluldrruld", "Test #3:")

    puzz = puzzle.Puzzle(4, 4, [[1, 2, 5, 0], [3, 6, 4, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    suite.run_test(puzz.solve_row0_tile(3), "llldruldrruldruldurdlurrdluldrruld", "Test #4:")

    suite.report_results()


def run_solve_2x2():

    puzz = puzzle.Puzzle(3, 3, [[3, 1, 2], [4, 0, 5], [6, 7, 8]])
    suite.run_test(puzz.solve_2x2(), "lu", "Test #1:")

    puzz = puzzle.Puzzle(2, 2, [[1, 3], [2, 0]])
    suite.run_test(puzz.solve_2x2(), "lurdlurdlu", "Test #2:")

    suite.report_results()


def run_test():
    run_lower_row_invariant()
    #run_solve_interior_tile()
    #run_solve_col0_tile()
    #run_row0_invariant()
    #run_row1_invariant()
    #run_solve_row1_tile()
    #run_solve_row0_tile()
    #run_solve_2x2()

run_test()