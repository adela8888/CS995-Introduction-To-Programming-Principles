"""
Prints out a list of odd numbers only from the original list x
"""
x =[1,2,3,4,5,44]
z =[]

for a in x:
    if a % 2 == 0 and a not in z:
        z.append(a)

print (z)
