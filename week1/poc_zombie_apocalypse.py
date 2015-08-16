"""
Student portion of Zombie Apocalypse mini-project
"""

import random
from CourseraPoc2.util import poc_grid
from CourseraPoc2.util import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        distance_field = [[self._grid_width * self._grid_height for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self._zombie_list:
                boundary.enqueue(zombie)
                visited[zombie[0]][zombie[1]] = FULL
                distance_field[zombie[0]][zombie[1]] = 0
        else:
            for human in self._human_list:
                boundary.enqueue(human)
                visited[human[0]][human[1]] = FULL
                distance_field[human[0]][human[1]] = 0

        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            neighbours = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbour in neighbours:
                if visited[neighbour[0]][neighbour[1]] is EMPTY and self.is_empty(neighbour[0], neighbour[1]):
                    visited[neighbour[0]][neighbour[1]] = FULL
                    boundary.enqueue(neighbour)
                    distance_field[neighbour[0]][neighbour[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human_idx in range(len(self._human_list)):
            human = self._human_list[human_idx]
            eight_neighbours = self.eight_neighbors(human[0], human[1])
            eight_neighbours_tuples = [(human, zombie_distance[human[0]][human[1]])]
            for neighbour in eight_neighbours:
                distance_neighbour = zombie_distance[neighbour[0]][neighbour[1]]
                if distance_neighbour < self._grid_width * self._grid_height and self._human_list.count(neighbour) == 0:
                    if distance_neighbour > eight_neighbours_tuples[0][1]:
                        eight_neighbours_tuples = [(neighbour, distance_neighbour)]
                    elif distance_neighbour == eight_neighbours_tuples[0][1]:
                        eight_neighbours_tuples.append((neighbour, distance_neighbour))
            farthest_zombie_move = random.choice(eight_neighbours_tuples)
            self._human_list[human_idx] = farthest_zombie_move[0]

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for zombie_idx in range(len(self._zombie_list)):
            zombie = self._zombie_list[zombie_idx]
            four_neighbours = self.four_neighbors(zombie[0], zombie[1])
            four_neighbours_tuples = [(zombie, human_distance[zombie[0]][zombie[1]])]
            for neighbour in four_neighbours:
                if self._zombie_list.count(neighbour) == 0:
                    distance_neighbour = human_distance[neighbour[0]][neighbour[1]]
                    if distance_neighbour < self._grid_height * self._grid_width:
                        if distance_neighbour < four_neighbours_tuples[0][1]:
                            four_neighbours_tuples = [(neighbour, distance_neighbour)]
                        elif distance_neighbour == four_neighbours_tuples[0][1]:
                            four_neighbours_tuples.append((neighbour, distance_neighbour))
            nearest_human_move = random.choice(four_neighbours_tuples)
            self._zombie_list[zombie_idx] = nearest_human_move[0]



# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Zombie(30, 40))
#poc_zombie_gui.run_gui(Zombie( 30 , 40 ,
#[(2, 1), (0, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (0, 3), (5, 3), (13, 3), (0, 4), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5), (13, 5), (3, 6), (5, 6), (13, 6), (1, 7), (3, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (1, 8), (3, 8), (5, 8), (9, 8), (13, 8), (1, 9), (5, 9), (6, 9), (7, 9), (9, 9), (13, 9), (14, 9), (15, 9), (16, 9), (18, 9), (19, 9), (21, 9), (22, 9), (23, 9), (24, 9), (25, 9), (26, 9), (27, 9), (28, 9), (29, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (7, 10), (8, 10), (9, 10), (16, 10), (21, 10), (24, 10), (16, 11), (21, 11), (24, 11), (16, 12), (17, 12), (19, 12), (20, 12), (21, 12), (24, 12), (0, 13), (1, 13), (2, 13), (3, 13), (6, 13), (7, 13), (8, 13), (12, 13), (13, 13), (14, 13), (15, 13), (16, 13), (24, 13), (4, 14), (5, 14), (9, 14), (10, 14), (11, 14), (16, 14), (17, 14), (19, 14), (20, 14), (21, 14), (24, 14), (25, 14), (26, 14), (17, 15), (19, 15), (22, 15), (26, 15), (16, 16), (20, 16), (23, 16), (25, 16), (15, 17), (21, 17), (24, 17), (0, 18), (1, 18), (14, 18), (22, 18), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (23, 19), (14, 20), (22, 20), (14, 21), (21, 21), (15, 22), (20, 22), (2, 23), (4, 23), (16, 23), (19, 23), (1, 24), (5, 24), (16, 24), (17, 24), (18, 24), (0, 25), (6, 25), (11, 25), (12, 25), (13, 25), (14, 25), (15, 25), (19, 25), (20, 25), (7, 26), (11, 26), (21, 26), (8, 27), (9, 27), (10, 27), (11, 27), (13, 27), (14, 27), (15, 27), (22, 27), (13, 28), (15, 28), (16, 28), (17, 28), (18, 28), (19, 28), (20, 28), (21, 28), (22, 28), (23, 28), (8, 29), (9, 29), (10, 29), (11, 29), (12, 29), (13, 29), (24, 29), (7, 30), (8, 30), (25, 30), (0, 31), (6, 31), (26, 31), (1, 32), (5, 32), (27, 32), (2, 33), (4, 33), (28, 33), (14, 34), (15, 34), (16, 34), (20, 34), (21, 34), (22, 34), (26, 34), (27, 34), (28, 34), (29, 34), (0, 35), (1, 35), (2, 35), (3, 35), (4, 35), (5, 35), (7, 35), (8, 35), (9, 35), (10, 35), (11, 35), (12, 35), (13, 35), (17, 35), (18, 35), (19, 35), (23, 35), (24, 35), (25, 35), (29, 35), (4, 36), (21, 36), (28, 36), (4, 37), (5, 37), (6, 37), (7, 37), (8, 37), (10, 37), (11, 37), (12, 37), (13, 37), (14, 37), (18, 37), (19, 37), (20, 37), (21, 37), (23, 37), (24, 37), (25, 37), (26, 37), (27, 37), (14, 38), (15, 38), (16, 38), (17, 38), (18, 38), (26, 38), (27, 39)] ,
#[(27, 3), (25, 10), (18, 11), (6, 16), (3, 28), (3, 38)] ,
#[(17, 4)] ))
#poc_zombie_gui.run_gui(Zombie( 30 , 40 ,
#[(0, 0), (8, 0), (23, 0), (29, 0), (7, 1), (12, 1), (22, 1), (6, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (4, 3), (5, 3), (12, 3), (22, 3), (4, 4), (11, 4), (23, 4), (24, 4), (25, 4), (4, 5), (11, 5), (15, 5), (16, 5), (26, 5), (4, 6), (10, 6), (14, 6), (17, 6), (27, 6), (29, 6), (0, 7), (4, 7), (6, 7), (7, 7), (8, 7), (9, 7), (13, 7), (18, 7), (28, 7), (0, 8), (1, 8), (10, 8), (11, 8), (12, 8), (19, 8), (20, 8), (21, 8), (23, 8), (24, 8), (25, 8), (26, 8), (28, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (21, 9), (23, 9), (26, 9), (0, 10), (10, 10), (11, 10), (12, 10), (26, 10), (27, 10), (28, 10), (13, 11), (14, 11), (15, 11), (16, 11), (21, 11), (5, 12), (6, 12), (7, 12), (8, 12), (17, 12), (18, 12), (19, 12), (20, 12), (21, 12), (22, 12), (23, 12), (24, 12), (25, 12), (26, 12), (28, 12), (29, 12), (0, 13), (2, 13), (3, 13), (4, 13), (9, 13), (10, 13), (11, 13), (27, 13), (29, 13), (0, 14), (1, 14), (10, 14), (12, 14), (13, 14), (14, 14), (15, 14), (0, 15), (13, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (26, 15), (27, 15), (28, 15), (29, 15), (10, 16), (13, 16), (16, 16), (18, 16), (19, 16), (20, 16), (29, 16), (10, 17), (11, 17), (12, 17), (13, 17), (16, 17), (19, 17), (19, 18), (15, 19), (20, 19), (9, 20), (11, 20), (15, 20), (16, 20), (19, 20), (0, 21), (8, 21), (10, 21), (12, 21), (13, 21), (14, 21), (15, 21), (16, 21), (17, 21), (18, 21), (19, 21), (0, 22), (1, 22), (2, 22), (3, 22), (4, 22), (5, 22), (6, 22), (7, 22), (10, 22), (18, 22), (19, 22), (20, 22), (22, 22), (7, 23), (10, 23), (12, 23), (14, 23), (19, 23), (20, 23), (21, 23), (23, 23), (24, 23), (25, 23), (26, 23), (27, 23), (28, 23), (1, 24), (2, 24), (3, 24), (5, 24), (7, 24), (8, 24), (10, 24), (13, 24), (19, 24), (1, 25), (3, 25), (5, 25), (7, 25), (10, 25), (19, 25), (1, 26), (3, 26), (4, 26), (5, 26), (7, 26), (9, 26), (10, 26), (18, 26), (19, 26), (21, 26), (22, 26), (23, 26), (24, 26), (25, 26), (26, 26), (27, 26), (28, 26), (7, 27), (10, 27), (16, 27), (18, 27), (25, 27), (2, 28), (3, 28), (4, 28), (5, 28), (7, 28), (8, 28), (10, 28), (15, 28), (18, 28), (25, 28), (1, 29), (2, 29), (3, 29), (4, 29), (7, 29), (10, 29), (11, 29), (12, 29), (13, 29), (16, 29), (18, 29), (19, 29), (21, 29), (25, 29), (26, 29), (27, 29), (29, 29), (2, 30), (3, 30), (7, 30), (13, 30), (18, 30), (19, 30), (20, 30), (22, 30), (23, 30), (24, 30), (25, 30), (26, 30), (27, 30), (29, 30), (4, 31), (5, 31), (7, 31), (9, 31), (11, 31), (13, 31), (18, 31), (7, 32), (10, 32), (12, 32), (18, 32), (25, 32), (26, 32), (27, 32), (28, 32), (29, 32), (1, 33), (2, 33), (3, 33), (4, 33), (5, 33), (7, 33), (9, 33), (10, 33), (13, 33), (15, 33), (18, 33), (20, 33), (21, 33), (22, 33), (23, 33), (24, 33), (29, 33), (1, 34), (3, 34), (7, 34), (13, 34), (16, 34), (19, 34), (1, 35), (8, 35), (9, 35), (10, 35), (11, 35), (12, 35), (13, 35), (15, 35), (20, 35), (7, 36), (21, 36), (1, 37), (2, 37), (3, 37), (4, 37), (5, 37), (7, 37), (11, 37), (18, 37), (22, 37), (1, 38), (3, 38), (5, 38), (7, 38), (10, 38), (12, 38), (17, 38), (19, 38), (22, 38), (1, 39), (5, 39), (7, 39), (8, 39), (21, 39), (22, 39), (29, 39)] ,
#[(6, 1), (29, 1), (5, 2), (2, 5), (29, 7), (29, 11), (4, 18), (12, 26), (26, 27), (26, 28), (9, 30), (25, 35)] ,
#[(7, 3)] ))
