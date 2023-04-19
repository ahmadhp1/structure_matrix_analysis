import math
import numpy as np

from models.coordinate_model import Coordinate


class TrussElement:
    def __init__(self, id, start_x, start_y, end_x, end_y, A, E):
        self.id = id
        self.bCoordinate = Coordinate(start_x, start_y)
        self.eCoordinate = Coordinate(end_x, end_y)
        self.A = A
        self.E = E

        self.delta = None
        self.forces = None

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

    def __str__(self):
        return f"start at {self.bCoordinate} | ends at {self.eCoordinate} | area : {self.A}"
