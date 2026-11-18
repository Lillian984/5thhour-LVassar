#Name: Lila
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
es = 0
players = int(input("How many players?: "))

m = "Model"
print(m)

for i in range(players - 1):
    r = int(input("Rate model from 1 to 5: "))
    es += r

av =  es / (players-1)
print(av)
