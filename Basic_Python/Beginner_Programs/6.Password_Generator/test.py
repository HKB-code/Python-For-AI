alpha1 = [chr(i) for i in range (ord("a"),ord("z")+1)]
alpha2 = [chr(i) for i in range (ord("A"),ord("Z")+1)]

letters = [*alpha1,*alpha2]
numbers = [str(i) for i in range(0,10)]
print(numbers)
symbols = [chr(i) for i in range(33, 44)]

password = list()
import random

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(1,nr_letters+1):
  password += random.choice(letters)

for i in range(1,nr_numbers+1):
  password +=random.choice(numbers)

for i in range(1,nr_symbols+1):
  password+=random.choice(symbols)

random.shuffle(password)

new_password = "".join(password)

print(new_password)