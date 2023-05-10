from models.coordinate_model import Coordinate


class Support:
    def __init__(self, node, support_type, rotation):
        self.coordinate = node.coordinate
        self.type = support_type
        self.rotation = rotation
        self.node = node

    def __str__(self):
        return f"{self.type} Support at {self.coordinate} with rotation of {self.rotation}"
