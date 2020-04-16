
"""
Generates two sets of ten random numbers in range from 1 to 100. If the same number is in both sets it prints it out
"""
import random

a = random.sample (range (1, 101), 10)
b = random.sample (range (1, 101), 10)

c = [x for x in a if x in b if x]

print (c)


