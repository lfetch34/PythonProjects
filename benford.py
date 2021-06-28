# Luke Fetchko
# CSCI 236 -- Dr. Wooster
# Program 05 - Benford's Law
# Hours invested: 3-4

# Problems encountered: I tried writing a program to calculate the first 500 fibonacci numbers using recursion, but this approach took way too long to run,
# so I did a little research and also noticed the example you provided to efficiently calculate the first n fibonacci numbers and used the list appending technique.
# I also struggled for a while to parse the height tables from the basketball site you provided, but after a few hours of researching, I realized I can use pandas to effectively parse HTML tables.
# Additionally I tried to use a loop to avoid having many print statements, but the way I stored the counter variables prevented me from being able to use a loop to control outputting the table in the correct format.

# Program runs correctly as it should.

# Import sys module for reading command line argument
import sys

def main():
    # Open the file from command line
    file = open(sys.argv[1],'r')
    # Get the number of lines in the file opened
    num_lines = len(open(sys.argv[1]).readlines())
    # Create list to store the first digit of each number
    first_nums = []
    # Iterate through the file and append first digit of each number to list
    for i in range(num_lines):
        first = int(file.readline()[0])
        first_nums.append(first)
    # Counter variable declarations for each digit
    num_1s = 0
    num_2s = 0
    num_3s = 0
    num_4s = 0
    num_5s = 0
    num_6s = 0
    num_7s = 0
    num_8s = 0
    num_9s = 0
    # Iterate through list containg the first digit of every number and increment counter variables for each digit if condition is true
    for item in first_nums:
        if item == 1:
            num_1s += 1
        elif item == 2:
            num_2s += 1
        elif item == 3:
            num_3s += 1
        elif item == 4:
            num_4s += 1
        elif item == 5:
            num_5s +=1
        elif item == 6:
            num_6s += 1
        elif item == 7:
            num_7s += 1
        elif item == 8:
            num_8s +=1
        elif item == 9:
            num_9s += 1
    # Store the total number of the amount of numbers analyzed from file
    total_nums = num_1s + num_2s + num_3s + num_4s + num_5s + num_6s + num_7s + num_8s + num_9s
    # Output table in proper format with heading, each digit, the counter variable of each digit, and the calculation of frequency percentage rounded to two decimal places
    print("Digit\tCount\tPercent")
    print("1\t"+str(num_1s)+"\t" + str(round(num_1s / total_nums * 100,2)))
    print("2\t"+str(num_2s)+"\t" + str(round(num_2s / total_nums * 100,2)))
    print("3\t"+str(num_3s)+"\t" + str(round(num_3s / total_nums * 100,2)))
    print("4\t"+str(num_4s)+"\t" + str(round(num_4s / total_nums * 100,2)))
    print("5\t"+str(num_5s)+"\t" + str(round(num_5s / total_nums * 100,2)))
    print("6\t"+str(num_6s)+"\t" + str(round(num_6s / total_nums * 100,2)))
    print("7\t"+str(num_7s)+"\t" + str(round(num_7s / total_nums * 100,2)))
    print("8\t"+str(num_8s)+"\t" + str(round(num_8s / total_nums * 100,2)))
    print("9\t"+str(num_9s)+"\t" + str(round(num_9s / total_nums * 100,2)))   
    print("Total\t"+str(total_nums)+"\t" + str(round(total_nums / total_nums * 100,2)))

    file.close()

main()



# Demonstrate that the first digits of the first 500 Fibonacci numbers follow Benford's Law quite closely.

## Output when running on fib500.txt
## Follows Benford's Law very closely, as the frequency of each succesive digit is decreasing, which is exactly following Benford's curve.
#Digit	Count	Percent
#1	151	30.2
#2	88	17.6
#3	63	12.6
#4	47	9.4
#5	40	8.0
#6	33	6.6
#7	29	5.8
#8	27	5.4
#9	22	4.4
#Total	500	100.0



# To what extent does the distribution of protein lengths obey Benford's Law?

# Output when running on proteins.txt
# Follows Benford's Law closely, but there is an oddity since digit 3 appears more frequently than digit 2
# which is unexpected, however all other digit percentages follow the expected pattern of Benford's Law.
# If percentages were plotted in a bar graph, it would mostly still follow the expected pattern of Benford's curve, although we notice an oddity.

#Digit	Count	Percent
#1	125	25.0
#2	95	19.0
#3	100	20.0
#4	58	11.6
#5	45	9.0
#6	31	6.2
#7	18	3.6
#8	17	3.4
#9	11	2.2
#Total	500	100.0

