"""
Prints out all dividers of the number you enter that gives the remainder of 0
"""
x = int(input("Enter a number: "))

i = 1

while True:
    if x%i == 0:
        print (i)
    i +=1

