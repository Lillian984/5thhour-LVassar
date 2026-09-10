#Name: Lila Vassar
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!

print("Helllllllo Worlllllld")

#1. Create a list with 5 strings containing 5 different names in it.

First_list = ["Timmy", "Tommy", "Kai", "Lexi", "Paedyn"]

#2. Append a new name onto the Name List.

First_list.append("Jessica")

#3. Print out the 4th name on the list.

print(First_list[5])

#4. Create a list with 4 different integers in it.

Second_list = [10,6,4,2]

#5. Insert a new integer into the 2nd spot and print the new list.

Second_list.insert(1, 8)
print(Second_list)

#6. Sort the list from lowest to highest and print the sorted list.

Second_list.sort()
print(Second_list)

#7. Add the 1st three numbers on the sorted list together and print the sum.

Second_list_sum = Second_list[0] + Second_list[1] + Second_list[2]
print(Second_list_sum)

#8. Create a list with two strings, two variables, and too boolean values.

Mixed = ["Taco", "Pancakes", 2, 17, True, False,]

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print(Mixed [int(input("Insert Thing to list: "))])
