# Luke Fetchko
# CSCI U236 - Dr. Wooster
# Program 08 - NumPy Timing
# Problems encountered: I thought it was an issue that the times while using lists was faster than using arrays for the loop-based dot function, but did some research and found out due to the overhead
# with using NumPy arrays it takes longer to iterate with a standard for loop in Python when using NumPy arrays.
# Program status: Runs as expected from assignment instructions
# Hours invested: 2 hours

"""
In this program, we use several methods compare the speed of numpy's built-in dot product versus a loop-based dot product. We visualize the results.
"""
# import packages - numpy, timeit and matplotlib.pyplot
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt

"""
Takes two vectors and returns their dot product.
Uses only base python.
"""
def dot(A_arr, B_arr):
    # variable to store total of dot product
    dot_product = 0
    # iterate through values returned from zip function that matches up each element of both vectors at each index
    for a, b in zip(A_arr, B_arr):
        # compute dot product
        dot_product += a*b
    # return dot product
    return dot_product

"""
Now see how the times change as the length of the vector grows. Build a function to time the different dot product functions at different lengths. Timing the function multiple times using the same vector might produce an inaccurate result, because the dot product may be faster to compute for some vectors. Repeat over different vectors to ensure a fair test.
"""
def time_dot_product(
    func,
    vector_length,
    input_type = "array",
    data_reps = 10,
    reps = 2
):
    """
    Takes func, a function that perfroms a calculation on two vectors 
    Returns the times (in ms) the function takes to run on std. normal generated vectors.

    Arguments:
    ----------
    func (function): a function that perfroms a calculation on two vectors
    vector_length (int): the length that the random vectors should be
    input_type (str): controls the data type of the random vector. Takes values \"list\" or \"array\"
    data_reps (int): the number of times to generate the data
    reps (int): the number of times to run the timer for each data set
    """
    # variable to store total execution time
    total = 0
    # repeat process of computing total execution time of function the value of data_reps variable times with loop
    for i in range(data_reps):
        # create array with random numbers with specified vector length from parameter
        A = np.random.standard_normal(vector_length)
        # create array with random numbers with specified vector length from parameter
        B = np.random.standard_normal(vector_length)
        # check if input type is list
        if input_type == 'list':
            # if list, compute total time by adding total time with result of time_function using lists as input
            total += time_function(func, list(A), list(B), reps = reps)
        else:
            # if array, compute total time by adding total time with result of time_function using NumPy arrays as input
            total += time_function(func, A, B, reps = reps)
    # compute average by dividing total execution time by number of repetitions for the data set
    avg = total / data_reps
    # return average execution time for specific dot product computation
    return avg

def time_function(func, *args, reps=10):
    """
    Passes *args into a function, func, and times it reps times, returns the average time in milliseconds (ms).
    """
    avg_time = timeit(lambda: func(*args), number=reps) / reps

    return avg_time * 1000

# use this random seed for testing purposes
np.random.seed(123456)
print("dot product of 2 random vectors using random seed 123456: ", dot(np.random.standard_normal(1000), np.random.standard_normal(1000)))

# create an array, called lengths, of increasing lengths, 1, 10, 100, 1000, 10000, etc based upon number of orders of magnitude; experiement with this number on your computer to see what your machine can handle
ord_mag = 6
lengths = [10 ** n for n in range(0, ord_mag + 1)]

# time the loop-based function using lists as inputs creating a list of times
# using list comprehension create list containing execution times for the different vector lengths with inputs as lists
times_lists = [time_dot_product(dot, x, input_type = "list") for x in lengths]
# time the loop-based function using arrays as inputs creating a list of times
# using list comprehension create list containing execution times for the different vector lengths with inputs as arrays
times_arrays = [time_dot_product(dot, x) for x in lengths]
# time numpy's dot product function creating a list of times
# using list comprehension create list containing execution times for the different vector lengths with inputs as arrays using NumPy's dot product function
times_numpy = [time_dot_product(np.dot, x) for x in lengths]
# plot numpy time vs loop with lists vs loop with arrays
# label each line accordingly
# title: Time Comparison of Dot Product Functions
# label X and Y accordingly
plt.figure(1)
plt.plot(lengths, times_numpy, label = 'arrays with numpy dot product function')
plt.plot(lengths, times_lists, label = 'lists with loop-based function')
plt.plot(lengths, times_arrays, label = 'arrays with loop-based function')
plt.title('Time Comparison of Dot Product Functions')
plt.xlabel('Vector Length')
plt.ylabel('Execution Time (ms)')
plt.legend()
plt.show()

# graph the times for numpy's dot product alone to emphasize that they too are linear in the vector's length
# label & title everything accordingly
plt.figure(2)
plt.plot(lengths, times_numpy)
plt.title('Execution Time of NumPy Dot Product Function for Increasing Vector Size')
plt.xlabel('Vector Length')
plt.ylabel('Execution Time (ms)')
plt.show()
