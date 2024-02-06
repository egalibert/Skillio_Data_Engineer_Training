# Use the numpy.array() function to create a 2D array with two lists: [3.14, 2.718, 1.414]
# and [5.55, 6.66, 7.77]. Use numpy.floor() to round down.

import numpy as np

arr = np.array([[3.14, 2.718, 1.414], [5.55, 6.66, 7.77]])
print(arr)
print(np.floor(arr))