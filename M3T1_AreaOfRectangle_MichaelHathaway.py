# Course Numbeer
print ("CTI-110")
# Assignment - Lesson Name
print ("M3T1 - Areas of Rectangles")
print ("Not Using main() function")
# Last Name
print ("Hathaway")
# Date
print ("15 September 2017")
print ()
print ()
# This line identifies Rectangle 1
print ("Area of Rectangle_1")
# This line asks for user input of an integer for width
width_1 = int(input("enter width_1: "))
# This line asks for user input of an integer for height
height_1 = int(input("enter height_1: "))
# This line contains the mathematical formula for A = L x W
area_1 = width_1 * height_1
# This line will print the outcome of the calculation
print ("Rectangle_1 area:",area_1)
# Space separator
print ()
# This line identifies Rectangle 2
print ("Area of Rectangle_2")
# This line asks for user input of an integer for width
width_2 = int(input("enter width_2: "))
# This line asks for user input of an integer for height
height_2 = int(input("enter height_2: "))
# This line contains the mathematical formula for A = L x W
area_2 = width_2 * height_2
# This line will print the outcome of the calculation
print ("Rectangle_2 area:",area_2)
# Space separator
print ()
# This section performs a comparison
if area_1 < area_2:
    print ("Rectangle_2 Area is Larger")
elif area_1 == area_2:
    print ("Rectangle Areas Are Equal")
else:
    print ("Rectangle_1 Area is Larger")
    
        
       
    
