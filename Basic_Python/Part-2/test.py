# control flow
for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(5):
    if i ==3:
        continue
    print(i)

n = 5
while n>0:
    print(n)
    n-=1

l = ["apple","mango","banana"]
for item in l:
    print(item+"pie")

# Functions:
def greet():
    print("Hello")

greet()

def greet(name):
    print(f"Hello {name}")

greet("world")

def add(a, b):
    return (a + b)

z= add(10, 20)
print(z)

def get_Person():
    return "Leon",25

name,age = get_Person()
print(name,age)

print(get_Person())  # it returns a tuple

# Default Arguments

def greet1(name="World"):
    print(f"Hello {name}")

greet1()
greet1("Leon")

# Multiple Default Arguments:
def power(base,exp=2):
    return base**exp

print(power(5))
print(power(5,3))



# 📌 *args : collects positional arguments in tuple
# variable number of positional arguments
def add(*args):
    return (args)
z = add(1,2,3,4)
def adds(*args):
    return sum(args)

print(adds(1,2,3,4))
print(type(z))

# 📌 **kwargs: It collects in dictionary, variable number of keyword arguments
def show(**kwargs):
    
    return kwargs

v = show(name="Leon", age=25)
print(type(v))
print(v)

def s(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    
s(name="Leon",age=25)

def d(*args,**kwargs):
    print(args)
    print(kwargs)

d(1,2,3,name="Leon",age=25)