a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
z = int (input("Enter random number:"))

b = []
for x in a:
    if x < z and x not in b:
        b.append(x)

print (b)
