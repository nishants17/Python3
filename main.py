#import User_input

import Boolean




row_number = 235
result = row_number % 2
print(result)

x = 15 // 2 # Floor division 
print(x)

var1,var2= 10,10


print(str(var1)+' '+str(var2))

my_string = "Hello, world!"
print(my_string)
"""
This is a multi line comment
"""


another_string = "My name is K\"\aan" #Using escape characters 
print(another_string)


name = "Nishant"
full_name = name +" Salian"

print(full_name)


age = 34
age_as_str = str(age)
print("You are "+age_as_str)
print(f"You are {age}") #f string only available in python 3.7


name = "Jose"
final_greeting = """How are you {name}?"""
jose_greeting = final_greeting.format(name = name) # name key is provided a value
print(jose_greeting) 

name = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"
 
address = f"""Name: {name}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""

print(address) #Multi line strings can be defined and can be used to print out using f strings

description = "{} is {} years old."
print(description.format("Bob", 30))

description = "{1} is {0} years old." # Can provide ordering to the string formatter
print(description.format("Bob", 30))

description = "{} is {age} years old."
print(description.format("Bob", age=30))





