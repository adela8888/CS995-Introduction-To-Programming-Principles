"""
Takes a word and let's you know if it is same from start to end and the other way around
"""
x = input("Enter word: ")
x = str (x)
y = x [::-1]

if x == y: print ("The word " + x + " is read the same from start to end end the other way around")
else: print ("Not the same from the end to the start")
