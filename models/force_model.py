import math


class Force:
    def __init__(self, node, value, rotation):
        node_number = node.number
        self.node = node
        self.angle = math.radians(rotation)
        self.value = value
        self.forces = {
            node_number * 2 - 1: math.cos(self.angle) * value,
            node_number * 2: math.sin(self.angle) * value,
        }
