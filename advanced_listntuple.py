# Write a program to create a list with random data type elements.
# ls = [1, 2.7, 5, "Muet", 'H']
# print(ls)

# Write a program to print specific elements of a list in single line
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# print(ls[1:5:3])

# Write a program to count the number of items stored in a list and also display it’s
# type.
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# print(len(ls1))
# print(type(ls1))

# Write a program to delete the item from the list using pop and remove method.
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# ls1.pop()
# print(ls1)
# ls1.remove("Muet")
# print(ls1)

# Write a program to add any item in the given list.
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# ls1.append(133)
# print(ls1)

# Write a program of python to concatenate first and last name of a person and
# displays a new list. The list should contain atleast 4 items.
# ls = ["Hina", "Faris", "Afshan"]
# ls2 = [" Akhlaque", " Ahmed", " Niaz"]
# ls3 = [ls[0]+ls2[0], ls[1]+ls2[1], ls[2]+ls2[2]]
# print(ls3)

# Write a program to reverse the list items.
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# ls1.reverse()
# print(ls1)

# Write a Python program to sum all the items in a list.
# lis = [1, 2, 5, 14]
# sum=0
# for i in range(0, len(lis)):
#     sum += lis[i]
#
# print(sum)

# Write a Python program to get a list, sorted in decreasing order.
# ls1 = [1, 7, 5, 14.4, 3]
# ls1.sort(reverse=True)
# print(ls1)

# Write a Python program to get a list, sorted in decreasing order.
# ls1 = [1, 2.7, 5, "Muet", 'H', "Yellow", 14.4]
# ls2 = ls1
# print(ls2)

# Write a Python program to get the smallest number from a list
# list = [1, 4, 1.4, 56, 8]
# smallest = list[0]
#
# for i in range(0, len(list)):
#     if smallest < list[i]:
#         smallest = list[i]
#
# print("smallest= ", smallest)

# Create an empty list and then add at least 5 items in the list with the help of list
# methods.
# list = []
# list.append(12)
# list.append(34)
# print(list)


# Write a program to print n natural numbers in descending order using for loop.
# n = 100
#
# for i in range(n, 1, -1):
#     print(i)

 # Write a program to iterate a list. Create an empty list and user will give the list and
# then iterate its items present in the list.
# list1 = []
# a = int(input("enter a range of list items"))
# for i in range(a):
#     b = input(("enter list item"))
#     list1.append(b)
#
# print(list1)


# Write a program to display all the multiples of 3 within the range 10 to 50.
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i)

# Write a program to find “apple” in the given list
# [‘banana’, ‘orange’, ‘apple’, ‘mango’]. Print “Found” if it is present in the list
# ls = ['banana', 'orange', 'apple', 'mango']
# for i in range(0, len(ls)):
#     if ls[i] == 'apple':
#         print("found at index ", i)


# Write a program to print the square of first 5 numbers
import math
# for i in range(1, 6):
#     print(pow(i, 2))

#. Write a program that accepts a number from the user and calculate the factorial of
# that number. The factorial of an integer n is defined as
# n ! = n ( n - 1)( n - 2)( n - 3) ... (3)(2)(1) ; if n>0
# For example, 5! = 5 x 4 x 3 x 2 x 1
# num = int(input("enter any value: "))
# fact = 1
# if num < 0:
#     print("Factorial doesnot exist!")
# elif num == 1:
#     print("Factorial is 1!")
# else:
#     for i in range(1, num+1):
#         fact = fact * i
#
# print(fact)

# Write a loop to display elements from a given list present at odd index positions.
# Given list is: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output: a. 10 30 50 70 90
#  b. 20 40 60 80 100

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(0, len(list)):
#     if i % 2 == 0:
#         print(list[i], end=" ")

#  Write a program to print the cube of all numbers from 1 to a given number
import math
# n = int(input("enter any number : "))
# for i in range(1, n+1):
#     print(pow(i, 3))


#  Display numbers from -10 to -1 using for loop
# for i in range(-10, 0, 1):
#     print(i)


# list1 = [12,34, "muet",[20,30,50], "jamshoro"]
# print(list1[3][1])

# Write a program to reverse the tuple
# tup = (10,20,30,40,50)
# tup2 = reversed(tup)
# print(tuple(tup2))

# Access value 20 from the tuple.
# Given Tuple is: tup1 = (“Orange”, [10,20,30], (5,15,25)
# tup1 = ("orange", [10,20,30], (5,15,25))
# print(tup1[1][1])


# Write a Python program to convert a tuple to a string
# tup = ('g', 'e', 'e', 'k', 's')
# for i in tup:
#     print(i, end="")

# Swap two tuples in Python. t1 = (11,22)    t2= (33,44)
# t1 = (11, 22)
# t2 = (33, 44)
# t3 = t1
# t1 = t2
# t2 = t3
# print("t1: ",t1)
# print("t2:", t2)


#  Given tuple is: tup2 = (11,[22,33],44,55) Expected output:       (11,[222,33],44,55)
# tup2 = (11, [22, 33], 44, 55)
# tup2[1][0] = 222
# print(tup2)

# Count the number of occurrences of item 60 from a given tuple. Tup3 = (10,20,50,60,70,60)
# Tup3 = (10,20,60,50,60,70,60)
# print(Tup3.count(60))

# Write a program to delete tuple elements.  Tup1 = (20,40,60,80,100). Delete 60 from the given tuple
# Tup1 = (20, 40, 60, 80, 100)
# T = list(Tup1)
# T.remove(60)
# print(tuple(T))


