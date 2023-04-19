import json
from models.support_model import Support
from models.truss_element_model import TrussElement


def _read_file(input_path):
    with open(input_path) as input:
        input_data = json.load(input)
        return input_data


def get_elements(input_path):
    data = _read_file(input_path)
    elements = _find_elements_from_json(data)
    return elements


def get_supports(input_path):
    data = _read_file(input_path)
    supports = _final_supports_from_json(data)
    return supports


def _final_supports_from_json(data):
    supports = []

    for support in data['supports']:
        x = support['x']
        y = support['y']
        support_type = support['type']
        rotation = support['rotation']

        s = Support(x, y, support_type, rotation)
        supports.append(s)

    return supports


def _find_elements_from_json(data):
    elements = []

    for element in data['elements']:
        id = element['id']
        start_x = element['start_x']
        start_y = element['start_y']
        end_x = element['end_x']
        end_y = element['end_y']
        A = element['A']
        E = element['E']

        e = TrussElement(id, start_x, start_y, end_x, end_y, A, E)
        elements.append(e)

    return elements
