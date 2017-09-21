# CTI-110
# M3HW2 - Software Sales
# Hathaway
# 21 September 2017
print(" ")
print(" ")
# Receipt Title
print('Software Sales')
def main():
    # Asks for quantity of software units
    quantity = int(input('Enter Quantity of Software Units. '))
    # Establishes software price
    software_price = 99.00
    # Calculates and prints subtotal
    subtotal = quantity * software_price
    print('Subtotal: . . . . . . . . . . . .$', format(quantity * software_price,'.2f'))
    # Calculates software discounts, prints discount amount,
    # Subtracts discount amount from subtotal
    # Prints discount price with discount amount subtracted from subtotal
    if quantity >= 100:
        print ('          40% Discount')
        forty_percent = subtotal * .4
        print ('Amount of 40% Discount: . . . . .$', format(subtotal * .4,'.2f'))
        print ('Subtotal with 40% Discount:. . . $', format(subtotal - forty_percent,'.2f'))
    elif quantity >= 50:
        print ('          30% Discount')
        thirty_percent = subtotal * .3
        print ('Amount of 30% Discount:. . . . . $', format(subtotal * .3,'.2f'))
        print ('Subtotal with 30% Discount:. . . $', format(subtotal - thirty_percent,'.2f'))
    elif quantity >= 20:
        print ('          20% Discount')
        twenty_percent = subtotal * .2
        print ('Amount of 20% Discount: . . . . .$', format(subtotal * .2,'.2f'))
        print ('Subtotal with 20% Discount: . . .$', format(subtotal - twenty_percent,'.2f'))
    elif quantity >= 10:
        print ('          10% Discount')
        ten_percent = subtotal * .1
        print ('Amount of 10% Discount: . . . . .$', format(subtotal * .1,'.2f'))
        print ('Subtotal with 10% Discount: . . .$', format(subtotal - ten_percent,'.2f'))
    else: print ('Sorry, Quantity Does Not Qualifty For Discount Price')
    
main ()

