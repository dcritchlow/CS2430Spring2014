# =========================================================================== #
#    Imports
# =========================================================================== #

import timeit

# =========================================================================== #
#    Functions
# =========================================================================== #

def fibonacci(number):
    ''' Recursive Fibonacci '''
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def iterative_fibonacci(number):
    ''' Iterative Fibonacci '''
    if number == 0:
        return 0
    else:
        x, y = 0, 1
        for i in xrange(1, number):
            z = x + y
            x, y = y, z
        return y

def base_expansion(number, base):
    ''' Expand number to base "base" '''
    q = number
    a = []
    while q != 0:
        a.append(q % base)
        q = q // base
    return a

def modular_exponentiation(b, n, m):
    ''' Calculates Modular Exponentiation for base 2 Iteratively '''
    a = base_expansion(n, 2) # calculate for base 2
    x = 1
    power = b % m
    for i in range(0, len (a)):
        if a[i] == 1:
            x = (x * power) % m
        power = (power * power) % m
    return x

def recursive_modular_exponentiation(b, n, m):
    ''' Recursive Modular Exponentiation '''
    if n == 0:
        return 1
    elif n % 2 == 0:
        return recursive_modular_exponentiation(b, n//2, m)**2 % m
    else:
        return (recursive_modular_exponentiation(b, n//2, m)**2 % m * b % m) % m

# =========================================================================== #
#    Main
# =========================================================================== #

if __name__ == '__main__':

    t1 = timeit.Timer('a = 20; fibonacci(a)', 'from __main__ import fibonacci')
    t2 = timeit.Timer('a = 20; iterative_fibonacci(a)', 'from __main__ import iterative_fibonacci')

    print '\n Find Fibonacci number for "20"'
    print '\n       Recursive:', fibonacci(20)
    print '\n       Iterative:', iterative_fibonacci(20)

    print '\nRecursive Fibonacci time:', min(t1.repeat(3, 10))*1000
    print '\nIterative Fibonacci time:', min(t2.repeat(3, 10))*1000

    print '\n Find 7^644 mod 645'
    print '\n       Recursive:', recursive_modular_exponentiation(7, 644, 645)
    print '\n       Iterative:', modular_exponentiation(7, 644, 645)

    print '\n Find 11^644 mod 645'
    print '\n       Recursive:', recursive_modular_exponentiation(11, 644, 645)
    print '\n       Iterative:', modular_exponentiation(11, 644, 645)

    print '\n Find 3^2003 mod 99'
    print '\n       Recursive:', recursive_modular_exponentiation(3, 2003, 99)
    print '\n       Iterative:', modular_exponentiation(3, 2003, 99)

    print '\n Find 123^1001 mod 101'
    print '\n      Recursive:', recursive_modular_exponentiation(123, 1001, 101)
    print '\n      Iterative:', modular_exponentiation(123, 1001, 101)


    t3 = timeit.Timer('b=3;n=644;m=645; recursive_modular_exponentiation(b,n,m)', 'from __main__ import recursive_modular_exponentiation')
    t4 = timeit.Timer('b=3;n=644;m=645; modular_exponentiation(b,n,m)','from __main__ import modular_exponentiation')

    print '\nRecursive Modular Exponentiation time:', min(t3.repeat(3, 10))*1000
    print '\nIterative Modular Exponentiation time:', min(t4.repeat(3, 10))*1000
