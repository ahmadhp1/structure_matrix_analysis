from models.truss_model import Truss
from penalty import solve_truss_with_penalty_method
from plotter import plot_truss
from read_json_input import get_elements, get_forces, get_nodes, get_supports
from models.node_model import Node
import numpy as np
import time

input = 'example_1.json'

start_time = time.time()

nodes = get_nodes(input)
elements = get_elements(input, nodes)
supports = get_supports(input, nodes)
forces = get_forces(input, nodes)

truss = Truss(nodes, elements, supports, forces)

result = solve_truss_with_penalty_method(truss)
print(result)

end_time = time.time()


# np.savetxt('output.txt', stiffnessMatrix, fmt="%.3f")
print('time:', end_time - start_time)
print("+++++++++++++++ check output.txt for results +++++++++++++++++")


# plot_truss(elements, supports, nodes)
