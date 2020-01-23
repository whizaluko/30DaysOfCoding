number = int(input("Enter the number you want to check: "))
divisor = 1
total = 0
while divisor < number:
    if number % divisor == 0:
        total += divisor
    divisor += 1

if number == total:
    print(number, "is perfect")
elif number < total:
    print(number, "is abundant")
elif number > total:
    print(number, "is deficient")

