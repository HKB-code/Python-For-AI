# File I/O (Input / Output)
# Syntax:   file = open("filename.txt", "mode")
# mode = "r" = read ,  "w" = write(overwrite) , "a" = append , "x" = create new file , "rb" = read binary , "wb" = write binary

# 1.Open:
# Read File
file= open("demo.txt","r")
content = file.read()
print(content)
file.close()

# Write a File
file1 = open("demo.txt","w")
file1.write("Hello World!")
file1.close()

# Append to a File
file2 = open("demo.txt","a")
file2.write("\nNew Line")
file2.close()

# 📌 with Statement (Recommended):
# instead of:
# file = open("notes.txt")

# # work

# file.close()

# use:
with open("demo.txt", "r") as file0:
    con = file0.read()
    print(con)
# file will automatically close

with open("demo.txt","w") as files:
    files.write("Hello Python")

with open("demo.txt","a") as f:
    f.write("\napple\nbanana\nmango")
# //////////
# read line by line
with open("demo.txt","r") as f1:
    for line in f1:
        print(line)


# ///////////////////////
# 📌 Error Handling:
# n = 10/0   #error: zeroDivisionError   , Program will crash

# it will not crash the program
try: 
    num = 10/0
except ZeroDivisionError:
    print("cannot divide by zero")

try:
    print(int("abc"))
except ValueError:
    print("Invalid Number")

# Catch Any Exception:
try:
    x = 10/0
except Exception as e:
    print(e) #e is error object

# Multiple Exceptions:
try:
    x = int(input("Enter Number: "))
    print(10/x)
except ValueError:
    print("not a valid integer")
except ZeroDivisionError:
    print("cannot divide by zero")


# 📌 finally: it will always execute

try: 
    print("Start")
except:
    print("Error")
finally:
    print("Always run")

# Error + Finally:
try:
    10/0
except ZeroDivisionError:
    print("Error happened")
finally:
    print("Cleanup")

# Real-Life Example:
f01 = None

try:
    f01 = open("demo.txt")
    data = f01.read()
except FileNotFoundError:
    print("File not found")

finally:  #finally ensures cleanup.
    if f01:
        f01.close()

# /////////
# Common File Errors

try:
    open("m.txt")
except FileNotFoundError:
    print("File does not exist")


# //////////////////////////////////////////////////
# Why close()?
# we have to tell the os that the file work is done, and if we forget to close, resources can be wasted 
# The OS allocates certain resources for the file:
# File Descriptor (FD) — A number used to identify the file
# Memory Buffers — To temporarily store data being read or written
# Kernel Data Structures — Internal tracking information maintained by the OS
# File Locks (occasionally) — To prevent conflicts with other programs