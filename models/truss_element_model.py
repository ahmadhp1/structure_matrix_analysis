import math
import numpy as np

from models.coordinate_model import Coordinate


class TrussElement:
    def __init__(self, id, start_node, end_node, A, E):
        self.id = id
        self.bCoordinate = start_node.coordinate
        self.eCoordinate = end_node.coordinate
        self.A = A
        self.E = E

        self.delta = None
        self.forces = None

        self.start_node = start_node
        self.end_node = end_node

        start_node_number = start_node.number
        end_node_number = end_node.number

        self.degrees = [
            (start_node_number * 2) - 1, (start_node_number * 2),
            (end_node_number * 2) - 1, (end_node_number * 2),
        ]

    def _dx_dy(self):
        dx = self.eCoordinate.x - self.bCoordinate.x
        dy = self.eCoordinate.y - self.bCoordinate.y
        return dx, dy

    def length(self):
        dx, dy = self._dx_dy()
        return math.sqrt(dx**2 + dy**2)

    def _sin_cos(self):
        L = self.length()
        dx, dy = self._dx_dy()
        cos = dx / L
        sin = dy / L
        return sin, cos

    def T(self):
        sin, cos = self._sin_cos()
        T = np.array([[cos, sin, 0, 0],
                      [-sin, cos, 0, 0],
                      [0, 0, cos, sin],
                      [0, 0, -sin, cos]],
                     )
        return T

    def localK(self):
        S = (self.E * self.A) / self.length()
        k = np.array([[S, 0, -S, 0],
                      [0, 0, 0, 0],
                      [-S, 0, S, 0],
                      [0, 0, 0, 0]])
        return k

    def globalK(self):
        return self.T().T @ self.localK() @ self.T()

    def __str__(self):
        return f"start at {self.bCoordinate} | ends at {self.eCoordinate} | area : {self.A}"
