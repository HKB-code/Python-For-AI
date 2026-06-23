# Variables and Data Types 
# ✅ 1. Variables : a container to store or dump data
name = "Jhon" #string
age = 25 #int
is_Developer = True #bool

print(name,"\n",age,"\n",is_Developer)

# ✅ 2. Variable Naming Rules
yourName = "Jhon Bovi"
user_age = 28
_age = 29
age2 = 30

# ❌ Not Allowed:
# 2age = 25      # starts with number
# user-name = 25 # hyphen not allowed
# class = "A"    # keyword

# ✅ 3. Naming Convention (Python Style)
# snake_case
first_name = "Leon"
total_marks = 95
user_age = 25



# Data Types

# 1.Integer : whole number
age = 25
marks = 100
temperature = -5

print(age)
print(type(age))

# 2.Flaot: Decimal numbers
height = 5.9
pi = 3.14

print(height)
print(type(height))

# 3.String: Text Data
name = "Harshil"
city = 'Amroha'

print(name)
print(type(name))

# 4.Boolean: True or False
is_student = True
is_logged_in = False

print(type(is_student))

# ////////////////////////////////////////

# Strings:
# 1. String Literals:
s1 = "Hello"
s2 = 'World'

# 2. Escaping Characters: If you want to use quote inside a string

msg = "I\'m Leon"
print(msg)

# Common escape sequences:
# \n   # New line
# \t   # Tab
# \"   # Double quote
# \'   # Single quote
# \\   # Backslash

# 3. Multiline Strings:
text = """
Line 1
Line 2
Line 3
"""

print(text)

# 4. String Concatenation:
first = "Leon"
last = "Jin"

full = first + " " + last

print(full)


# 5. f-Strings (Most Important):
name = "leon"
age = 25

print(f"My name is {name} and I am {age}")

# 6. String Indexing: Every character has an index.

name = "leon"

print(name[0])
print(name[2])
# Negative indexing:
print(name[-1])

# 7. String Slicing: string[start:end]
name = "leon"

print(name[0:4])

# 8. Common String Methods
# upper():
print(name.upper())

# lower():
print(name.lower())

# replace():
text = "I like Java"
print(text.replace("Java", "Python"))

# strip():Removes spaces.
t = "   Hello   "
print(t.strip())

# find()
print(name.find("e"))

# count():
n = "ha ha ha ha ha"
print(n.count("h"))

# //////////////////////////////////////////////////////////////
# 📌 LISTS:  collection of values.

# 1. Create a List
fruits = ["apple", "banana", "mango"]

# 2. Indexing
print(fruits[0])

# 3. Slicing
print(fruits[:1])

# 4. Mutate (Modify)
fruits = ["apple", "banana"]

fruits[0] = "mango"

print(fruits) 


# List Methods

# append():

nums = [1, 2]

nums.append(3)

print(nums)

# insert():
nums = [1, 3]

nums.insert(1, 2)

print(nums)

# remove():
nums = [1, 2, 3]

nums.remove(2)

print(nums)

# pop():
nums = [10, 20, 30]

x = nums.pop()

print(x)
print(nums)

# sort(): Ascending sort.
nums = [5, 2, 9, 1]

nums.sort()

print(nums)

# Descending:
nums.sort(reverse=True)

print(nums)

# 📌 List Comprehension
# old way 

square = []
for x in range (5):
    square.append(x*x)
print(square)

squares = [x * x for x in range(5)]

print(squares)

# with conditions:
evens = [x for x in range(10) if x % 2 == 0]

print(evens)


# Dictionary = key-value pairs:
# 1. Create a Dictionary:
deve = {
    "name": "Leon",
    "age": 25,
    "city": "Amroha"
}
print(deve)

# 2. Access Values:

print(deve["name"])
print(deve["age"])

# 3. Add New Key-Value Pair:

deve["language"] = "English"
print(deve)

# 4.Update Existing Value:
deve["age"] = 28
print(deve)

# 5. Delete a Key:

del deve["language"]
print(deve)

# Important Methods

# Keys()

print(deve.keys())

# values()
print(deve.values())

# items()
print(deve.items())

# get(): safe way to access values

print(deve.get("name"))

# Difference Between [] and get()
# print(deve["job"]) #KeyError
print( deve.get("job"))
# default value
print(deve.get("wife",0))



# Iterate Over Dictionaries:

# 1.Loop Through Keys
for key in deve:
    print(key)

# 2. Loop Through Values
for value in deve.values():
    print(value)

# 3. Loop Through Keys Explicitly
for key in deve.keys():
    print(key)

# 4. Loop Through Key-Value Pairs (Most Common):
for key,value in deve.items():
    print(key,value)

#     Dictionary
# Stores data as key-value pairs.
# Keys must be unique.
# Values can repeat.
# Mutable (can be changed).


# ////////////////////////////////
# Tuples: just like list but immutable

person = ("Hello", "World!")
# Access Elements:
print(person[0])
# slicing:
nums = (10, 20, 30, 40)

print(nums[1:3])

# Immutable:
# list: mutable
# nums1 = [1, 2, 3]
# nums[0] = 100

# tuple: immutable 
# nums = (1, 2, 3)
# nums[0] = 100   #TypeError: 'tuple' object does not support item assignment


# Single Element Tuple:
x = (5)
print(type(x))

z = (5,)#Comma is important.
print(type(z))

# Tuple Unpacking:
person = ("Leon", 25)

name, age = person

print(name)
print(age)

# Why Use Tuples?
# When data should not change.
# Coordinates and RGB values usually shouldn't be modified accidentally.
point = (10, 20)
rgb = (255, 0, 0)

# //////////////////////////////////////////////////////
# Sets: unordered collection of unique values.No duplicates, Fast membership checking(in)

n = {1,2,3}
print(n)
# Automatic Deduplication:
n = {1,1,1,2,2,2,3,4,5,3,4,3}
print(n)

# Create Empty Set:
# wrong: Because {} creates a dictionary.
s= {}
print(type(s))
# Correct:
s = set()
print(type(s))

# Add Elements:
n.add(8)
print(n)

# Remove Elements:
n.remove(8)
print(n)

# Membership Check (in):One of the biggest uses of sets.
print(8 in n)
print(5 in n)

# Fast Deduplication Trick:
names = ["A", "B", "A", "C", "B"]
unique_names = list(set(names))

print(unique_names)

# Iterate Over Set:
nb = {1,2,3}
# No guaranteed order
for n in nb:
    print(n)

