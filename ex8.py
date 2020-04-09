import random

a = random.randint(1, 9)

guess = 0
count = 0

while a != guess:

    if guess == 11:
        break

    guess = int (input("Guess a number. For exit enter 11"))
    count +=1


    if a < guess:
        print ("Your guess is too high")

    elif a > guess:
        print ("Your guess is too low")

    else:
        print ("You guessed right")
        print ("It took you {} tries".format(count))







