import math
import cProfile
import timeit


def primes(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j +=i

    result = [i for i in sieve if i != 0]
    return result

#primes(100)
#6 function calls in 0.000 seconds
#1000 loops, best of 5: 51.5 usec per loop

#primes(1000)
#6 function calls in 0.002 seconds
#1000 loops, best of 5: 720 usec per loop

#primes(10000)
#6 function calls in 0.006 seconds
#1000 loops, best of 5: 8.21 msec per loop



def primes_2(n):
    sieve = set(range(1, n, 2))
    for i in range(2, int(math.sqrt(n))):
        if i in sieve:
            sieve -= set(range(i*i, n, i))
    sieve  = list(sieve)
    sieve[0] = 2
    return sieve



#primes_2(100)
#5 function calls in 0.000 seconds
#1000 loops, best of 5: 12 usec per loop

#primes_2(1000)
#5 function calls in 0.000 seconds
#1000 loops, best of 5: 162 usec per loop

#primes_2(10000)
#5 function calls in 0.002 seconds
#1000 loops, best of 5: 2.15 msec per loop
