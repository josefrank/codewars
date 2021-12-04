"""
Complete the square sum function so that it squares each number passed
into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9
"""

# Solution

def square_sum(numbers):
    # Simple function that uses a For loop and iterates over a list.
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum