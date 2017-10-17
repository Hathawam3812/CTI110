# CTI-110
# M5T2 Bug Collection
# Michael Hathaway
# 17 October 2017


# Accumulator function

# Start with a total of zero.
total = 0


# get number of objects colledted for each day
# Specify in sequence day 1 through day 7.
for day in range(1, 8):

    # Ask for the number of bugs collected for each day
    print('enter bugs collected on day...', day)

    # User must input an integer in whole numbers
    bugs = int(input())

    # Adds a cumulative total for each day
    total += bugs

# display total bugs collected for the specified span of days
print('a total of', total, 'bugs collected.')
