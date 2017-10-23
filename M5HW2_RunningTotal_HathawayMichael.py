# CTI-100
# M5HW2 - Running Total
# Hathaway, Michael
# 22 October 2017
print(" ")
print(" ")
print(" ")

# Define Integers
n = 1
t = 0

# While adding loop, ignoring negative numbers
print('Running Total Exercise')
print('enter a negative number to quit.')
while n >= 0:
    n = float(input('Please enter a number: '))
    if n >= 0:
        t += n
    if n < 0:
        print('TOTAL:', t)
    

    
