def isvalid_age(b):  
  if b.isdigit() == False: #Checks if the string contains only digits
    print(b)
    age2 = int(input(f"Please enter valid age {user_name}"))
    return age2
  else:
    return int(b) #Need to convert string to int as we have to perform month calculation


class Robot:
  def __init__(self,name,age): #Constructor
    self.name = name
    self.age = age
    
r2d2 = Robot("r2d2",  5) #r2d2 Robot object

#robot_name = "Jose"
user_name = input("Hello there! What is your name?")

print(f"Hey {user_name}! I am {r2d2.name}")
age1 = (input(f"How old are you {user_name}?"))
print(type(age1))
a = isvalid_age(age1)
print(a)
print(type(a))



print(f"You have lived here for {(a)*12} months.")

my_number = 5
user_number = int(input("What number am I thinking of?"))
if user_number == my_number:
  print(f"You got it right{user_name}")
else:
  print("Not even close!")



if __name__ == "__main__": 
    print ("Executed when invoked directly")
else: 
    print ("Executed when imported")




