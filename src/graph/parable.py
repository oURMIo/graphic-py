import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 4000)
y = x**2

plt.plot(x, y, label="y = x^2")

plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
