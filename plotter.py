import math
from matplotlib import patches
import matplotlib.pyplot as plt
import numpy as np
from models.coordinate_model import Coordinate

from models.node_model import Node


def plot_truss(truss, elements_with_delta):
    fig, ax = plt.subplots()
    elements = truss.elements
    supports = truss.supports
    nodes = truss.nodes
    forces = truss.forces
    delta = truss.delta

    for element in elements:
        x_points = [element.eCoordinate.x, element.bCoordinate.x]
        y_points = [element.eCoordinate.y, element.bCoordinate.y]
        ax.plot(x_points, y_points, 'b')

    for support in supports:
        x = support.coordinate.x
        y = support.coordinate.y
        if support.type == 'pin':
            ax.plot(x, y, 'ro')
        elif support.type == 'roller':
            ax.plot(x, y, 'yo')

    for node in nodes:
        ax.annotate(node.number, (node.coordinate.x, node.coordinate.y))

    for force in forces:
        if math.isnan(force.value):
            continue

        length = .5
        x = force.node.coordinate.x
        y = force.node.coordinate.y

        arrow = patches.Arrow(x, y, length *
                              np.cos(force.angle), length * np.sin(force.angle), width=.1)
        ax.add_patch(arrow)
        ax.annotate(force.value, (x, y - .3))

        for element in elements_with_delta:
            e_delta = element.delta
            for index, delta in enumerate(e_delta):
                e_delta[index] = delta * 10

            x_points = [element.eCoordinate.x + e_delta[2],
                        element.bCoordinate.x + e_delta[0]]
            y_points = [element.eCoordinate.y + e_delta[3],
                        element.bCoordinate.y + e_delta[1]]

            ax.plot(x_points, y_points, '--')

    plt.show()
