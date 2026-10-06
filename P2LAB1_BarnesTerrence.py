# Terrence Barnes Jr. 
# 10/6/2026
# P2LAB1
# This program will calculate the diameter, circumference and area of a circle.

import math

radius = float(input("What is the radius of the circle? "))
print()

diameter = 2 * radius

print(f"The diameter of the circle is {diameter:.1f}\n")

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {circumference:.2f}\n")

area = math.pi * radius ** 2

print(f"the area of the circle is {area:.3f}\n")
