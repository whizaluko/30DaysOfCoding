# Safe Lead in Basketball
TeamPoints = int(input("Enter the points difference for the leading team: "))

TeamPoints -= 3

TeamAhead = input("Is the ball with the team that is ahead (Yes or No): ")

if TeamAhead == "Yes":
    TeamPoints += 0.5
else:
    TeamPoints -= 0.5

if TeamPoints < 0:
    TeamPoints = 0

TeamPoints **= 2

SecondsLeft = float(input("Enter the seconds remaining: "))

if TeamPoints > SecondsLeft:
    print("The lead is safe")
else:
    print("The lead is not safe")
  

