import numpy as np
import argparse
from statistics import mode

parser = argparse.ArgumentParser()
parser.add_argument('numbers', type=int, nargs='+')
args = parser.parse_args()

numbers_list = []

# print(args)
for item in args.numbers:
	numbers_list.append(item)

print(numbers_list)

print(sum(numbers_list))
print(f"The minimum value of given numbers is {min(numbers_list)} and maximun is {max(numbers_list)}")
print(f"The mean value is {np.mean(numbers_list)}, median is {np.median(numbers_list)} mode is = {mode(numbers_list)}")