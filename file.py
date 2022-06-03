import random
Cguess = random.randint(1, 6)
Hguess = 0
while 1>0:
    Hguess = int(input("Guess a Number (1-6): "))
    if Cguess == Hguess:
        print ("You guessed correctly!", end=' ')
        break
    elif Hguess < Cguess:
        print ("Your guess is a lesser", end=' ')
    else:
        print ("Your guess is a greater", end=' ')