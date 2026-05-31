"""Count the ones in the binary representation of a given base-10 number."""

def egg_count(display_value):
    num = display_value
    if num == 0:
        return 0

    ones = 0

    while num > 0:
        if num % 2 == 1:
            ones += 1
        num //= 2

    return ones
    