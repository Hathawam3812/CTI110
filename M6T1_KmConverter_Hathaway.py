# CTI-100
# M6T1 Kilometer Converter
# Hathaway Michael
# 10 Nov 2017

#Defines the main function
def main():
   
    # This is where the function will convert kilometers to miles.
    def show_miles():
        # an integer input is required from the user.
        km = int(input('Enter kilometers:'))
        # This will multiply kilometers by .6214 and assign the value to miles.
        mi = km * .6214
        # This will return the product of the calculation for distance in miles.
        print('You traveled ', mi, ' miles.')

    # calls the function
    show_miles()  

main()
    
