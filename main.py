from assemble_truss_stiffness_matrix import assembleGlobalStiffnessMatrix
from plotter import plot_truss
from read_json_input import get_elements, get_nodes, get_supports
from models.node_model import Node
import numpy as np
import time

input = 'example_2.json'

start_time = time.time()

nodes = get_nodes(input)
elements = get_elements(input, nodes)
supports = get_supports(input, nodes)


stiffnessMatrix = assembleGlobalStiffnessMatrix(nodes, elements)

end_time = time.time()

np.savetxt('output.txt', stiffnessMatrix, fmt="%.3f")
print('time:', end_time - start_time)
print("+++++++++++++++ check output.txt for results +++++++++++++++++")


plot_truss(elements, supports, nodes)
