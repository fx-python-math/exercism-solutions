def square_root(number):
    x = -1
    s_list = []
    
    while number != 0:
        number -= x + 2
        x += 2
        s_list.append(x)

    return len(s_list)
