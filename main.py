from plotter import plot_truss
from read_json_input import get_elements, get_supports

elements = get_elements('input.json')
supports = get_supports('input.json')

plot_truss(elements, supports)
