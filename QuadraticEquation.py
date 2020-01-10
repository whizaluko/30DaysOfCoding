import math

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))
d = (b ** 2) - 4 * a * c

if d < 0:
    print("Imaginary Roots!")
else:
    root1 = (-b + math.sqrt(d)) / 2.0 * a
    root2 = (-b - math.sqrt(d)) / 2.0 * a
    print("Root1 is", root1)
    print("Root1 is", root2)

