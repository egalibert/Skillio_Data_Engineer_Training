# Generate a 3x3 NumPy array with random integers between 1 and 100 using both numpy.random
# and numpy.array()

import numpy as np

arr = np.array([np.random.randint(1, 100, 3), np.random.randint(1, 100, 3), np.random.randint(1, 100, 3)])

print(arr)