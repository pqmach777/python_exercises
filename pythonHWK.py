# 1. Hello, you!
# name = input("What's your name? ")
# print("Hello, " + name + "!")

# 2. HELLO, YOU!
# name = input("WHAT IS YOUR NAME? ")

# print("HELLO, " + name.upper() + "!")
# print("YOUR NAME HAS " + str(len(name)) + "! AWESOME!")

#3 Madlib
# print("Please fill in the blanks below:")
# print("___(name)____'s favorite sport of all time is ___(sport)___.")
# name = input("What is name? ")
# sport = input("What is sport? ")
# print(name + "'s favorite sport of all time is "+ sport +".")

# 4 Day of the Week
# day = int(input('Day (0-6)? (Please choose a number from 1 to 6)'))
# if(day == 0):
#     print("Sunday")
# elif(day == 1):
#     print("Monday")
# elif(day == 2):
#     print("Tuesday")
# elif(day == 3):
#     print("Wednsday")
# elif(day == 4):
#     print("Thursday")
# elif(day == 5):
#     print("Friday")    
# elif(day == 6):
#     print("Saturday")
# else:
#     print("Please enter number from 1 to 6!")

# 5 Work or Sleep In?
# day = int(input('Day (0-6)? '))
# while True:
#     if(day == 0):
#         print("Sleep In!")
#     elif(day == 1):
#         print("Work Day!")
#     elif(day == 2):
#         print("Work Day!")
#     elif(day == 3):
#         print("Work Day!")
#     elif(day == 4):
#         print("Work Day!")
#     elif(day == 5):
#         print("Work Day!")    
#     elif(day == 6):
#         print("Sleep In!")
#     else:
#         print("Please try again!")
#     break

#6 Celsius to Fahrenheit
Celsius = int(input("Temperature in C? "))
Fahrenheit = (Celsius * 1.8) +32
print(Fahrenheit, " F")


#7 Tip Calculator
# totalBill = int(input("Total bill amount? "))
# levelService = input('Level of service? (good, fair, or bad) ')
# if(levelService == 'good'):
#     tip = totalBill * .20
# elif(levelService == 'fair'):
#     tip = totalBill * .15 
# elif(levelService == 'bad'):
#     tip = totalBill * .10
# print("Total Tip: ${:.2f}" .format(tip)) 
# totalAmount = totalBill + tip
# print ("Total Amount: ${:.2f}" .format(totalAmount))

#8 Tip Calculator 2
# totalBill = int(input("Total bill amount? "))
# levelService = input('Level of service? (good, fair, or bad) ')
# if(levelService == 'good'):
#     tip = totalBill * .20
# elif(levelService == 'fair'):
#     tip = totalBill * .15 
# elif(levelService == 'bad'):
#     tip = totalBill * .10
# split = int(input("Split how many ways? "))
# print("Total Tip: ${:.2f}" .format(tip)) 
# totalAmount = totalBill + tip
# print("Total Amount: ${:.2f}" .format(totalAmount))
# splitTotal = totalAmount/split
# print("Amount per person: ${:.2f}" .format(splitTotal)) 

#9 1 to 10
# count = 0
# while count < 10:
#   count += 1
#   print(count)

#10 How many coins
# coinsCount = 0
# print("You have {} coins.".format(coinsCount))
# while True:
#     coinsQuestion = input("Do you want another? (yes or no)")
#     if coinsQuestion == 'yes':
#         coinsCount += 1
#         print("You have {} coins.".format(coinsCount))
#     elif coinsQuestion == 'no':
#         print("Bye")
#         break
#     else:
#         print("Please type yes or no!")