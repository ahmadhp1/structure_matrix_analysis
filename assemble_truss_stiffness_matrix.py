import numpy as np


def assembleGlobalStiffnessMatrix(nodes, elements):
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
