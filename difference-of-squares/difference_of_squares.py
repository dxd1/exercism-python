from math import pow

def difference(num):
    return square_of_sum(num)-sum_of_squares(num)

def square_of_sum(num):
    return pow(sum(range(num+1)), 2)

def sum_of_squares(num):
    return sum([pow(x, 2) for x in range(num+1)])
