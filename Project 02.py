'''

Write a program that reads three side lengths of a triangle (a, b, c) and a radius r.

Check if the three sides can form a triangle (sum of any two sides > third side).

If not valid, print "Triangle does not exist" and skip to step 5.

If valid, determine its type: "Equilateral", "Isosceles", or "Scalene".

Compute the triangle's perimeter.

Using math.pi and math.sqrt(), compute the area of the triangle using Heron's formula:

s = (a + b + c) / 2

area = √(s(s−a)(s−b)(s−c))

Round the area to 2 decimal places using round().

Regardless of triangle validity, compute the area of the circle with radius r using math.pi and round it to 2 decimals.
'''

import math

a = float(input("Enter the first length of the triangle: "))
b = float(input("Enter the second length of the triangle: "))
c = float(input("Enter the third length of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    # Type
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")

    # Perimeter and area (only when valid)
    perimeter = a + b + c
    s = perimeter / 2
    triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Perimeter:", perimeter)
    print("Triangle area:", round(triangle_area, 2))
else:
    print("Triangle does not exist")

# Circle area (always computed)
r = float(input("Enter the radius: "))
circle_area = math.pi * r ** 2
print("Circle area:", round(circle_area, 2))