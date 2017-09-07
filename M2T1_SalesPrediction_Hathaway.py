print('CTI-110')
print('M2T1 - Sales Prediction')
print('Hathaway, Michael J.')
print('07 September 2017')
print(' ')
print(' ')
print(' ')


# Get the projected total sales.
# Converts value to a float that will be applied to Profit calculation.
Total_Sales = float(input('Enter the Projected Total Sales. '))

# Calculate Profit as 23 percent of Total Sales.
# Float input is multiplied by .23 then is sent to next line to display.
Profit = Total_Sales * .23

# Display the Profit.
# Profit is formatted to display commas for thousands and 2 digit for cents.
print ('The Profit Is $', format(Profit, ',.2f'))

               
                           

      
