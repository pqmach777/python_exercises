# Exercise 1
phonebook_dict = {
 'Alice' : '703-493-1834',
  'Bob' : '857-384-1234',
  'Elizabeth' : '484-584-2923',
}
# 1. Print Elizabeth's phone number 
phone_number = phonebook_dict['Elizabeth']
print(phone_number)
# 2. Add a entry to the dictionary: Kareem's number is 938-489-1234
phonebook_dict['Kareem'] = "938-489-1234"
print(phonebook_dict)
# 3. Delete Alice's phone entry
del phonebook_dict['Alice']
print(phonebook_dict)
# 4. Change Bob's phone number to '968-345-2345'
phonebook_dict['Bob'] = "968-345-2345"
bobNumber = phonebook_dict['Bob']
print(phonebook_dict)
print(bobNumber)
# 5. Print all the phone entries.
phone_entries = phonebook_dict.items()
print(phone_entries)
phone_entries1 = phonebook_dict.keys()
print(phone_entries1)
phone_entries2 = phonebook_dict.values()
print(phone_entries2)

# Exercise 2: Nested Dictionaries
ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}
# 1. Write a python expression that gets the email address of Ramit.
print(ramit['email'])
# 2. Write a python expression that gets the first of Ramit's interests.
print(ramit['interests'][0])
# 3. Write a python expression that gets the email address of Jasmine.
print(ramit['friends'][0]['email'])
# 4. Write a python expression that gets the second of Jan's two interests.
print(ramit['friends'][1]['interests'][1])

# 3. Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example: 
#>>> letter_histogram('banana') 
# {'a': 3, 'b': 1, 'n': 2}

def char_frequency(string):
  dict = {}
  for i in string:
    keys = dict.keys()
    if i in keys:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict
word = input("Letter Histogram: ")
print(char_frequency(word))

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. 
# For example: >>> word_histogram('To be or not to be') 
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

def word_histogram(string):
  sentence = string.lower().split()
  diction = {}
  for w in sentence:
    if w in diction:
      diction[w] += 1
    else:
      diction[w] = 1
  return diction
type_sentence = input("Word Histogram: ")
print(word_histogram(type_sentence))
