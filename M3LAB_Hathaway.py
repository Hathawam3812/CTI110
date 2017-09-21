# CTI110
# M3LAB Calculate Student Grades
# Hathaway
# 20 September 2017

# Establish parameters of grading
def main():
    A_grade = 90
    B_grade = 80
    C_grade = 70
    D_grade = 60
    E_grade = 50
# Ask for numerical grade input    
    score = int(input('Enter Numerical Score, 0 to 100: '))
# Run a comparison for the input to be classified to a letter grade   
    if score >= A_grade:
        print ('Your grade is: A')
    elif score >= B_grade:
        print ('Your grade is: B')
    elif score >= C_grade:
        print ('Your grade is: C')
    elif score >= D_grade:
        print ('Your grade is: D')
    else:
        print ('Your grade is: E')
main ()


                 
                           
                    

