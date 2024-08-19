import matplotlib.pyplot as plt
import numpy as np


def koch_curve(order, start, end):
    if order == 0:
        return np.array([start, end])

    vec = (end - start) / 3.0
    p1 = start + vec
    p2 = start + 2 * vec

    angle = np.pi / 3
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    peak = p1 + np.dot(rotation_matrix, vec)

    points1 = koch_curve(order - 1, start, p1)
    points2 = koch_curve(order - 1, p1, peak)
    points3 = koch_curve(order - 1, peak, p2)
    points4 = koch_curve(order - 1, p2, end)

    return np.vstack([points1[:-1], points2[:-1], points3[:-1], points4])


def plot_koch_curve(order):
    start = np.array([0, 0])
    end = np.array([1, 0])
    points = koch_curve(order, start, end)

    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], color="#7800ff")
    plt.title(f"Koch Curve - Order {order}")
    plt.axis("equal")
    plt.axis("off")
    plt.show()


plot_koch_curve(8)
