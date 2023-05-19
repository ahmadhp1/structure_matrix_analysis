import json
from models.coordinate_model import Coordinate
from models.force_model import Force
from models.support_model import Support
from models.truss_element_model import TrussElement
from models.node_model import Node


def _read_file(input_path):
    with open(input_path) as input:
        input_data = json.load(input)
        return input_data


def get_nodes(input_path):
    data = _read_file(input_path)
    elements = _find_node_from_json(data)
    return elements


def get_elements(input_path, nodes):
    data = _read_file(input_path)
    elements = _find_elements_from_json(data, nodes)
    return elements


def get_supports(input_path, nodes):
    data = _read_file(input_path)
    supports = _find_supports_from_json(data, nodes)
    return supports


def get_forces(input_path, nodes):
    data = _read_file(input_path)
    forces = _find_forces_from_json(data, nodes)
    return forces


def _find_forces_from_json(data, nodes):
    forces = []

    for force in data['forces']:
        node_id = force['node']
        value = force['value']
        rotation = force['rotation']

        _node = None

        for node in nodes:
            if node.number == node_id:
                _node = node
                break

        f = Force(_node, value, rotation)
        forces.append(f)

    return forces


def _find_supports_from_json(data, nodes):
    supports = []

    for support in data['supports']:
        node_id = support['node']
        support_type = support['type']
        rotation = support['rotation']

        _node = None

        for node in nodes:
            if node.number == node_id:
                _node = node
                break

        s = Support(_node, support_type, rotation)
        supports.append(s)

    return supports


def _find_node_from_json(data):
    nodes = []

    for node in data['nodes']:
        id = node['id']
        x = node['x']
        y = node['y']
        e = Node(id, Coordinate(x, y))
        nodes.append(e)

    return nodes


def _find_elements_from_json(data, nodes):
    elements = []

    for element in data['elements']:
        id = element['id']
        start_node_id = element['start_node']
        end_node_id = element['end_node']
        A = element['A']
        E = element['E']

        start_node = None
        end_node = None

        for node in nodes:
            if node.number == start_node_id:
                start_node = node

            if node.number == end_node_id:
                end_node = node

            if not start_node is None and not end_node is None:
                break

        e = TrussElement(id, start_node, end_node, A, E)
        elements.append(e)

    return elements
