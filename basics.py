# This file contains all the basic understanding concepts of python, "Hello World", "Variables", "List", "Tuple",
# "Dictionary", "Loops", "Conditional Statements", "Functions", "Class", "File Handling" & "Text To Speech".

#task1
# #a=34
#b=12
#print(a+b)

#task2
#a= int(input("write firt num:"))
#b= int(input ("write second num:"))
#print("the multiplication of a and b is:", a*b)


#task4
#a = "Welcome to Python class"
#print(a)
#print(len(a))

#task5
# a = "Welcome to Python class"
# print(a.upper())
# print(a.lower())
# print("Welcome" in a)
# print(a.count('e'))

#task6
# z=input("Enter your birth year:")
# print(2022-int(z))

#task7
# f= float(input("enter temperature in fahrenheit: "))
# c= (5/9)*(f-32)
# print("The temperature in celsius is: ", float(c))

# c= float(input("enter temperature in  fahrenheit: "))
# f=(c*9/5)+32
# print("The temperature in celsius is: ", float(f))

 # TASKS 17-3-2022


#TASK1
# list = [112,435,'a',5,"Muet",21,67.11,3]
# print(list)
#
# #TAK2
# print(list[-6:-1])
# print(list[2:4])
#
# #TASK3
# print(len(list))
# print(type(list))
#
# #task4
# print(list.pop())
# print(list)
# print(list.remove(435))
#
# #task5
# list.append("a list")
# print(list)

#task6
l1 =["Hina ","Umama ","Talha ","Afshan "]
l2 =["Memon","Mirani","Khan","Chachar"]
list1= (l1[0]+l2[0], l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])
print(list1)

# #task 7
# list.reverse()
# print(list)


# num = int(input("Enter any number from 1 to 7: "))
# if num == 1:
#     print("Sunday")
# elif num == 2:
#     print("Monday")
# elif num == 3:
#     print("Tuesday")
# elif num == 4:
#     print("Wednesday")
# elif num == 5:
#     print("Thursday")
# elif num == 6:
#     print("Friday")
# elif num == 7:
#     print("Monday")
# else:
#     print("Invalid Input")


# ch = input("Enter a character: ")
#
# if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'
#         or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
#     print(ch, "is a Vowel")
# else:
#     print(ch, "is a Consonant")
#
# ch = input("Enter a character: ")
# ch = ch.lower()
# if ch in "aeiou":
#     print(ch, "is a vowel")
# else:
#     print(ch, "is a Consonant")

# Nested If Else Game

# myNumber = 16
# yourNumber = int(input("Enter Your Number: "))
# if yourNumber == 16:
#     print("You WON")
# else:
#     if yourNumber > 20:
#         print("Too High")
#     else:
#         print("Too Low.")
#


# age = int(input("Enter Your Age: "))
# if 10 <= age <= 18:
#     print("You're a Teenager.")
# else:
#     if age >= 50:
#         print("You are more than 50 years old.")
#     elif age < 10:
#         print("You are less than 10 years old")
#     else:
#         print("You are not a teenager.")


# angle1 = int(input("enter first angle: "))
# angle2 = int(input("enter first angle: "))
# angle3 = int(input("enter first angle: "))
#
# if angle1 + angle2 + angle3 == 180:
#     if (angle1 == 90 and angle2 + angle3) or (angle2 == 90 and angle1 + angle3) or (angle3 == 90 and angle1 + angle2):
#         print("Right angled triangle!")
#     elif angle1 < 90 and angle2 < 90 and angle3 < 90:
#         print("Acute angled triangle")
#     elif angle1 > 90 and angle2 > 90 and angle3 > 90:
#         print("obtuse angled triangle")
# else:
#     print("It's not a triangle")

# hesco charges

# units = int(input("Enter number of units consumed: "))
#
# cost = 0
#
# if 0 < units <= 50:
#     cost = units * 5
# elif 51 <= units <= 100:
#     cost = 50 * 5 + (units - 50) * 8
# elif 101 <= units <= 200:
#     cost = 100 * 8 + (units - 100) * 11
# elif 201 <= units <= 300:
#     cost = 200 * 11 + (units - 200) * 13
# elif 301 <= units <= 500:
#     cost = 300 * 13 + (units - 300) * 19
# elif 501 <= units <= 700:
#     cost = 500 * 19 + (units - 500) * 22
# elif units > 700:
#     cost = 700 * 22 + (units - 700) * 28
#
# FPA = 1.8 * units
# QTR = units * 2.3
#
# hesco_charges = cost + FPA + QTR
# print("hesco charges= ", hesco_charges)
#
# ed = 0.015 * cost
# gst = 0.17 * (cost + ed)
# ptv = 35
# njs = units * 0.7
#
# govt_charges = ed + gst + ptv + njs
# print("govt charges= ", govt_charges)
#
# bill = hesco_charges + govt_charges
#
# print("bill =", b

# for word in ["mehran", "university", "jamshoro"]:
#     for ch in word:
#         print(ch)
#
#
# for i in [[1,2,3], [3,4,6]]:
#         print(i)

# for n in range(1,11):
# odd = (2*n-1) + 100
# print(odd)

# for n in range(5, 0, -1):
#     odd = 10000 - 5*n
#     print(odd)

# for i in range(50,101):
#     if i%7 == 0:
#         print(i)

# start = int(input("please input start of range: "))
# end = int(input("enter end of range: "))
# multiple = int(input("please enter multiple: "))
#
# for i in range(start,end):
#     if i % multiple == 0:
#         print(i)

# sum = 0
# for i in range(1, 11):
#     odd = (2*i-1) + 100
#     sum += odd
#
# print(sum)

# table, method 1
# for i in range(1, 11):
#     print("5 x",i,"=", i*5)

# method 2
# for i in range(1, 11):
#     print("5 x {} = {}" .format(i, i*5))

# max = 0
# for i in range(1,5):
#     num = int(input("enter a number: "))
#     if num > max:
#         max = num
#
#
# print("Maximum = {}" .format(max))

# task 1
# for i in range(10, 0, -1):
#     print(i)

# task 2
# list = []
# item = int(input("enter nos of item: "))
#
# for i in range(item):
#     j = input("enter items: ")
#     list.append(j)
#     print(list)

# task 3
# for i in range(10, 51):
#     if i%3 == 0:
#         print(i)

#
# for i in range(1, 11, 2):
#     print(i)
#
# for i in range(1, 6):
#     odd = (2 * i) - 1
#     print(odd)


# i = 5
# while i>=1:
#     print(i*"*" )
#     i = i - 1
#
# i = 1
# while i<=6:
#     print(i*"*" )
#     i = i + 1


# 31-3-2022
# task 7
# sum = 0
# i = 1
# while i <= 5:
#     add = int(input("enter the numbers: "))
#     sum = sum + add
#     i = i + 1
#
# print("the sum is: ", sum)

# task 8
# fact = 1
# num = int(input("enter a number: "))
# if num > 0:
#     for i in range(1, num + 1):
#         fact = fact * i
#
# print(fact)

# task 9
# import random
# winning_num = random.randint(1, 11)
# num = 0
# counter = 0
# while winning_num != num:
#     num = int(input("Enter your guess b/w 1 to 10: "))
#     if num > winning_num:
#         print("Too High, Try Again.")
#     elif num < winning_num:
#         print("Too Low, Try Again.")
#     else:
#         print("You have Won")
#     counter = counter + 1
# print(" your total counts are: ", counter)

# task 10
# given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(0, len(given_list), 2):
#     print(given_list[i], end=" ")
# print(end="\n")
# for i in range(1, len(given_list), 2):
#     print(given_list[i], end=" ")

# task 11
# num = int(input("Enter the range: "))
# for i in range(1, num+1):
#     cube = pow(i,3)
#     print(cube)


# # task 12
# for i in range(-10,0, 1):
#     print(i)


# 4-1-22
# task 1
# t = (12, 20, 30, 40, 50)
# tpl = list(t)
# tpl.reverse()
# t = tuple(tpl)
# print(t)

# task 2
# tup1 = ("orange", [10, 20,  30], (5, 15, 25))
# print(tup1[1][1])

# rask 3
# tup = str((1, 4, 7, 8, 9))
# print(type(tup))

# task 4
# t1 = (11, 22)
# t2 = (33, 44)
# temp = t1
# t1 = t2
# t2 = temp
# print("t1=", t1)
# print("t2=", t2)

# task 5
# tup2 = (11, [22, 33], 44, 55)
# tup2[1][0] = 222
# print(tup2)

# task 6
# tup3 = (10, 20, 50, 60, 70, 60, 40, 90, 60)
# count_num = tup3.count(60)
# print(count_num)

# task 7
# T1 = (20, 40, 60, 80, 100)
# delete = (T1[:2]+T1[3:])
# print(delete)

# tup = (2, 2, 1, 3)
# print(tup)


# syntax of dictionary
# {key : value}

# d1 = {1: "one", 2: "two", 3: "three"}
# # print(d1[1])
# print(d1)

cities = {'city1': 'HYD', 'city2': 'LAHORE', 'city3': 'KARACHI'}
# print(cities.keys())
# print(cities.values())
# print(cities)
# print(cities.items())
# cities['city4'] = 'MULTAN'
# print(cities)
# cities.pop('city2')
# print(cities)
# del cities['city2']
# print(cities.popitem())
# print(cities)
# d1 = {
#     'name': 'ahmed',
#     'status': 'student',
#     'age': 18,
#     'age': 21,
#     'subject': {1: 'maths', 2: 'eng', 3: 'urdu'}
# }
# print(d1['subject'][2])
# d1['subject'][2] = 'chemistry'
# print(d1)


# from sketchpy import library as lib
# obj = lib.rdj()
# obj.draw()

# from sketchpy import library as lib
# obj = lib.ironman_ascii()
# obj.draw()

# d1 = {1: 'pakistan', 2: 'turkey', 3: 'qatar', 4: 'iran'}
# d2 = {'c1': 'isb', 'c2': 'istanbul', 'c3': 'doha', 'c4': 'tehran'}
#
# d3 = {**d1, **d2}
# print(d3)

# 5-4-22 tasks
# 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# d1 = dict(zip(keys, values))
# print(d1)

# 2
# d1 = {1: 'pakistan', 2: 'turkey', 3: 'qatar', 4: 'iran'}
# d1.pop(3)
# print(d1)

# 3
# d1 = {1: 'pakistan', 2: 'turkey', 3: 'qatar', 4: 'iran'}
# d2 = {'c1': 'isb', 'c2': 'istanbul', 'c3': 'doha', 'c4': 'tehran'}
#
# d3 = {**d1, **d2}
# print(d3)

# 4
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("it exists!")
# else:
#     print("it doesn't exist")

# 5
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 'b' in sample_dict.keys():
#     print("it exists!")
# else:
#     print("it doesn't exist")

# 6
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# sample_dict['d'] = 400
# print(sample_dict)

# 7
# sample_dic = {
#     'emp1': {'name':'ahmed','salary': 7500},
#     'emp2': {'name':'ali','salary': 8000},
#     'emp3': {'name':'bilal','salary': 500}
# }
# sample_dic['emp3']['salary'] = 8500
# print(sample_dic)

# 8
# marks = {
#     'ali': {'urdu': 71, 'eng': 88, 'maths': 67, 'pst': 58, 'eco': 88},
#     'rohan': {'urdu': 61, 'eng': 78, 'maths': 77, 'pst': 58, 'eco': 68},
#     'talha': {'urdu': 75, 'eng': 72, 'maths': 89, 'pst': 54, 'eco': 81},
# }
# a = input("enter the name of the student: ")
# name = a.lower()
# if name in marks.keys():
#     print("Record found")
#     print(marks[name])
# else:
#     print("Record not found")

# # 9
# from sketchpy import library as lib
# obj = lib.tom_holland()
# obj.draw()
#
# # Python3 code to demonstrate
# # each occurrence frequency using
# # naive method
#
# # initializing string
# test_str = "Hello Talha"
#
# # using naive method to get count
# # of each element in string
# all_freq = {}
#
# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
#
# # printing result
# print("Count of all characters in Hello Talha is :\n " + str(all_freq))

#
# str = input("Enter a String: ")
# dict = {}
# for ch in str:
#     if ch in dict:
#         dict[ch] +=1
#     else:
#         dict[ch]=1
#
# for k in dict:
#     print(k, ':', dict[k])


# 1
# def maxi(a,b,c):
#     if a > b and a > c:
#         print('A ia greater')
#     elif b > a and b > c:
#         print('B is greater ')
#     else:
#         print('C is greater')
#
#
# print(maxi(12, 8, 31))

# 2
# def mini(a,b,c):
#     if b < a and c < a:
#         print('A is minimum')
#     elif a < b and c < b:
#         print('B is minimun')
#     else:
#          print('C is minimun')
#
#
# print(mini(12, 8, 3))

# 3
# def find(x):
#     if x % 2 == 0:
#         print('even number!')
#     else:
#         print('odd number!')
#
#
# print(find(71))

# 4
# def cube(a):
#     y = pow(a, 3)
#     return y
#
#
# print(cube(5))

# 5
# def calculator(a, b, c):
#     if c == '-':
#         print(a-b)
#     elif c == '+':
#         print(a+b)
#     elif c == '*':
#         print(a*b)
#     elif c == '/':
#         return a / b
#     else:
#         print("invalid option")
#
#
# print(calculator(21, 5, '-'))

# 6
# def divisible(num):
#     if num % 5 == 0:
#         print("Number is divisible by 5")
#     else:
#         print(" not divisible")
#
#
# print(divisible(225))

# 7
# def vote(age):
#     if age >= 18:
#         print(" Eligible to vote! ")
#     else:
#         print("not eligible to vote!")
#
#
# print(vote(56))

# 8
# def reverse():
#     text = input("enter a string: ")
#     return text[::-1]
#
#
# print(reverse())

# 9
# def check():
#     num = int(input("Enter a number: "))
#     if num > 0:
#         print("Number is positive!")
#     else:
#         print("Number is Negative!")
#
#
# print(check())

# 10
# import math
#
# def area():
#     rad = int(input("Enter radius: "))
#     return math.pi*rad*rad
#
#
# print(area())

# 11
# def vowel():
#     c = input("Enter a character: ")
#     if c in 'aeiou':
#         print("its a vowel ")
#     else:
#         print("not a vowel ")
#
#
# print(vowel())

# 12
# def generate():
#     a = int(input("Enter first num: "))
#     b = int(input("Enter second num: "))
#     for i in range(a, b+1, 2):
#         print(i)
#
#
# print(generate())

# 13
# def odd():
#     a = int(input("Enter first num: "))
#     b = int(input("Enter second num: "))
#     for i in range(a, b+1, 2):
#         print(i)
#
#
# print(odd())


# import math
#
#
# class Circle:
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.radius = r
#
#     def display(self):
#         print("({}, {}) , radius = {}".format(self.x, self.y, self.radius))
#
#     def translate(self, dx, dy):
#         self.x = self.x + dx
#         self.y = self.y + dy
#
#     def scale(self, s):
#         self.radius = self.radius * s
#
#     def area(self):
#         return math.pi * math.pow(self.radius, 2)
#
#     def circum(self):
#         return 2 * math.pi * self.radius
#
#     def atOrigin(self):
#         if self.x == 0 and self.y == 0:
#             return True
#         else:
#             return False
#
#     def showQuadrant(self):
#         if self.x > 0 and self.y > 0:
#             print("First Quadrant")
#         elif self.x < 0 < self.y:
#             print("Second Quadrant")
#         elif self.x < 0 and self.y < 0:
#             print("Third Quadrant")
#         else:
#             print("First Quadrant")
#
#
# c1 = Circle(5, 6, 15)
# c2 = Circle(3, 8, 11)
# c2.translate(5, 5)
# c2.display()
# c2.scale(3)
# c2.display()
# print("Area =", c2.area())
# c2.scale(1.9)
# print("area = ", c2.area())
# c1.display()
# print("Circmference =", c1.circum())
# print(c1.atOrigin())
# c1.showQuadrant()


# class Point:
#     def __init__(self,x ,y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def translate(self, dx, dy, dz):
#         self.x += dx
#         self.y += dy
#         self.z += dz
#
#     def __str__(self):
#         return "({},{},{})".format(self.x, self.y, self.z)
#
#     def is_at_origin(self):
#         if self.x == 0 and self.y == 0 and self.z == 0:
#             return True
#         else:
#             return False
#
#     def __add__(self, other):
#         return Point((self.x + other.x), (self.y + other.y), (self.z + other.z))
#
#     def __sub__(self, other):
#         return Point((self.x - other.x), (self.y - other.y), (self.z - other.z))
#
#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.x and self.z == other.z:
#             return True
#         else:
#             return False
#
#
# p1 = Point(2, 5, 6)
# p2 = Point(1, 2, 4)
# p3 = p1 + p2
# p4 = p1 - p2
# p = p1 == p2
# print(p3)
# print(p4)
# print(p)


# class Contact:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def __str__(self):
#         return "{} ({})".format(self.name, self.number)
#
#
# class Message:
#     def __init__(self, text, number, datetime):
#         self.text = text
#         self.number = number
#         self.datetime = datetime
#
#     def __str__(self):
#         str = "From: " + self.number + "\n"
#         str += "Time: " + self.datetime.strftime("%d/%m/%Y, %H:%M:%S") + "\n"  # STRFTIME = string formatted time
#         str += "--------------------------------" + "\n"
#         str += self.text
#         return str
#
#
# class Phone:
#     def __init__(self, model, number, IMEI):
#         self.model = model
#         self.number = number
#         self.IMEI = IMEI
#         self.contacts = []
#         self.inbox = []
#         self.outbox = []
#
#     def add_contacts(self, cnt):
#         self.contacts.append(cnt)
#
#     def show_contacts(self):
#         print("Total contacts = ", len(self.contacts))
#         print("---------------------------------------")
#         for c in self.contacts:
#             print(c)
#
#     def send_message(self, other_phone, msg):
#         other_phone.inbox.append(msg)
#         self.outbox.append(msg)
#
#     def show_inbox(self):
#         print("Inbox: ", len(self.inbox))
#         print("-------------------------")
#         for m in self.inbox:
#             print(m)
#
#     def show_outbox(self):
#         print("outbox:")
#
#     def __str__(self):
#         str = "Model: " + self.model + "\n"
#         str += "Number: " + self.number + "\n"
#         str += "IMEI: " + self.IMEI + "\n"
#         return str
#
#
# p1 = Phone("IPHONE- 7 PLUS", "033529747331", "23987BRG6")
# p2 = Phone("IPHONE 8", "02341154221", "12DGH8666")
# p3 = Phone("samsung j7", "03352066399", "14y7u7980")
# print(p1, "\n", p2, "\n", p3)
# c1 = Contact("Hina", "030078601")
# c2 = Contact("Talha", "02081762144")
# p1.add_contacts(c1)
# p1.add_contacts(c2)
# p1.show_contacts()

# File Handling
# modes
# r- read, w- write, a- append, x- create new file.
# open(filename +mode)

file = open("mydata.txt", "r")
# f = file.read()
# print(f)
# f = file.readable()
# f = file.readline()       #the number of times readline is called it calls the nth lines
# f = file.read(60)
# print(f)

# with open("mydata.txt", "r") as file:
#     f = file.read()
#     print(f)

# file = open("mydata.txt", "w")
# file.write("It is a 8th week plan!")
# file.close()
# new_file = open("mydata.txt", "r")
# print(new_file.read())

file = open("mydata.txt", "a")
file.write("My name is Hinna")
file.write("Today is a rainy day")
file.close()
print(open("mydata.txt", "r"). readline())


file = open("mydata1.txt", "x")

file = open("mydata1.txt", "w")
file.writelines(["fhjygkjggv\n", "vhgdghh\n", "rsrrfxfs\n"])
file.close()
print(open("mydata1.txt", "r").read())


#textToSpeech

import pyttsx3
friend = pyttsx3.init()
friend.say("Hinna Come Here.")
friend.runAndWait()
