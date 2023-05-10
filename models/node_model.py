from models.coordinate_model import Coordinate


class Node:
    def __init__(self, number, coordinate):
        self.number = number
        self.coordinate = coordinate

    def __str__(self):
        return f"node at {self.coordinate}"
