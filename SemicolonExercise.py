# Safe Lead in Basketball
TeamPoints = int(input("Enter the lead team points: "))

TeamPoints = TeamPoints - 3

TeamAhead = input("Is the ball with the team that is ahead (Yes or No): ")

if TeamAhead == "Yes":
    TeamPoints = float(TeamPoints + 0.5)
else:
    TeamPoints = float(TeamPoints - 0.5)

if TeamPoints < 0:
    TeamPoints = 0

TeamPoints = TeamPoints ** 2

SecondsLeft = int(input("Enter the seconds remaining: "))

if TeamPoints > SecondsLeft:
    print("The lead is safe")
else:
    print("The lead is not safe")
