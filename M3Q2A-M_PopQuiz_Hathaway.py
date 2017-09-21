# Question M3Q2A-M
# Hathaway
# 21 September 2017
#

def main():
    print ()
    # Water temperature in degrees Fahrenheit
    # solid <= 32
    # liquid <= 33 but < 212
    # gas >= 212
    temperature = int(input('Enter water temperature sample in Fahrenheit. '))
    if temperature < 33:
        print ('state of water matter sample is SOLID')
    elif temperature >= 212:
        print ('state of water matter sample is GAS')
    else:
        print ('state of water matter sample is LIQUID')
main()

        

