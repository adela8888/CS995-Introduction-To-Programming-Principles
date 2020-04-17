"""
Lottery game that uses a dictionary 
"""
lottery = {1: "£50", 2: "chocolate", 3: "nothing", 4: "win nothing", 6: "£10", 7:"£10000",
           8: "roses", 9: "£10", 10: "a bottle of red wine"}

number = int (input("Choose a number 1 to 10: "))

if number in lottery.keys(): print ("You have won {}".format(lottery.get(number)))


