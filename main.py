import matplotlib.pyplot as plt
import numpy as np
import matrixfiller

z = [[3, 3, 15], [1, 2, 171], [2, 1, 90], [-2, 2, 255]]

z = matrixfiller.matrix_from_array(z, 50, 50)

# Plot the grid
plt.imshow(z)
# plt.gray()
plt.show()
