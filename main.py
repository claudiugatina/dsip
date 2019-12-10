import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.linspace(0,255,255), np.linspace(0,255,255))
z = x * y

for i in range(0, 255):
    z[155][i] = 0

# Plot the grid
plt.imshow(z)
plt.gray()
plt.show()