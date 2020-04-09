x = {1: "John", 2: "Peter", 3: "Chris", 4: "Tom"}
b = int(input("Choose a number and we will choose you a man:"))

if b in x.keys(): print ("Your man is {}".format(x.get(b)))