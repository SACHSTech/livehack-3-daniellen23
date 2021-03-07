
""""
Name: TournamentTracker.py

Purpose: This program will track the player wins and determine which group a player is placed in.

Author: Nguyen.D 

Created: 2021-03-04
"""

#get the player win and losses
player = (input("Enter the wins and losses for your team: "))

# Set the initial total
total=0

# count the number of wins or "w"
for i in range(len(player)):
  if player[i] == "w":
    total = total + 1
  print(player[i])

# condition and print the team
if total == 5 or total == 6:
  print ("Your team is in Group 1")
elif total == 3 or total == 4:
  print ("Your team is in Group 2")
elif total == 1 or total == 2:
  print ("Your team is in Group 3")
else:
  print ("Your team is eliminated from the tournament")