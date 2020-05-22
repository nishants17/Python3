friend_ages = {"Nish" : 10 , "Adam" : 10}

print(friend_ages["Nish"])

friend_ages["Nish"] = 30

print(friend_ages["Nish"])

#Dictionaries have order kept in python 3.7 but cannot have duplicate keys

friends = ({"name" : "Rolf SMith", "age" : 24},
            {"name" : "John", "age": 33})


print(friends[0]["name"]) #Accessing first element in the tuple and then Accessing first key in the dictionary 

friend_ages = [("Rolf", 24), ("Adam",30)]
friend_ages = dict(friend_ages)
print(friend_ages)

