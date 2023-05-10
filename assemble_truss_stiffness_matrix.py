import numpy as np


def assembleGlobalStiffnessMatrix(nodes, elements):
    n = len(nodes) * 2
    K = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            print('hello')

    return K
