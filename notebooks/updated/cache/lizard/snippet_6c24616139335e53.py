def augknt(knots, order):
    a = []
    [a.append(knots[0]) for t in range(0, order)]
    [a.append(k) for k in knots]
    [a.append(knots[-1]) for t in range(0, order)]
    return np.array(a)