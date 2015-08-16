import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

NODE_HEIGHT = 100
NODE_WIDTH = 100


class TreeDisplay:

    def __init__(self, tree):
        self._tree = tree
        self.canvas_width, self.canvas_height = self.get_box_size(self._tree)
        self._frame = simplegui.create_frame("Tree Diagram", self.canvas_width, self.canvas_height)
        self._frame.set_canvas_background("White")
        self._frame.set_draw_handler(self.draw)
        self._frame.start()

    def get_box_size(self, tree):
        tree_height = 0
        children_width = 0
        for child in tree.children():
            tree_height = max(tree_height, self.get_box_size(child)[1])
            children_width += self.get_box_size(child)[0]
        canvas_width = max(NODE_WIDTH, children_width)
        canvas_height = NODE_HEIGHT + tree_height
        return canvas_width, canvas_height

    def draw(self, canvas):

        self.draw_tree(canvas, self._tree, [0, 0])

    def draw_tree(self, canvas, tree, pos):
        """
        Recursively draw a tree on the canvas
        pos is the position of the upper left corner of the bounding box
        """
        # compute horizontal position for left boundary of each subtree
        dummy_ans = self.get_box_size(tree)
        root_center = [(dummy_ans[0] + 2 * pos[0]) / 2, pos[1] + NODE_HEIGHT / 2]
        children_boundary_list = [pos[0]]
        for child in tree.children():
            child_box_width, dummy_child_height = self.get_box_size(child)
            children_boundary_list.append(children_boundary_list[-1] + child_box_width)

        for idx in range(len(children_boundary_list) - 1):
            child_center = [(children_boundary_list[idx] + children_boundary_list[idx + 1]) / 2,
                            pos[1] + 3 * NODE_HEIGHT / 2]
            canvas.draw_line(root_center, child_center, 3, "Black")

        canvas.draw_circle(root_center, NODE_HEIGHT / 4, 2, "Black", "LightGreen")
        text_pos = [root_center[0] - NODE_HEIGHT / 12, root_center[1] + NODE_HEIGHT / 12]
        canvas.draw_text(tree.get_value(), text_pos, NODE_HEIGHT / 4, "Black")

        for child, boundary in zip(tree.children(), children_boundary_list):
            self.draw_tree(canvas, child, [boundary, pos[1] + NODE_HEIGHT])

