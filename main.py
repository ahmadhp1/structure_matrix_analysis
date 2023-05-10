from assemble_truss_stiffness_matrix import assembleGlobalStiffnessMatrix
from plotter import plot_truss
from read_json_input import get_elements, get_nodes, get_supports
from models.node_model import Node
import numpy as np

input = 'input1.json'

nodes = get_nodes(input)
elements = get_elements(input, nodes)
supports = get_supports(input, nodes)


stiffnessMatrix = assembleGlobalStiffnessMatrix(nodes, elements)
np.savetxt('output.txt', stiffnessMatrix, fmt="%.3f")


plot_truss(elements, supports, nodes)
