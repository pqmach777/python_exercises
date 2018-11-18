# 1. 1 to 10
# for count in range(1,11):
#     print(count)

# 2. n to m
# count_start = int(input("Input your starting number: "))
# count_end = int(input("Input your ending number: "))
# for count in range(count_start, count_end):
#     print(count)

# 3. Odd Numbers 
# for oddNumbers in range(1, 11):
#     if oddNumbers % 2 != 0:
#         print(oddNumbers)

# 4. Print a Square
# star = 5
# inner_star = star
# for i in range(inner_star):
#     print(inner_star * "*")
# 
# 5. Print a Square 2
# star = 10
# inner_star = star
# for i in range(inner_star):
#     print(inner_star* "*")

# 6. Print a box
# width, height = 6, 4
# for w in range(width):
#     for h in range(height):
#        print('*' if w in [0, height+1] or h in [0, width-3] else ' ', end=" ")
#     print()

# 7. Print a Triangle
# t = 4
# for a in range(1,t+1): 
#     for b in range(t-a):
#         print(" ",end='')
#     for b in range(1,a):
#         print("*",end='')
#     for c in range(a,0,-1):
#         print("*",end='')
#     print()

# 8. Print a Triangle 2
# t = int(input("Please give the height of the Triangle in numbers: "))
# for a in range(1,t+1): 
#     for b in range(t-a):
#         print(" ",end='')
#     for b in range(1,a):
#         print("*",end='')
#     for c in range(a,0,-1):
#         print("*",end='')
#     print()

# 9. Multiplication Table
# for i in range(1,11):
#     for j in range(1,11):
#         print(j,'x',i,'=',j*i)
