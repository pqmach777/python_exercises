#Step 2
guessNumber = int(input("I am thinking of a number between 1 to 10. What's the number? "))
theRange = range(1,10)
theNumber = 3
correct = False
while not correct:
    if guessNumber == theNumber:
        print("Yes! You Win!")
    elif guessNumber > theNumber and theRange:
        print (guessNumber, " is too high!")
    elif guessNumber < theNumber and theRange:
        print (guessNumber, " is oo low!")
    else:
        print ("Please try again with a number from 1 to 10!")
    break