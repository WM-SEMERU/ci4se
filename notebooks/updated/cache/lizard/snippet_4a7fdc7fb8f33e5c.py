def make_data(n):
    p, r, d, w = {}, {}, {}, {}
    J = range(1, n + 1)
    for j in J:
        p[j] = random.randint(1, 4)
        w[j] = random.randint(1, 3)
    T = sum(p)
    for j in J:
        r[j] = random.randint(0, 5)
        d[j] = r[j] + random.randint(0, 5)
    return J, p, r, d, w