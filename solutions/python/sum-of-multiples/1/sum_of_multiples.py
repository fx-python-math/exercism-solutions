def sum_of_multiples(limit, multiples):
    res = []
    for num in multiples:
        if num == 0:
            continue
        
        n = 1
        while num * n < limit:
            res.append(num * n)
            n += 1
            
    res = list(set(res))
    print(res)

    return sum(res)

    
    
