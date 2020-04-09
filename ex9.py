import random

a = random.sample (range (1, 101), 10)
b = random.sample (range (1, 101), 10)

c = [x for x in a if x in b if x]

print (c)



"""
HOW TO GENERATE A GIVEN NUMBER OF RANDOM NUMBERS

A = RANDOM.SAMPLE (RANGE(1, 101), 10)
"""