print("Welcome To The Tip Calculator")
bill  = float(input("Enter the bill\n"))
tip = int(input("Enter the Tip you want to give 10%, 12% ,15%\n"))
if (tip != 10 and tip!=12 and tip!=15):
    print("please enter the valid tip")
else:
    amount = bill+(bill*(tip/100))
    split = int(input("How many people to split the bill?\n"))
    each_amount = "{:.2f}".format(amount/split)
    print(f"The total amount is {amount}, Each person should pay: {each_amount}")
