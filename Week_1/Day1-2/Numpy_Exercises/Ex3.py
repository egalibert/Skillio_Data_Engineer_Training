# Generate an array of 25 random integers between -100 and 100 using the numpy random module.
# Calculate the mean of the array.

import numpy as np

arr = []
for i in range(25):
	random_int = np.random.randint(-100, 100)
	arr.append(random_int)

print(arr)
print(f"The mean of the array is {np.mean(arr)}")