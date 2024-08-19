import matplotlib.pyplot as plt
import numpy as np


def dragon_curve(order):
    points = np.array([[0, 0], [1, 0]])

    for i in range(order):
        new_points = []
        for j in range(len(points) - 1):
            start = points[j]
            end = points[j + 1]
            mid = (start + end) / 2
            vec = (end - start) / 2
            perp_vec = np.array([-vec[1], vec[0]])
            if j % 2 == 0:
                new_point = mid + perp_vec
            else:
                new_point = mid - perp_vec
            new_points.append(start)
            new_points.append(new_point)
        new_points.append(end)
        points = np.array(new_points)

    return points


def plot_dragon_curve(order):
    points = dragon_curve(order)

    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], color="#7800ff")
    plt.title(f"Dragon Curve - Order {order}")
    plt.axis("equal")
    plt.axis("off")
    plt.show()


plot_dragon_curve(15)
