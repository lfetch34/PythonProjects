# Luke Fetchko
# CSCI 236
# 1/30/2020
# Program 01 - Steps
# approximate number of hours you invested: 2 hours
# Grade Version (so if you did the A version say: A version)
# At first I kept getting a error saying 'invalid non-printable character U+2003' while trying to run, but I figured out it was because there was an extra space right under the main() call
# status of the program: compiles and runs as it should
# need to import sys module
import sys
# Named constants - create one for each month to store number of days in that month; assume this is NOT a leap year
# Left out constant for FEB since it may change based on number of lines in read in file
JAN = 31
MAR = 31
APR = 30
MAY = 31
JUN = 30
JUL = 31
AUG = 31
SEP = 30
OCT = 31
NOV = 30
DEC = 31
def main():
    # Open the steps file using the first command line argument to get the input file name. For example: python steps.py steps.txt would open the file steps.txt to read the steps 
    steps_file = open(sys.argv[1], 'r')
    num_of_days = len(open(sys.argv[1]).readlines(  ))
    if (num_of_days > 365):
        FEB = 29
    else:
        FEB = 28
    # Display the average steps for each month using a function to calculate and display
    average_steps(steps_file,'January',JAN)
    average_steps(steps_file,'Febuary',FEB)
    average_steps(steps_file,'March',MAR)
    average_steps(steps_file,'April',APR)
    average_steps(steps_file,'May',MAY)
    average_steps(steps_file,'June',JUN)
    average_steps(steps_file,'July',JUL)
    average_steps(steps_file,'August',AUG)
    average_steps(steps_file,'September',SEP)
    average_steps(steps_file,'October',OCT)
    average_steps(steps_file,'November',NOV)
    average_steps(steps_file,'December',DEC)
 
    
 
    # Close the file.
    steps_file.close()
 
def average_steps(file, month_name, days):
    # compute the average number of steps for the given month
    summ = 0
    for i in range(days):
        steps = int(file.readline())
        summ += steps
    avg = summ / days
    f = str('{:.1f}'.format(avg))
    # output the results
    print('The average steps taken in',month_name,'was',f)
    
main()
