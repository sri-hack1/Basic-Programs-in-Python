# Taking year input from the user
year = int(input("Enter the year: "))

# Condition for the leap year
if (year % 400 == 0) and (year % 100 ==0):
    print(f"The year {year} is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not a leap year")