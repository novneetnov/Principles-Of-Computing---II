"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import random

# Set timeout, as mini-max can take a long time
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # find the children of the board - by provided.get_empty_squares and provided.check_win
    switch_player = provided.switch_player(player)
    child_draw_boards = []
    child_lose_boards = []
    if board.check_win() is None:
        empty_squares = board.get_empty_squares()
        # Iterate on the children - and mm_move on them. If any child returns the winning move return the max/min score
        # and the child board.
        for square in empty_squares:
            child_board = board.clone()
            child_board.move(square[0], square[1], player)
            score_child = mm_move(child_board, switch_player)
            if score_child[0] * SCORES[player] == 1:
                return score_child[0], square
            elif score_child[0] == 0:
                child_draw_boards.append((score_child[0], square))
            elif score_child[0] * SCORES[player] == -1 and not child_draw_boards:
                child_lose_boards.append((score_child[0], square))
        if not child_draw_boards:
            return random.choice(child_lose_boards)
        else:
            return random.choice(child_draw_boards)
    else:
        # Base Case : If no children return score of the board, (-1, -1). Score can be determined by provided.check_win
        winner = board.check_win()
        return SCORES[winner], (-1, -1)


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, move_wrapper, 1, False)
