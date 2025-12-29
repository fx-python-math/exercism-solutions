def factors(value):
    v = value
    factor_list = []
    p = 2
    while p * p <= v:
        while v % p == 0:
            factor_list.append(p)
            v //= p
        p += 1
    if v > 1:
        factor_list.append(v)
    return factor_list

def prime(n):
    if n == 1:
        return 2
    if n == 0:
        raise ValueError('there is no zeroth prime')
    number_list = [2] + [i for i in range(3, 20*n, 2)]
    primes = []
    for num in number_list:
        f = factors(num)
        if len(f) == 1:
            primes.append(num)
            if len(primes) == n:
                return primes[-1]
