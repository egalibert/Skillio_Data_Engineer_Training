# Create a 1D array with random floats between -5 and 5. 
# Calculate the mean of the array and roound each float to two decimal places.

import numpy as np

arr = -5 + 10 * np.random.random(size=10)

# for i in range(10):
	# random_float = np.random.random()
	# arr.append(random_float)

print(arr)
print(f"The mean of the array is {np.mean(arr)}")