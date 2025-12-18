def square_root(number):
    x = -1
    
    while number != 0:
        number -= x + 2
        x += 2

    return x // 2 + 1
