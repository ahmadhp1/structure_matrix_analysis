import math
import numpy as np


def _get_penalty_stiffness_matrix(truss):
    new_stiffness_matrix = truss.stiffness_matrix()
    supports = truss.supports

    diagonal = np.diagonal(new_stiffness_matrix)
    largest_k = np.amax(diagonal)
    p = largest_k * 10e5

    for support in supports:
        for degree in support.degrees:
            new_stiffness_matrix[degree - 1, degree - 1] = p

    return new_stiffness_matrix


def solve_truss_with_penalty_method(truss):
    Kp = _get_penalty_stiffness_matrix(truss)
    forces = truss.get_forces_vector()
    p_forces = [0 if math.isnan(x) else round(x, 10) for x in forces]
    delta = np.linalg.inv(Kp) @ p_forces

    return delta
