num = int(input("Enter any number: "))

while num != 1:
    if num % 2 != 0:
        num = num * 3 + 1
    elif num % 2 == 0:
        num = num / 2

    print(num)



