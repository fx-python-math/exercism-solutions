import math

def upper_bound_nth(k):
    if k == 1: 
        return 2
    if k < 6:
        return [2,3,5,7,11][k-1]

    return int(math.ceil(k * (math.log(k) + math.log(math.log(k)) + 1)))

def era_sieve(k):
    n = upper_bound_nth(k)

    arr = bytearray([1]) * (n + 1)
    arr[0] = arr[1] = 0

    p = 2
    while p * p <= n:
        start = p * p

        if start <= n:
            count = ((n - (p * p)) // p) + 1
            arr[start:n + 1:p] = b'\x00' * count

        for next_index in range(p + 1, n + 1):
            if arr[next_index] == 1:
                p = next_index
                break

    primes = [i for i in range(2, n+1) if arr[i]]
    return primes[k-1]


def prime(k):
    if k == 0:
        raise ValueError('there is no zeroth prime')
    return era_sieve(k)
