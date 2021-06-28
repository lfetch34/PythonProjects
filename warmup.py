#Name your program file warmup.py

#Submit your working Python code to your CodePost.io account.

#In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

#Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

#Examples

#is_curzon(5) ➞ True
#2 ** 5 + 1 = 33
#2 * 5 + 1 = 11
#33 is a multiple of 11

#is_curzon(10) ➞ False
#2 ** 10 + 1 = 1025
#2 * 10 + 1 = 21
#1025 is not a multiple of 21

#is_curzon(14) ➞ True
#2 ** 14 + 1 = 16385
#2 * 14 + 1 = 29
#16385 is a multiple of 29

#Write a Python program that reads in an integer (without a prompt). Make sure the integer is positive (including zero).
#If it is then output the sum of the Curzon numbers that exist between and including both 1 and the number.
#If the number is not positive then output an error message "input not valid" on a line by itself.

#Repeat this process until you read in a zero, then stop.




# Luke Fetchko
# CSCI 236
# 1/20/21
# Program 00 - Warmup
# 1.5-2 hours invested
# Grade Version (some programs will have A, B, C versions, this one does not)
# At first, I tried to write this program using the sublime text editor on my MacBook, but it would not do anything after reading in an integer,
# I googled this problem and others also had this, so I went back to using IDLE to write and test my program
# status of the program - it compiles and runs as it should, it sums up the curzon numbers between 1 and the read in integer and prints the sum if the read in integer is positive,
# stops if read in integer is 0,
# and will print "input not valid" if read in integer is negative

def is_curzon(num):
    if ((2 ** num + 1) % (2 * num + 1) == 0):
        return True
    else:
        return False
while True:
    read_in = int(input())
    if read_in == 0:
        break
    elif read_in < 0:
        print("input not valid")
    else:
        sum = 0
        i = 1
        for i in range(read_in + 1):
            if is_curzon(i):
                sum += i
        print(sum)
                
