import math
import CourseraPoc2.util.poc_simpletest as simpletest
import poc_tttmm_solution as tttmm
import poc_ttt_provided as provided

suite = simpletest.TestSuite()


def run_mm_move():

    board = provided.TTTBoard(3, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                        [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                                        [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
    player = provided.PLAYERX
    suite.run_test(tttmm.mm_move(board, player), (0, (-1, -1)), "Test #1:")


    board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO],
                                        [provided.PLAYERX, provided.PLAYERX, provided.EMPTY],
                                        [provided.PLAYERX, provided.EMPTY, provided.PLAYERO]])
    player = provided.PLAYERX
    suite.run_test(tttmm.mm_move(board, player), (1, (-1, -1)), "Test #2:")


    board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO],
                                        [provided.EMPTY, provided.PLAYERX, provided.EMPTY],
                                        [provided.PLAYERX, provided.EMPTY, provided.PLAYERO]])
    player = provided.PLAYERX
    suite.run_test(tttmm.mm_move(board, player), (1, (1, 0)), "Test #3:")


    board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
                                        [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                                        [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])
    player = provided.PLAYERX
    suite.run_test(tttmm.mm_move(board, player), (0, (1, 2)), "Test #4:")


    board = provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.PLAYERX],
                                [provided.EMPTY, provided.EMPTY, provided.EMPTY],
                                [provided.EMPTY, provided.EMPTY, provided.EMPTY]])
    player = provided.PLAYERO
    suite.run_test(tttmm.mm_move(board, player), (0, (1, 1)), "Test #5:")

    suite.report_results()


def run_test():
    run_mm_move()

run_test()