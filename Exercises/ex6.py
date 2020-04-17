"""
Takes a list of number and creates a new list of odd number from the original list
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
# for every element in the list a if the remainder of %2 is 0 it adds the element to the list b 
for x in a: 
    if x%2 == 0:
        b.append(x)

print (b)
