# # 1. Hello
# def saysHello(name):
#     if not name: 
#         print("Hello everyone!")
#     else:
#         print("Hello "+name)

# saysHello("")
# saysHello("Phong")


# # 2. y = x + 1
# import matplotlib.pyplot as plot 

# def f(x):
#     y = x + 1
#     return y


# xs = list(range(-3, 4)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

# # 3. Square of x
# import matplotlib.pyplot as plot
# def f(x):
#     y=x**2+2*x+2
#     return y

# xs = list(range(-100,100))
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs, ys)
# plot.show()

# # 4. Odd or Even
# import matplotlib.pyplot as plot
# def f(x):
#     if x % 2 == 0:
#         y = -1
#     elif x % 2 != 0:
#         y = 1
#     return y
    
# xs = list(range(-5, 5))
# ys = []

# for x in xs:
#     ys.append(f(x))
# plot.bar(xs, ys)
# plot.show()

# # 5. Sine
# import matplotlib.pyplot as plot
# import math

# def f(x):
#     y= math.sin(x)
#     return y
# xs = list(range(-5,5))
# ys = []

# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)
# plot.show()

# # 6. Sine 2
# import matplotlib.pyplot as plot
# import math
# from numpy import arange

# def f(x):
#     y=math.sin(x)
#     return y
# xs = arange(-5,5,0.1)
# ys = []

# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)
# plot.show()


# # 7. Degree Conversion
# import matplotlib.pyplot as plot
# import math
# from numpy import arange
# def convertTemp(Celsius):
#     Fahrenheit = (Celsius * 1.8) +32
#     return Fahrenheit
# xs = arange(0, 5,0.1)
# ys = [] 

# for Celsius in xs: 
#      ys.append(convertTemp(Celsius)) 

# plot.plot(xs, ys) 
# plot.show()

# # 8. Play again?
# def wantPlay(x):
#     if x == "Y":
#         return True
#     elif x == "N":
#         return False
#     elif x != ["Y","N"] :
#         return("Please type Y or N!")
# play = str.upper(input("Do you want to play? (type Y or N) "))
# print(wantPlay(play))

# # 9. Play again? Again.
# play = str.upper(input("Do you want to play? (type Y or N) "))
# def wantPlay(x):
#     y = "Y"
#     n = "N"
#     while True:
#         if x == y:
#             return True
#         elif x == n:
#             return False
#         elif x != [y,n]:
#             print("Invalid Input")
#             play = input("Do you want to play? (type Y or N) ")
#             if play == y:
#                 return True
#             if play == n:
#                 return False
# print(wantPlay(play))
