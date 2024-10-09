# Importing math module for calc
import math

# Taking coordinates input 
x1 = float(input("Enter the x1: "))
y1 = float(input("Enter the y1: "))

x2 = float(input("Enter the x2: "))
y2 = float(input("Enter the y2: "))

# Finding euclidean distance from the formula
x_bar = (x2- x1)**2
y_bar = (y2 - y1)**2
value = x_bar + y_bar
dist = math.sqrt(value)

print(f"The distance between the coordinates are:", round(dist, 2))


