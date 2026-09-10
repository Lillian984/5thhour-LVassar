#Name: Lila Vassar
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.

no = [ 9, 7, 3, 6, 2, 20, 4, 284, 21]

#2. Sort the list from highest to lowest.

no.sort()
print(no)
#3. Create an empty list.

ok = []

#4. Remove the median number from the first list and add it to the second list.

yes = no.pop(4)
ok.append(yes)

#5. Remove the first number from the first list and add it to the second list.

maybe = no.pop(0)
ok.append(maybe)

#6. Print both lists.

print(ok)
print(no)

#7. Add the two numbers in the second list together and print the result.

duh = ok[0] + ok[1]
print(duh)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

no.append(duh)

#9. Sort the first list from lowest to highest and print it.

no.sort()
print(no)