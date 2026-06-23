# 📌 OOP (Object-Oriented Programming): In python classes use for representing an object
# 1.Class:
class Student:  #blueprint/template
    pass

# 2.Object: we create object from class
s1 = Student()
s2 = Student()
# both are different objects
print(s1)
print(s2)

# 3._init_: special method , it run automatically run/call when an object is created

class Person:
    def __init__(self,name):
        print("Object Created")
        self.name = name

p1 = Person("Leon")

# 4.self: self=cirrent object

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

e1 = Employee("Leon",25)

# Python internally: Employee._init_(e1,"Leon")
print(e1.name)
print(e1.age)

#/////////////////////////
# methods:

class Intro:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"{self.name} is {self.age} years old")

i1 = Intro("Leon",25)
i1.introduce()

# //////////////////
# Inheritance

class Animal: #parent class
    def speak(self):
        print("Animal speaks")

class Dog(Animal): #child class
    def bark(self):
        print("woof")

d = Dog()

d.speak() 
d.bark()

# Override Method


class Dog1(Animal):
    def speak(self):
        print("woof woof")

d1 = Dog1()
d1.speak()

# //////////////////////////////
# 📌 @property: you can use method as an attribute

# without @property:
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
c = Circle(5)
print(c.area())

# with @property:
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    @property
    def area(self):
       return self.length*self.breadth
    
r = Rectangle(5,6)
print(r.area)
# //////////////////////////
#📌 @staticmethod
class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
print(Math.add(1,2))

class Temperature:
    @staticmethod
    def c_to_f(c):
        return (c*9/5)+32
    
print(Temperature.c_to_f(0))