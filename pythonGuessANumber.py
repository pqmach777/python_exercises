# #Step 1 & 2
# the_Number = 3
# guessed = False
# def guessed_Number(x):
#     guessed = x
#     while guessed==False:
#         try:
#             userInput = int(input("What is the number?(Guess from 1 to 10) "))
#         except ValueError:
#             print("Please enter a number!")
#             continue
#         if userInput==the_Number:
#             guessed = True
#             print("Well done!")
#         elif userInput>10:
#             print("Our guess range is between 0 and 10, please try a bit lower")
#         elif userInput<0:
#             print("Our guess range is between 0 and 10, please try a bit higher")
#         elif userInput>the_Number:
#             print("Try one more time, a bit lower")
#         elif userInput < the_Number:
#             print("Try one more time, a bit higher")
# guessed_Number(guessed)

# #Step 3 
# import random
# random_number = random.randint(1,10)
# guessed = False
# def guessed_Number(x):
#     guessed = x
#     while guessed==False:
#         try:
#             userInput = int(input("What is the number?(Guess from 1 to 10) "))
#         except ValueError:
#             print("Please enter a number!")
#             continue
#         if userInput==random_number:
#             guessed = True
#             print("Well done!")
#             break
#         elif userInput>10:
#             print("Our guess range is between 0 and 10, please try a bit lower")
#         elif userInput<0:
#             print("Our guess range is between 0 and 10, please try a bit higher")
#         elif userInput>random_number:
#             print("Try one more time, a bit lower")
#         elif userInput < random_number:
#             print("Try one more time, a bit higher")
# guessed_Number(guessed)

# #Step 4 Limit Number of Guess

# import random
# guessed = True
# def guessed_Number(x):
#     random_number = random.randint(1,10)
#     limit = []
#     limit2 = len(limit)
#     guessed = x
#     while True:
#         try:
#             userInput = int(input("What is the number?(Guess from 1 to 10) "))
#         except ValueError:
#             print("Please enter a number!")
#             continue
#         if limit2 < 5:
#             limit2 = limit2 +1
#             print("You have ",(5-limit2),"guesses left.")
#             if limit2 == 5:
#                 print("You ran out of guesses. GG")
#                 break
#             elif userInput==random_number:
#                 guessed = True
#                 print("Well done!")
#                 break
#             elif userInput>10:
#                 print("Our guess range is between 0 and 10, please try a bit lower")
#                 continue
#             elif userInput<0:
#                 print("Our guess range is between 0 and 10, please try a bit higher")
#                 continue
#             elif userInput>random_number:
#                 limit.apped(1)
#                 print("Try one more time, a bit lower")
#                 continue
#             elif userInput < random_number:
#                 limit.append(1)
#                 print("Try one more time, a bit higher")
#                 continue
# guessed_Number(guessed)
      
