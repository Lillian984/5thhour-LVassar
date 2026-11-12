#Name: Lila
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library

import random
import math

#2. print "Hello World!"

print("Hello World")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
c = int(input("Give me a number: "))

#4. Add a and b together, then divide the sum by c. Print the result.

mathh = (a + b) /c
print(math)

#5. Round the result from #3 up or down, and then determine if it is even or odd.
r = round(mathh)
print(r)
if r % 2 == 0:
    print("It's even")
else:
    print("It's odd")

#6. Create a list of five different random integers between 1 and 10.

math_list = [ 2, 4, 6, 8, 10]

#7. Print the 4th number in the list.

print(math_list[3])

#8. Append another integer to the end of the list, also random from 1 to 10.

math_list.append(random.randint(1, 10))
print(mathh)

#9. Sort the list from lowest to highest and then print the 4th number in the list again.

math_list.sort()
print(math_list[3])

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i

#11. Create a list containing the names of five other students in the classroom.

listt = ["Neely", "Gavin", "Oliver", "Cruz", "Ethan"]

#12. Create a for loop that individually prints out the names of each student in the list.

for name in listt:
  print(name)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.

for number in range(1, 100):
    if number % 10 == 0:
      break
    else:
        print(number)

#14. Free space. Do something creative. :)

knock_knock = ("Knock Knock")
print(knock_knock)

w = input("Answer: ")

if w == "whos there":
    print("No one")
