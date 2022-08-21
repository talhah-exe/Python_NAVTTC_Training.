# Python program to demonstrate class

class Dog:
    pass




# Python program to demonstrate object

obj = Dog()




# Python Program To Demonstrate "Self"
class dog():

    # init method or constructor
    def __init__(self, breed, age):
        self.breed = "Bull Dog"
        self.age = 5

    def show(self):
        print("Breed is", self.breed)
        print("Age is", self.age)






# Python Program To Demonstrate "The __init__ method"

class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()







# Python Program To Demonstrate "Inheritance"
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary,
                 post):
        self.salary = salary
        self.post = post

    # invoking the __init__ of the parent class
    Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))

    print("IdNumber: {}".format(self.idnumber))
    print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()



# Python Program To Demonstrate "Polymorphism"

class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")




# Python Program To Demonstrate "Encapsulation"

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# Python Program To Demonstrate "Abstraction"


from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()



