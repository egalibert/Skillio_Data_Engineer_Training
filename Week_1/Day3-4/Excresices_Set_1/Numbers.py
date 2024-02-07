import numpy as np
import math
from statistics import mode

numbers = input("Give numbers separated by commas (1,2,3): ")
# numbers = "1,3,4,6"

numbers_list = numbers.split(",")

array_mean = np.mean(numbers_list)
array_median = np.median(numbers_list)

print(numbers_list)

print(f"The minimum value of given numbers is {min(numbers_list)} and maximun is {max(numbers_list)}")
print(f"The mean value is {array_mean}, median is {array_median}, mode is {mode(numbers_list)}")