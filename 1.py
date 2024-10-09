# Taking user input
first = int(input("Enter age1 :"))
second = int(input("Enter age2 :"))
third = int(input("Enter age3 :"))

# Code for getting the oldest one
if (first > second) and (first > third):
    print(first, "is the Oldest")
elif (second> first) and (second> third):
    print(second, "is the oldest")
else:
    print(third, "is the oldest")