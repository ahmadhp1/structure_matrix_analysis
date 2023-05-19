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
    Pp = np.nan_to_num(forces)
    print('Pp', Pp)

    delta = np.transpose(Kp) @ Pp

    print('delta', delta)
