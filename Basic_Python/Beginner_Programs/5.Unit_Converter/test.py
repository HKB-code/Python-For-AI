def length():
    try:
        print("1.Kilometers to Miles")
        print("2.Miles to Kilometers")

        choice = int(input("Choose (1 or 2): "))
        value = float(input("Enter value: "))

        if choice ==1:
            result = value *0.621371
            print(f"{value} km = {result:.2f} miles")
        elif choice==2:
            result = value/.621371
            print(f"{value} miles = {result:.2f} km")
        else:
            print("Invalid Choice")

    except ValueError:
        print("please enter valid numbers.")


def temperature():
    try:
      print("1.Celsius to Fahrenheit")
      print("2.Fahrenheit to Celsius")
      choice = int(input("Choose (1 or 2): "))
      temp = float(input("Enter temperature: "))
      
      if choice ==1:
          result = (temp*9/5) +32
          print(f"{temp}°C = {result:.2f}°F")
      elif choice ==2:
          result = (temp-32)*5/9
          print(f"{temp}°F = {result:.2f}°C")
      else:
          print("Invalid Choice")
    except ValueError:
        print("Invalid Input")

def Weight():
    try:
    
     print("1. Kg to Pounds")
     print("2. Pounds to Kg")

     choice = int(input("Choose: "))
     weight = float(input("Enter weight: "))

     if choice == 1:
        print(f"{weight} kg = {weight * 2.20462:.2f} lb")

     elif choice == 2:
        print(f"{weight} lb = {weight / 2.20462:.2f} kg")

     else:
        print("Invalid choice")

    except ValueError:
     print("Invalid input")



unit={
   "length" : length,
   "weight": Weight,
   "temperature": temperature
}


def unit_convertor():
   while True:
      print("============ Unit Converter ================")
      print("Available Conversions: ")
      for name in unit:
         print(f"- {name}")
      print("- exit")

      choice = input("\nEnter your choice ").strip().lower()

      if choice =="exit":
        print("Thank you for using Unit Converter!")
        break
      
      converter = unit.get(choice)
      if converter:
         converter()
      else: 
         print("Invalid conversion. Please try again")



unit_convertor()

         


   
   