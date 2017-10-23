# CTI110
# M5HW3 Factorial
# Hathaway
# 22 October 2017




f = float(input('Enter a NON-Negative integer:'))
if f >= 0:
    def factorial(f):
        if f <= 1:
            return 1
        return f * factorial(f - 1)
    print ('The factorial of', f, 'is', factorial(f))


                 
                           
                    

