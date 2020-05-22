lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [{'name': 'Nishant',   
            'numbers': {2,3,4,5,6}},
            {'name': 'Raj',
            'numbers': {5,6,7,8,9}},
            {'name': 'Rajan',
            'numbers': {13,22,5,8,9}}       
            ]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
b = 0
for i in range(0,len(players)):
    print('{0} had {1} in his ticket'.format( players[i]['name'], (players[i]['numbers'].intersection(lottery_numbers))))
    for j in players[i]['numbers'].intersection(lottery_numbers):
      b+=1 
      #print(b)
      count = 0
    while b!= 0:
      count+=1
      b-=1
    print("{0} got {1} numbers right".format(players[i]["name"], count))


    

