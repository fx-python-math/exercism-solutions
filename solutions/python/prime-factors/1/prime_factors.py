def factors(value):
    v = value

    factor_list = []
    p = 2
    while p*p <= v:
        while v % p == 0:
            factor_list.append(p)
            v //= p

        p += 1
    if v > 1:
        factor_list.append(v)

    return factor_list
