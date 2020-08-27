"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N ?
Example:
=> INPUT
    3
    10
=> OUTPUT
    6
    2520
"""


from math import sqrt
from timeit import Timer


# 1st Method
def isPrime(n):
    primeNum = True
    d = round(sqrt(n))
    for i in range(2,d+1):
        if n%i==0:
            primeNum = False
            break
    return primeNum

def small(n):
    smallest = 1
    i = 1
    if n == 1:
        return smallest
    else:
        smallest = 2
        while i <= n:
            r = smallest%i
            if r==0:
                pass
            elif isPrime(i):
                smallest = smallest * i
            elif r!=0:
                div = i//r
                smallest = smallest * div
            i += 1
        return smallest

# 2nd Method

if __name__ == "__main__":
    n = int(input())
    print(small(n))