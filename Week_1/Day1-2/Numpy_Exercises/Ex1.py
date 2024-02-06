#Create a 1D array with 12 random integers between 5 and 50. Find the minimum and maximum values.

import numpy as np
arr = []

for i in range(0, 12):
	random_int = np.random.randint(5, 50)
	arr.append(random_int)

print(arr)
print(f"Maximum value is {np.max(arr)}, Minimum value is {np.min(arr)}")