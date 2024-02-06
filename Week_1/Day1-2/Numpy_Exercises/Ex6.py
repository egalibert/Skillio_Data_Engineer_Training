# Create a 2D array using numpy.ndarray() with shape(4, 5) and random integers between 10 and 50.
# Calculate the median of the array.

import numpy as np

arr = np.ndarray(shape=(4, 5), dtype=int, buffer=np.random.randint(10, 51, size=(4, 5)))

print(arr)
print(f"The median of the array is {np.median(arr)}")