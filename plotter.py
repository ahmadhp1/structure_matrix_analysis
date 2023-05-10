import matplotlib.pyplot as plt


def plot_truss(elements, supports, nodes):
    fig, ax = plt.subplots()

    for element in elements:
        x_points = [element.eCoordinate.x, element.bCoordinate.x]
        y_points = [element.eCoordinate.y, element.bCoordinate.y]
        ax.plot(x_points, y_points, 'b')

    for support in supports:
        x = support.coordinate.x
        y = support.coordinate.y
        if support.type == 'pin':
            ax.plot(x, y, 'ro')
        elif support.type == 'roller':
            ax.plot(x, y, 'yo')

    for node in nodes:
        ax.annotate(node.number, (node.coordinate.x, node.coordinate.y))

    plt.show()
