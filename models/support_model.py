from models.coordinate_model import Coordinate


class Support:
    def __init__(self, node, support_type, rotation):
        self.coordinate = node.coordinate
        self.type = support_type
        self.rotation = rotation  # from X counterClockWise
        self.node = node

        node_number = node.number
        is_horizontal = self.rotation == 0 or self.rotation == 180
        is_vertical = self.rotation == 90 or self.rotation == 270

        if not (is_horizontal or is_vertical):
            print('********* not supported support ***********')

        degrees = []

        if self.type == 'pin':
            degrees.append(node_number * 2 - 1)
            degrees.append(node_number * 2)

        elif self.type == 'roller':
            if is_horizontal:
                degrees.append(node_number * 2 - 1)
            elif is_vertical:
                degrees.append(node_number * 2)

        self.degrees = degrees

    def __str__(self):
        return f"{self.type} Support at {self.coordinate} with rotation of {self.rotation}"
