# #Easy Way
# from datetime import date 

# today = date.today()

# try:
#     dob = input("Enter DOB (yyyy/mm/dd): ")
#     year,month,day = map(int,dob.split("/"))
#     age = today.year - year
#     if (today.year,today.month)<(year,month):
#         age-=1
#     print(f"Your age is {age} years.")
# except ValueError:
#     print("Invalid date format")



# //////////////////////////////////////////////////////



# #Best Way

from datetime import date, datetime

try:
    dob = input("Enter DOB (yyyy/mm/dd): ")
    birth_date = datetime.strptime(dob,"%Y/%m/%d").date()
    print(birth_date)
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days <0:
        months-=1
        days+=30 #Approx

    if months<0:
        years-=1
        months+=12

    print(f"Age: {years} years, {months} months, {days} days")
    
except ValueError:
    print("Invalid date format. Use yyyy/mm/dd")


# /////////////////////////////////////////////////////////////////


# #pip install python-dateutil
# from datetime import date
# from dateutil.relativedelta import relativedelta

# dob = date(2000, 1, 10)
# today = date.today()

# diff = relativedelta(today, dob)

# print(
#     f"{diff.years} years, "
#     f"{diff.months} months, "
#     f"{diff.days} days"
# )