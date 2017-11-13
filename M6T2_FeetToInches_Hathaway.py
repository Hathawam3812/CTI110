# CTI110
# M6T2 Feet To Inches
# Hathaway
# 10 Nov 2017

# This defines the function to convert feet to inches.
def feet_to_inches():
    # This asks the user to input a distance in feet to be converted to inches.
    feet = int(input('Enter distance in feet. '))
    # We will now multiply the integer input by 12 to assign to inches.
    inches = feet * 12
    # The returned values will be in inches and in feet
    return inches, feet


# The main function will call on the feet_to_inches function
def main():
    # This line will call distance and feet from the feet_to_inches function
    distance, feet = feet_to_inches()
    # The distance of feet will be printed, as will the distance in inches.
    print('The distance of ', feet, ' foot/feet is ', distance, ' inches.')
# Calls the main() function to execute.
main()










