import numpy as np
import matplotlib.pyplot as plt


def julia(c, width, height, iterations):
    x = np.linspace(-2.0, 2.0, width)
    y = np.linspace(-2.0, 2.0, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = np.zeros(Z.shape, dtype=int)

    mask = np.ones(Z.shape, dtype=bool)

    for i in range(iterations):
        Z[mask] = Z[mask] ** 2 + c
        mask = np.abs(Z) <= 2
        C += mask

    plt.imshow(C, cmap="inferno", extent=(-2.0, 2.0, -2.0, 2.0))
    plt.colorbar()
    plt.title("Julia Set")
    plt.show()


julia(complex(-0.7, 0.27015), 1600, 1600, 300)
