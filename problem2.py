""""
Name: round_distances.py

Purpose: Round distances to the nearest kilometre.

Author: Nguyen.D 

Created: 2021-03-04
"""
# initilize counters
distance =0
total = 0
count = 0

# welcome header
print("***** Welcome to the DoorDash Distance Tracker *****")
print()

# loop to get the distance per day
while total < 100:
  distance = int(input("Enter the distance travelled for the day: "))
  total = total + distance
  count += 1

# calculate the speed  
speed = total / count

# print the days it took to surpass 200km 
# and the average speed
print()
print("** Travel Log ** ")
print("It took", count, "days to surpass 100km driven.")

print()
print (" ** Summary ** ")
print("The average distance driven per day is ", int(speed), "km")