#Name: Lila
#Class: 5th Hour
#Assignment: HW11

import random

#1. Print "Hello World!"

print("Hellloooo Woorrllddd")

#2. Create a list with three variables that each randomly generate a number between 1 and 100

List = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

#3. Print the list.

print(List)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if List[0] > List[1] and List[0] > List[2]:
    print(f"{List [0]} Is the bigger number")
    num = List[0]
elif List[1] > List[0] and List[1] > List[2]:
    print(f"{List [1]} is the bigger number")
    num = List[1]
elif List[2] > List[1] and List[2] > List[0]:
    print(f"{List [2]} Is the bigger number")
    num = List[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".

print(num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 and 2")
    else:
        print(f"{num} is divisible by 2")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by none")

