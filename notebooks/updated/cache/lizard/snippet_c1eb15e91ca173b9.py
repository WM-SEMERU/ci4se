def strategyKLogN(kls, n, k=4):
    assert k > 1
    s = set([n])
    i = 0
    while k ** i <= n:
        s.update(range(n, n - k * k ** i, -k ** i))
        i += 1
        n -= n % k ** i
    return set(map(str, filter(lambda x: x >= 0, s)))