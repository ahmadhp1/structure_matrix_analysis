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

delta = solve_truss_with_penalty_method(truss)
truss.delta = delta

elements_with_delta = []
for element in truss.elements:
    elements_with_delta.append(element.apply_delta(delta))

print(elements_with_delta)

print(truss.delta)

end_time = time.time()

print('time:', end_time - start_time)


plot_truss(truss , elements_with_delta)
