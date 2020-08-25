"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of a given number N ?
Example:
=> INPUT
    10
    17
=> OUTPUT
    5
    17
"""

"""
There are 2 methods to solve this challenge.
"""

# 1st Method
from math import sqrt

def isPrime(n):
    primeNum = True
    d = round(sqrt(n))
    for i in range(2,d+1):
        if n%i==0:
            primeNum = False
            break
    return primeNum

def method_1(n):
    setPrime = []
    for i in range(1,n+1):
        if n%i==0 and isPrime(i):
            setPrime.append(i)
    return max(setPrime)

# 2nd method
def method_2(n):
    first = 2
    largest = 2
    d = round(sqrt(n))
    while first <= n:
        if first > d:
            largest = n
            break
        elif n%first==0:
            largest = first
            while n%first==0:
                n = n//first
        first += 1
    return largest

if __name__ == "__main__":
    n = int(input())
    print(f'Method 1 => {method_1(n)}')
    print(f'Method 2 => {method_2(n)}')

"""
NB: The 2nd is faster than the 1st method
"""