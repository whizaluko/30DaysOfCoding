import random
number = random.randint(0,100)

print("Welcome to Hi-Low Guess Game!")
print()

guess = int(input("Guess a number: "))

while 0 <= guess <= 100:
    if guess < number:
        print("Your guess is too low. Try again!")
    elif guess > number:
        print("Your guess is too high. Try again!")
    else:
        print("You're correct!")
        break
    guess = int(input("Guess a number: "))

else:
    print("Game over! Your guess is out of range. The correct number is", number)