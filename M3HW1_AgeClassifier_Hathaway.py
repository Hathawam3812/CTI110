# CTI110
# M3HW1 - Age Classifier
# Hathaway
# 20 September 2017
#
# Establish parameters of age
def main():
    # Infant is one year old or less
    Infant = 1
    # Child is over one but younger than 13
    Child = 1.01
    # Teenager is over 13 but younger than 20
    Teenager = 13
    # Adult is 20 and older
    Adult = 20
# Ask for age input
# Float input necessary to calculate decimal integers less than one
    age = float(input('Enter Age (Limit: 2 decimal places): '))
# Run a comparison for age input
# Start with lowest, then compare oldest on down,
# Otherwise it will not get past Child age
    if age <= Infant:
        print ('Infant')
    elif age >= Adult:
        print ('Adult')
    elif age >= Teenager:
        print ('Teenager')
    else:
        print ('Child')
main ()


                 
                           
                    

