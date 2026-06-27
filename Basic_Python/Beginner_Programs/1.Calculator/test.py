def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        print("cannot divide by zero")
    else:
        return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

should_continue = False
def calculator():
    global should_continue
    
    print("Welcome to The Python Calculator\n")
    n1 = float(input("enter the first digit\n"))
    while not should_continue:
     for operation in operations:
        print(operation)
    
     op = input("pick an operation\n")
     n2 = float(input("enter the second digit\n"))
     ans = operations[op](n1,n2)
     repeat = input("wana repeat type Y for yes or N for no\n").lower()
     if repeat ==  "y":
         n1 = ans 
     else:
         should_continue = True
         print(f"here is the {ans}")
         calculator()

calculator()