# Create a 2 D NumPy array with the sahpe(3, 4) containing random integers between 1 and 100.
# Find the minimun and maximum values in the entire array. Tound each element to the neareast integer.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4))

min_value = np.min(arr)
max_value = np.max(arr)

print(f"Minimun is = {min_value}, maximum is = {max_value} The array rounded = {np.round(arr)}")