# # 1. Basics
# class Person: 
#     def __init__(self,name,email,phone): 
#         self.name = name
#         self.email = email
#         self.phone = phone
# # Add an instance variable(attribute)
#         self.friends =[]
#         self.greet_count = 0

# # Add an add_friends method        
#     def add_friends(self,friend):
#         self.friends.append(friend.name)
# # Add a num_friends method
#     def num_friends(self):
#         print(len(self.friends))
# # Add a greet other person method with adding counter   
#     def greet(self,other_person):
#         # Count number of greetings
#         self.greet_count += 1
#         print('Hello {}, I am {}!'.format(other_person.name,self.name))
# # Add a method 2
#     def print_contact_info(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")
# # __str__
#     def __str__(self):
#         return f"{self.name} information: {self.email}, {self.phone}. Number of friends: {len(self.friends)}"
       
# sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
# jordan = Person("Jordan","jordan@aol.com","495-586-3456")
# print(jordan)

## Add a greeting method
# sonny.greet(jordan)
# jordan.greet(sonny)

## Print contact info of sonny
# print(sonny.email,sonny.phone)

## Print statement for jardan contact info
# jordan2 = (f"{jordan.name} {jordan.email} {jordan.phone}")
# print(jordan2)

## A print contact information method
# sonny.print_contact_info()

## Add a friends instance variable (attribute) to the Person class with append method
# jordan.friends.append(sonny) 
# sonny.friends.append(jordan)
# sonny.friends.append(phong)
# print(len(jordan.friends))
# print(len(sonny.friends))

## Implement and use a method to add friends
# jordan.add_friends(sonny)
# print(len(jordan.friends))

## Count numbers of friends
# jordan.num_friends()

## Count number of greetings
# print(sonny.greet_count)
# sonny.greet(jordan)
# print(sonny.greet_count)
# sonny.greet(jordan)
# print(sonny.greet_count)

## __str__ make a string for objects
# print(jordan)
# print(sonny)

## 2. Make your own class
# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     # Add a method
#     def print_info(self):
#         print(f"{self.make} {self.model} {self.year}")

# car = Vehicle('Nissan','Leaf','2015')
# print(car.make, car.model, car.year)

# # Add a method print
# car.print_info()

