# CTI-100
# M6HW1 Grades Average and Scores
# Hathaway, Michael
# 8 November 2017

# After buying some Python books and studying online programming sites, I learned
# how to enhance the grading program.

# Welcome to Grades Averages Version 2.

import sys

# Grade score parameters
MIN_A_GRADE = 90
MIN_B_GRADE = 80
MIN_C_GRADE = 70
MIN_D_GRADE = 60

# calculate the average of the list of scores
# the parameter scores is assumed to be a list that can be converted to floats
def calc_average(scores):
    # scores is a list, so determine the length of the list (e.g. number of list items)
    # and assign it to the variable 'count'
    count = float(len(scores))
    # create the sum variable and initialize it as a float with value 0.0 so we can sum
    sum = float(0.0)
    # for each score in the list of scores...
    for score in scores:
        # add the new score to the total sum
        sum += float(score)
    
    # now divide the total sum by the number of items to compute the average
    avg = sum / count
    
    # and return the average
    return avg
    
    
def determine_grade(score):
    # first make sure that score is a number, not a string
    # because we are comparing against numbers, not strings.
    # e.g. "if score < 60 (int)", not "if score < '60' (str)"
    score = float(score)

    # self-explanatory
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

        
def input_scores():
    print('\nWelcome to Version 2 of Test Scores and Averages\n')
    # create the variable named scores and initialize as a python list ( could also use [] vs list() )
    scores = list()
    # Loop 5 times.  Ask the user for test score input each time we loop
    while len(scores) < 5:
    # This could be written this as:
    # for i in range(5):
    # where 'i' would state which iteration we are currently on
    # e.g. 1, 2, 3, 4, 5
    
        # Get user input. Try is there because per the python documentation for the function input(),
        # it can throw an EOFError exception. If that happens, this should catch the exception.
        try:
            # Get the user input and store it in the variable 'score'
            score = input('Please enter a score:  ')
            # Append the new score to the end of the 'scores' list
            scores.append(float(score))
        
        # catch ValueError.  If the input value cannot be converted to int or float. e.g. letter
        except ValueError:
            print ('Invalid, input must be a number, please try again')
            # continue means go to the start of the loop and do it again
            continue

        # This should catch the EOFError exception if it occurs
        except (EOFError, KeyboardInterrupt):
            # let the user know that an error occurred
            print('Failed to get user input')
            # and exit the program
            sys.exit()

    # Looping is finished. All scores have been entered.
    # Return the list of scores
    return scores

def main():
    # Get user input for test scores
    scores = input_scores()

    # for each score in the list of scores...
    for score in scores:
        # ...determine the letter grade by passing the score to the 'determine_grade' function
        grade = determine_grade(score)
        # Print the score and letter grade
        print ('Letter grade for ' + str(score) + ' is ' + grade)
    
    # calculate the average
    avg = calc_average(scores)
    # print the final average and letter grade by calling the function determine_grade(score)
    
    print('The average test score is: ' + str(avg))
    print('Letter Grade: ' + determine_grade(avg))
    
    

if __name__ == '__main__':
    main()

