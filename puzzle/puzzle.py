"""
Its a fork from
https://github.com/Jain-Pratiksha/Python/blob/master/Artificial%20Intelligence/AI_EXP3_Puzzle.py
but this code have better CLI application and it shows the steps correctly.
"""

from copy import deepcopy


class Node:
    def __init__(self, data, level, fval) -> None:
        self.data = data
        self.level = level  # g(x)
        self.fval = fval
        self.parent = None
        self.children: list[Node] = []

    def generate_child(self):
        # Generate hild nodes from the given node by moving the blank space
        # either in the four direction {up,down,left,right}
        x, y = self.find(self.data, '_')

        # the 4 direction [up,down,left,right] respectively.
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                self.children.append(child_node)

    def shuffle(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction
            and if the position value are out
        """

        # Of limits the return None
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = deepcopy(puz)
            temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2],  temp_puz[x1][y1]
            return temp_puz
        else:
            return None

    def find(self, puz, x):
        # Specifically used to find the position of the blank space
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

    def __eq__(self, __value: object) -> bool:
        return self.data == __value.data


class Puzzle:
    def __init__(self, start, goal, size, h_function) -> None:
        self.start = Node(start, 0, 0)
        self.goal = goal
        self.h_function = h_function
        self.n = size
        self.steps = 0
        self.node_searched = 0

    def f(self, start: Node):
        # f(x) = h(x) + g(x)
        return self.h_function(start.data, self.goal) + start.level

    def get_path(self, node: Node) -> list[Node]:
        path = []
        current_node = node

        while current_node.parent is not None:
            path.append(current_node)
            current_node = current_node.parent

        path.reverse()
        return path

    def is_goal(self, node: Node):
        return self.h_function(node.data, self.goal) == 0

    def a_star(self):
        self.start.fval = self.f(self.start)
        self.open: list[Node] = [self.start]
        self.closed: list[Node] = []

        while self.open:
            current_node = min(self.open, key=lambda k: k.fval)
            self.open.remove(current_node)
            self.closed.append(current_node)

            if self.is_goal(current_node):
                return self.get_path(current_node)

            current_node.generate_child()
            for ch in current_node.children:
                if ch in self.closed:
                    continue

                self.node_searched += 1
                ch.fval = self.f(ch)
                ch.parent = current_node
                self.open.append(ch)

    def __show_node_data(self, node: Node, num: int):
        print(f'-------------"{num+1}"----------------')
        for r in node.data:
            for tile in r:
                print(tile, end=" ")
            print()

    def calculate(self, show_steps: bool):
        print('=====================================')
        path = self.a_star()
        if path is None:
            print("This puzzle cant be solve.")
        else:
            self.steps = len(path)

        if path and show_steps:
            print("The Steps:")
            for idx, n in enumerate(path):
                self.__show_node_data(n, idx)

            print(f"In {self.steps} steps and \
                  {self.node_searched} nodes searched!")
