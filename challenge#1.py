"""
If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of or below N.
Example:
=> INPUT
    10
    100
=> OUTPUT
    23
    2318
"""

"""
2 methods exist to solve this porblem: a raw method and a mathematic method
"""

# 1st Method: Raw method
def method_1(n):
    som = 0
    for i in range(n):
        if (i%3==0) or (i%5==0):
            som += i
    return som

#2nd Method: Mathematic method
def calc(x):
    return x*(x+1)

def method_2(n):
    n -= 1
    a = n//3
    b = n//5
    c = n//15
    som = int((3*calc(a) + 5*calc(b) - 15*calc(c)) >> 1)
    return som


if __name__ == "__main__":
    n = int(input())
    print(f'Méthode 1 => {method_1(n)}')
    print(f'Méthode 2 => {method_2(n)}')

# NB: Second method is faster than first method