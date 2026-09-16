def make_data(n, m):
    I = range(1, n + 1)
    J = range(1, m + 1)
    x, y, w = {}, {}, {}
    for i in I:
        x[i] = random.randint(0, 100)
        y[i] = random.randint(0, 100)
        w[i] = random.randint(1, 5)
    return I, J, x, y, w