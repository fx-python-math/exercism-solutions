def sum_of_multiples(limit, multiples):
    res = [num * n for num in multiples if num != 0 for n in range(1, (limit + num - 1) // num)]
            
    res = set(res)

    return sum(res)

    
    
