from assemble_truss_stiffness_matrix import assembleGlobalStiffnessMatrix
from models.truss_element_model import get_degrees_of_truss_element
from plotter import plot_truss
from read_json_input import get_elements, get_nodes, get_supports
from models.node_model import Node
import numpy as np

nodes = get_nodes('input.json')
elements = get_elements('input.json', nodes)
supports = get_supports('input.json', nodes)


stiffnessMatrix = assembleGlobalStiffnessMatrix(nodes, elements)
print(stiffnessMatrix)


# # plot_truss(elements, supports, nodes)
