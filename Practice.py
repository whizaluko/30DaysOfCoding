n = 7
userAge = [23, 41, 35, 48, 75]
highest = max(userAge)

for i in range(n):
    if highest == max(userAge):
        userAge.remove(max(userAge))

print(max(userAge))

