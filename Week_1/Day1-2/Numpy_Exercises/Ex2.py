# Create a 1D NumPy array with 15 random floats between 1 and 10.
# Calculate the median and round each float to the nearest integer.

import numpy as np

arr = []
random_floats = np.random.uniform(1, 10, 15)
arr = np.array(random_floats)

print(arr)
print(f"The median is {np.median(arr)} and the array rounded is {np.round(arr)}")