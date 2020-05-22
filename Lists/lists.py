friends = ["Jon", "Martha", "Lucius"]
print("My name is" + friends[0])
print("Jon snow is dead")
friends.remove("Jon")
print("I have "+str(len(friends))+" friends now :(")


grades = [80 ,75,90,100] #List is the best choice for grades as it is mutable as compare to tuples
grades = (80, 75, 90, 100)
grades = {80, 75, 90,100} #Worst choice for grades

print(sum(grades))