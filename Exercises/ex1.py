"""
Takes three inputs. Your name, your age and 'z' intenger and prints out your name and age z times
"""
x = input ("What is your first name: ")
y = input ("What is your age: ")
z = int (input ("How many times do you want to print the message?: "))


m = ("{} is {} years old. \n".format(x, y))

print (z * m)
