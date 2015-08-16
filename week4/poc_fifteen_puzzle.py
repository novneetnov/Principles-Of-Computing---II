#http://www.codeskulptor.org/#user39_kFAZ3a1NGk_20.py
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui
import math


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self._grid[target_row][target_col] == 0:
            for row in range(target_row, self._height):
                for col in range(0, self._width):
                    if row == target_row and col <= target_col:
                        continue
                    if self._grid[row][col] != col + row * self._width:
                        return False
            return True
        return False

    def place_tile_at_pos(self, hunt_row, hunt_col, target_row, target_col):
        """
        A helper function that returns the moves required to move the tile at (hunt_row, hunt_col)
        to a solvable configuration.
        """
        ans_moves = ""
        if hunt_col == 0:
            ans_moves += "rdl"
        elif hunt_row == target_row:
            ans_moves += "urdlu"
        elif hunt_col < target_col:
            ans_moves += "drrul"
        elif hunt_row == 0:
            ans_moves += "rdllu"
        else:
            ans_moves += "rulld"
        return ans_moves

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col), "all further tiles not in correct place"
        moves = ""
        if target_row > 1 and target_col > 0:
            hunt_row, hunt_col = self.current_position(target_row, target_col)
            for _ in range(target_row - hunt_row):
                moves += "u"
                self.update_puzzle("u")
            for _ in range(int(math.floor(abs(target_col + 0.5 - hunt_col)))):
                if target_col > hunt_col:
                    moves += "l"
                    self.update_puzzle("l")
                else:
                    moves += "r"
                    self.update_puzzle("r")

            hunt_row, hunt_col = self.current_position(target_row, target_col)
            while hunt_col != target_col:
                ans_moves = self.place_tile_at_pos(hunt_row, hunt_col, target_row, target_col)
                moves += ans_moves
                self.update_puzzle(ans_moves)
                hunt_row, hunt_col = self.current_position(target_row, target_col)

            dummy_zero_tile_row, zero_tile_col = self.current_position(0, 0)
            while hunt_row != target_row or zero_tile_col != target_col - 1:
                if zero_tile_col == hunt_col:
                    moves += "ld"
                    self.update_puzzle("ld")
                else:
                    moves += "druld"
                    self.update_puzzle("druld")
                hunt_row, hunt_col = self.current_position(target_row, target_col)
                dummy_zero_tile_row, zero_tile_col = self.current_position(0, 0)
        assert self.lower_row_invariant(target_row, target_col - 1), "all further tiles not in correct place"
        return moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0), "all further tiles not in correct place"
        if target_row > 1:
            moves = ""
            hunt_row, hunt_col = self.current_position(target_row, 0)
            if hunt_row == target_row - 1 and hunt_col == 0:
                moves += "u"
                self.update_puzzle("u")
            else:
                for _ in range(target_row - hunt_row):
                    moves += "u"
                for _ in range(hunt_col - 1):
                    moves += "r"
                self.update_puzzle(moves)
                while hunt_col != 1:
                    ans_moves = self.place_tile_at_pos(hunt_row, hunt_col, target_row - 1, 1)
                    self.update_puzzle(ans_moves)
                    moves += ans_moves
                    hunt_row, hunt_col = self.current_position(target_row, 0)
                while hunt_row != target_row - 1:
                    moves += "druld"
                    self.update_puzzle("druld")
                    hunt_row, hunt_col = self.current_position(target_row, 0)
                moves += "rulddrulurddlu"
                self.update_puzzle("rulddrulurddlu")
            for _ in range(self._width - 1):
                moves += "r"
                self.update_puzzle("r")
            assert self.lower_row_invariant(target_row - 1, self._width - 1), "all further tiles not in correct place"
            return moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] == 0:
            for row in range(0, self._height):
                for col in range(self._width):
                    if row == 0 and col <= target_col:
                        continue
                    if row == 1 and col < target_col:
                        continue
                    if self._grid[row][col] != col + row * self._width:
                        return False
            return True
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[1][target_col] == 0:
            for row in range(1, self._height):
                for col in range(self._width):
                    if row == 1 and col <= target_col:
                        continue
                    if self._grid[row][col] != row * self._width + col:
                        return False
            return True
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.row0_invariant(target_col), "all further tiles not in correct place"
        moves = ""
        hunt_row, hunt_col = self.current_position(0, target_col)
        if hunt_row == 0 and hunt_col == target_col - 1:
            moves += "ld"
            self.update_puzzle(moves)
        else:
            if hunt_row == 1 and hunt_col == target_col - 1:
                moves += "lld"
                self.update_puzzle(moves)
            else:
                for _ in range(target_col - hunt_col):
                    moves += "l"
                if hunt_row == 1:
                    moves += "drul"
                self.update_puzzle(moves)
                hunt_row, hunt_col = self.current_position(0, target_col)
                while hunt_col != target_col - 1:
                    ans_move = self.place_tile_at_pos(hunt_row, hunt_col, 1, target_col - 1)
                    moves += ans_move
                    self.update_puzzle(ans_move)
                    hunt_row, hunt_col = self.current_position(0, target_col)
                moves += "druld"
                self.update_puzzle("druld")
            moves += "urdlurrdluldrruld"
            self.update_puzzle("urdlurrdluldrruld")
        assert self.row1_invariant(target_col - 1), "all further tiles not in correct place"
        return moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col), "all further tiles not in correct place"
        moves = ""
        hunt_row, hunt_col = self.current_position(1, target_col)
        for _ in range(1 - hunt_row):
            moves += "u"
            self.update_puzzle("u")
        for _ in range(target_col - hunt_col):
            moves += "l"
            self.update_puzzle("l")
        hunt_row, hunt_col = self.current_position(1, target_col)
        while hunt_col != target_col:
            ans_moves = self.place_tile_at_pos(hunt_row, hunt_col, 1, target_col)
            moves += ans_moves
            self.update_puzzle(ans_moves)
            hunt_row, hunt_col = self.current_position(1, target_col)

        zero_tile_row, dummy_zero_tile_col = self.current_position(0, 0)
        if zero_tile_row == 1:
            moves += "ur"
            self.update_puzzle("ur")
        elif hunt_row < 1:
            moves += "dru"
            self.update_puzzle("dru")
        assert self.row0_invariant(target_col), "all further tiles not in correct place"
        return moves
    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1), "all further tiles not in correct place"
        moves = "lu"
        self.update_puzzle(moves)
        for _ in range(3):
            if self._grid[0][1] == 1:
                return moves
            moves += "rdlu"
            self.update_puzzle("rdlu")
        return moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        moves = ""
        zero_tile_row, zero_tile_col = self.current_position(0, 0)
        for _ in range(zero_tile_row, self._height - 1):
            moves += "d"
        for _ in range(zero_tile_col, self._width - 1):
            moves += "r"
        self.update_puzzle(moves)
        for row in range(self._height - 1, 1, -1):
            for col in range(self._width - 1, -1, -1):
                if col == 0:
                    moves += self.solve_col0_tile(row)
                else:
                    moves += self.solve_interior_tile(row, col)
        for col in range(self._width - 1, 1, -1):
            for row in range(1, -1, -1):
                if row == 1:
                    moves += self.solve_row1_tile(col)
                else:
                    moves += self.solve_row0_tile(col)
        moves += self.solve_2x2()
        return moves

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))