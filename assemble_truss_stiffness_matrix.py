import numpy as np


def assembleGlobalStiffnessMatrix(nodes, elements):
    n = len(nodes) * 2
    K = np.zeros((n, n))

    for element in elements:
        degrees = element.degrees
        for i in degrees:
            for j in degrees:
                i_in_global = i - 1
                j_in_global = j - 1

                i_in_local = list(degrees).index(i)
                j_in_local = list(degrees).index(j)
                # print(element.id, element.degrees, i, j,  i_in_global,
                #   j_in_global, i_in_local, j_in_local)
                K[i_in_global, j_in_global] = K[i_in_global, j_in_global] + \
                    element.globalK()[i_in_local, j_in_local]

    return K
