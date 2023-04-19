from models.coordinate_model import Coordinate


class Support:
    def __init__(self, x, y, support_type, rotation):
        self.coordinate = Coordinate(x, y)
        self.type = support_type
        self.rotation = rotation

    def __str__(self):
        return f"{self.type} Support at {self.coordinate} with rotation of {self.rotation}"
