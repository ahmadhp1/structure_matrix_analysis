import math


class Force:
    def __init__(self, node, value, rotation):
        node_number = node.number
        angle = math.radians(rotation)
        print(angle)
        self.forces = {
            node_number * 2 - 1: math.cos(angle) * value,
            node_number * 2: math.sin(angle) * value,
        }
