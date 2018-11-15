# myShoppingList = ["apples", "kale", "ginger", "spinach"]

# myShoppingList[0]
# #apples
# myShoppingList[1]
# #kale
# myShoppingList[2]
# #ginger
# myShoppingList[3]
# #spinach
# len(myShoppingList)
# print(myShoppingList[0])
# l = len(myShoppingList)
# print(l)
# print(myShoppingList[3])

# myShoppingList.append("oranges")
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)
# print(myShoppingList)

#splicing
# numbers = [1, 2, 3, 4, 5]

# print(numbers[3:5])
# numberSubset = numbers[3:5]
# print(len(numberSubset))

# numbers = [1, 2, 3, 4, 5]
# pv = numbers.pop()
# numbers.insert(1, 56)
# print(numbers)
# numbers.extend([6, 7, 8, 'anuj'])
# print(numbers)
# print(numbers)
# print(pv)
# print(numbers[1])
# print(numbers.index(4))

#len strings
# myName = "Anuj"
# print(len(myName))
# sentence = "this is a wonderful life"
# print(sentence.index(' '))
# numbers1 = [22, 2, 3, 13, 5, 1]
# numbers2 = [-1, -2, -3]
# print(numbers1 + numbers2)

#Tuple
# myTuple = (1, 3, 5)
# print(myTuple[0])
# myTuple = [1, "Sandhya", "Ram"]
# myTuple[0] = "hello Anuj"
# print(myTuple)

#range is a function that indicate how many times the loo will be repeated.
# myRange = range(1, 10, 20)
# print(myRange)
# for index in range(1, 10):
#     print("hello world")
# for index in range(1, 11):
#     print(index)
# for index in range(1, 11, 2):
#     print(index)

#For loop nested
# for index in range(10):
#     print("Index", index)
#     for innerIndex in range(10):
#         print("Inner Index", innerIndex)
for index in range(1, 11):
    # print("Index", index)
    for innerIndex in range(1, 11):
        print(index, " x ", innerIndex, " = ", index * innerIndex)


# Hokage = ['Anuj', 'The', 'Caste']
# print(Hokage)
# for name in Hokage:
#     # print(Hokage.index(name))
#     print(Hokage.pop())
# print("my list length", len(Hokage))
# print(Hokage)

# for index in range(1, 11, 2):
#     # print("Index", index)
#     for innerIndex in range(1, 11, 3):
#         print(index, " x ", innerIndex, " = ", index * innerIndex)


# l1 = [1,5,3,6,7]
# l2 = [3,6,9,10,2]
# l3 = []
# for num1 in l1:
#     total = 0
#     for num2 in l2:
#         total += num1 * num2
#     l3.append(total)
# print(l3)        


