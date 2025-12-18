def sum_of_multiples(limit, multiples):
    res = [num for num in multiples 
           if num != 0 
           for num in range(num, limit, num)]
            
    res = set(res)

    return sum(res)