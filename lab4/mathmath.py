import math
from math import pi

#1 task
degree = float(input("Enter a degree: "))
radian = format(float(degree * pi / 180),".6f")
print(radian)

#2 task
height = float(input("Enter a height: "))
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
AreaOfTrapeoid = 1/2 * (side1 + side2) * height
print(AreaOfTrapeoid)

#3 task
number_of_sides = int(input("Enter number of sides: " ))
length_of_side = float(input("Enter a length of a side: "))
Area_of_trapezoid = (number_of_sides * length_of_side ** 2) / (4 * math.tan(pi / number_of_sides))
Area_of_trapezoid = round(Area_of_trapezoid)
print(Area_of_trapezoid)

#4 task 
height_of_parallelogram = float(input("Enter a heght of parallelogram: "))
base_of_parallelogram = float(input("Enter a base of parallelogram: "))
Area_of_parallelogram = height_of_parallelogram * base_of_parallelogram
print(Area_of_parallelogram)


