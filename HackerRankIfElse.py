''' If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird '''

import math
n = int(input("Enter any integer: "))
if n % 2 != 0:
    print("Weird")
if n % 2 == 0 and 2 <= n <= 5:
    print("Not weird")
if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
if n > 20 and n % 2 == 0:
    print("Not weird")
