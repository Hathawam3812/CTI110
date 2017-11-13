# CTI-110
# M6HW1 Test Average and Grades
# Hathaway, Michael J.
# 5 November 2017


def main():
    A_Grade = 90
    B_Grade = 80
    C_Grade = 70
    D_Grade = 60

    total = 0
    for grade in range(1,6):
        print('Enter Number', grade)
        Grade = int(input())
        total += Grade
#   print('A number grade of', total, 'will be averaged.')
    Average = (total / 5)
    print('Average Grade is:', Average, 'points.')
    if Average >= A_Grade:
        print ('Your grade is: A')
    elif Average >= B_Grade:
        print ('Your grade is: B')
    elif Average >= C_Grade:
        print ('Your grade is: C')
    elif Average >= D_Grade:
        print ('Your grade is: D')
    else:
        print ('Your grade is: F')      
main()
