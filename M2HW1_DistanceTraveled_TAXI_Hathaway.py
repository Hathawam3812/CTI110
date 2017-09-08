# COURSE NUMBER
print("CTI-110")
# ASSIGNMENT - LESSON NAME
print("M2HW1 - DistanceTraveled")
# LAST NAME
print("Hathaway")
# DATE
print("07SEP2017")
print(" ")
print(" ")
print(" ")

# Rate has been replaced with Speed to make more sense
# Rate could be mistaken for a dollar amount per mile
print("Input Speed and Distance")
# Distance is defined in miles.
print(" ")
distance = float(input("distance in miles: "))
# Speed is defined in miles per hour.
print(" ")
speed = float(input("speed in MPH: "))
# Time is defined as distance divided by speed.
print(" ")
time = distance / speed
# Output is the time elapsed to travel the distance at the given speed.
print("time: ", distance / speed)

# Additional information: calculate price per mile as a Taxi
print(" ")
print(" ")
rate = 1.25
# Rate is fixed at $1.25 per mile
print("Mike's Taxi Service")
print("Rate Per Mile: $", rate)
# Cost of Mike's Taxi Service
print(" ")
price = rate * distance
print("Please pay this amount $ ", format(price, ',.2f'))



