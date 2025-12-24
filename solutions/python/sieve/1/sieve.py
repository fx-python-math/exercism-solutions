def primes(n):
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

    primes = [i for i in range(2, n + 1) if arr[i]]
    return primes
