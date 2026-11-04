#Name:Lila
#Class: 5th Hour
#Assignment: HW14
import random
import time
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i >= 1:
    print(i)
    time.sleep(0.2)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

j = 1
while j >= 0:
    if j % 2 == 0:
        print(j)
    time.sleep(0.2)
    j += 1
    if j == 32:
        break
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

l = 1
while l < 30:
    l += 1
    if l % 3 == 0:
        continue
    time.sleep(0.4)
    print(l)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

k = random.randint(1, 6)
while k < 6:
    if k == 1:
        break
    print(k)
    time.sleep(0.4)
    k = random.randint(1, 6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.

k = int(input("Enter a number: "))
while k != 0:
    k = int(input("Enter a number: "))