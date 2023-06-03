import numpy as np


class Truss:
    def __init__(self, nodes, elements, supports, forces):
        self.nodes = nodes
        self.elements = elements
        self.supports = supports
        self.forces = forces
        self.delta = None

    def get_all_degrees(self):
        all_degrees = []
        for node in self.nodes:
            for degree in node.degrees:
                if not degree in all_degrees:
                    all_degrees.append(degree)

        return all_degrees

    def get_locked_degrees(self):
        degrees = []
        for support in self.supports:
            for degree in support.degrees:
                if not degree in degrees:
                    degrees.append(degree)
        return degrees

    def get_free_degrees(self):
        locked_degrees = self.get_locked_degrees()
        all_degrees = self.get_all_degrees()
        degrees = []

        for degree in all_degrees:
            if not degree in locked_degrees:
                degrees.append(degree)

        return degrees

    def get_forces_vector(self):
        all_degrees = self.get_all_degrees()
        locked_degrees = self.get_locked_degrees()

        forces_vector = np.zeros(len(all_degrees))

        for f in self.forces:
            for degree, value in f.forces.items():
                forces_vector[degree - 1] = forces_vector[degree - 1] + value

        for degree in locked_degrees:
            forces_vector[degree - 1] = None

        return forces_vector

    def get_delta_vector(self):
        all_degrees = self.get_all_degrees()
        free_degrees = self.get_free_degrees()
        locked_degrees = self.get_locked_degrees()

        delta_vector = np.zeros(len(all_degrees))
        for degree in locked_degrees:
            delta_vector[degree - 1] = 0

        for degree in free_degrees:
            delta_vector[degree - 1] = None
        return delta_vector

    def stiffness_matrix(self):
        nodes = self.nodes
        elements = self.elements
        n = len(nodes) * 2
        K = np.zeros((n, n))

        for element in elements:
            degrees = element.degrees
            for i in degrees:
                for j in degrees:
                    i_in_global, j_in_global = i - 1, j - 1
                    l = list(degrees)
                    i_in_local, j_in_local = l.index(i), l.index(j)

                    K[i_in_global, j_in_global] = K[i_in_global, j_in_global] + \
                        element.globalK()[i_in_local, j_in_local]

        return K
