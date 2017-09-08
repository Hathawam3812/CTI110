# COURSE NUMBER
print("CTI-110")
# ASSIGNMENT - LESSON NAME
print("M2HW2 - TipTaxTotal")
# LAST NAME
print("Hathaway")
# DATE
print("07SEP2017")
print(" ")
print(" ")
print(" ")

# Meal Calculations at restaurant
print("Tip Tax Total")
print(" ")
# Cost of a single meal is defined.
print("Thank You for Dining at Mike's Greasy Spoon")
print("Good Food in an Atmosphere of Frivolity")
print(" ")
meal = float(input("Porkchop Slop Gumbo Platter:......$ "))
# Drink cost is defined.
print(" ")
drinks = float(input("Ripple Dipple Rotgut Smoothie:....$ "))
# Subtotal is meal cost plus drink cost.
print(" ")
subtotal = meal + drinks
# Output is the time elapsed to travel the distance at the given speed.
print("            Subtotal:........ $ ", format(meal + drinks, '.2f'))
# Tip gratuity is calculated at 18 percent before taxes and is included in total price.
tip = subtotal * .18
print(" ")
print("Tip Gratuity at 18%:......... $ ", format(tip, '.2f'))
# seven percent Sales Tax is calculated at of cost of meal, not including Tip
tax = subtotal * .07
print("Tax Not Including Tip:....... $ ", format(tax, '.2f'))
print(" ")
# Grand Total is Meal, Tip and Taxes added together
print(" ")
print(" ")
total_amount = subtotal + tip + tax
print("Cough Up This Amount......... $ ", format(total_amount, ',.2f'))
print(" ")
print(" ")
# Thanks and endorsement
print("Thank You, Please Pig Out Here Again !")
print("Hate us on FaceBook")



