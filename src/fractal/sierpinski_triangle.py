import matplotlib.pyplot as plt
import numpy as np


def sierpinski_triangle(order, vertices):
    if order == 0:
        plt.fill(vertices[:, 0], vertices[:, 1], "b")
    else:
        midpoints = [(vertices[i] + vertices[(i + 1) % 3]) / 2 for i in range(3)]
        midpoints = np.array(midpoints)

        sierpinski_triangle(
            order - 1, np.array([vertices[0], midpoints[0], midpoints[2]])
        )
        sierpinski_triangle(
            order - 1, np.array([vertices[1], midpoints[0], midpoints[1]])
        )
        sierpinski_triangle(
            order - 1, np.array([vertices[2], midpoints[1], midpoints[2]])
        )


def plot_sierpinski_triangle(order):
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])

    plt.figure(figsize=(8, 8))
    sierpinski_triangle(order, vertices)
    plt.title(f"Sierpinski Triangle - Order {order}")
    plt.axis("equal")
    plt.axis("off")
    plt.show()


plot_sierpinski_triangle(8)
