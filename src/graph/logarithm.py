import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 400)

y = np.log2(x)

plt.plot(x, y, label="y = x^2")

plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
