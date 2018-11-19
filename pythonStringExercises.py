# 1. Uppercase a String 
# string = "hi, i am phong!"
# print (string.upper())

# 2. Capitalize a String
# string = "anuj is hokage"
# print (string.title())

# 3. Reverse a String
# string = "kcire si juna"
# def reverse(string)
#     return(string[::-1])
# print(reverse(string))

# 4. Leetspeak
#A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7

# string = input("Input String: ")
# string = string.replace("A","4")
# string = string.replace("E","3")
# string = string.replace("G","6")
# string = string.replace("I","1")
# string = string.replace("O","0")
# string = string.replace("S","5")
# string = string.replace("T","7")
# print(string)

# 5. Long-long vowels
#Good => Goooood Cheese => Cheeeeese Man => Man Spoon => Spooooon

# string = input("Your Word: ")
# long_vowels = ["oo","ee"]

# string_result = " "
# for x in range(len(string)):
#     dup_letters = string[x:x+2]
#     if dup_letters in long_vowels:
#         string_result += string[x]*4
#     else:
#         string_result += string[x]
# print(string_result)

# string = string.replace("oo","ooooo")
# string = string.replace("ee","eeeee")
# print(string)

# 6. Caesar Cipher

# cipher_string = "lbh zhfg hayrnea jung lbh unir yrnearq"
# offset = 13
# decipher = ""
# offset = 13
            
# for char in cipher_string:
#     code = ord(char)
#     if code >= 97 and code <= 122:
#         dcipher_char = code + offset
#         if dcipher_char >= 122:
#             new_character = chr(dcipher_char - 26)
#         else:
#             new_character = chr(dcipher_char)
#     else:
#         new_character = chr(code)
#     decipher += new_character
# print(decipher)
