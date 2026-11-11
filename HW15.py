#Name: Lila
#Class: 5th Hour
#Assignment: HW15

import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for i in range(5, 0 , -1):
    time.sleep(0.2)
    print(i)
else:
    print("Hello World!")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

for a in range(0,31,2):
    time.sleep(0.2)
    print(a)

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.

for a in range(1,30):
    if a % 3 == 0:
        continue
    time.sleep(0.2)
    print(a)

#4. Create a for loop that prints 5 different animals from a list.

animals = ["Dinosaur", "Snow Leopard", "Horsie", "Donkey", "Squirrel" ]
for animal in animals:
    print(animal)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

Word = ("uzbekistan")
for letter in input("Word please: ")[::-1]:
    print(letter)

#6. Create a list containing 10 integers of your choice and print the list.

num = [20, 281, 645, 2, 8, 229, 283, 1090, 182, 0]
print(num)

#7. Create two empty variables named evenNumbers and oddNumbers.

evenNumbers = 0
oddNumbers = 0

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

for number in num:
    if number % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print(evenNumbers)
print(oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.

ask = int(input("Type a number: "))
empty_number = 1


#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

for rawr in range(1, ask + 1):
    empty_number *= rawr
print(empty_number)