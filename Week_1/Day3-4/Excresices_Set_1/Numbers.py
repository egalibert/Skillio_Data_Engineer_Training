import numpy as np
import math

numbers = input("Give numbers separated by commas (1,2,3)")
# numbers = "1,3,4,6"

numbers_list = numbers.split(",")
print(numbers_list)

print(f"The minimum value of given numbers is {min(numbers_list)} and maximun is {max(numbers_list)}")
print(f"The mean value is {np.mean(numbers_list)}, median is {np.median(numbers_list)}")