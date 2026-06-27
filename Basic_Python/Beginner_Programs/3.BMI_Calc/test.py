try:
    weight = float(input("enter the weight"))
    height = float(input("enter the height"))

    bmi = weight/height**2
    print(f"Here is your BMI {bmi:.2f}")
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

except ValueError:
    print("Invalid value") 
except ZeroDivisionError:
    print("Height cannot be zero")