def egg_count(display_value):
    n = display_value
    if n == 0:
        return 0

    ones = 0

    while n > 0:
        if n % 2 == 1:
            ones += 1
        n //= 2

    return ones
    