#Name: Lila
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library

import random

#2. print "Hello World!"

print("Hi!")

#3. Create three different variables that each randomly generate an integer between 1 and 10

one = random.randint(1,10)

two = random.randint(1,10)

three = random.randint(1,10)

#4. Print the three variables from #3 on the same line.

print(one, two, three)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.

one = one+2
two = two-4
three = three*1.5

#6. Print each result from #5 on the same line.

print(one, two, three)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

dog_list = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

#8. Sort the list in #7 and print it.

dog_list.sort()
print(dog_list)

#9. Add together the highest three numbers in the list from #7 and print the result.

taco = dog_list[1]+dog_list[2]+dog_list[3]
print(taco)

#10. Create a list with 5 names of other students in this class and print the list.

names = ["neely","lila","max","cruz","echo"]

#11. Shuffle the list in #10 and print the list again.

random.shuffle(names)
print(names)

#12. Print a random choice from the list of names from #10.

names_list = random.choice(names)
print(names_list)