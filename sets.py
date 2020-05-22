art_friends = {"Rolf","Anne"}

science_friends = {"Pankaj","Udaas","Anne"}



art_friends.add("Jen")

print(art_friends)

art_friends.add("Jen") #Notice that the order of the sets can change because they are unordered 

#We don't "append" to sets because appending means "adding at the end". Since sets #don't have order, there is no "end" to add to.


art_but_not_science = art_friends.difference(science_friends) #Subtract operation in sets. Elements that are in one but not in other


not_in_both = art_friends.symmetric_difference(science_friends) #Elements that are in one but not in both

print("Art but not in science",art_but_not_science)
print("not in both",not_in_both)



