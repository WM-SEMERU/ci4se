def normalize_layout(l):
    xs = []
    ys = []
    ks = []
    for k, (x, y) in l.items():
        xs.append(x)
        ys.append(y)
        ks.append(k)
    minx = np.min(xs)
    maxx = np.max(xs)
    try:
        xco = 0.98 / (maxx - minx)
        xnorm = np.multiply(np.subtract(xs, [minx] * len(xs)), xco)
    except ZeroDivisionError:
        xnorm = np.array([0.5] * len(xs))
    miny = np.min(ys)
    maxy = np.max(ys)
    try:
        yco = 0.98 / (maxy - miny)
        ynorm = np.multiply(np.subtract(ys, [miny] * len(ys)), yco)
    except ZeroDivisionError:
        ynorm = np.array([0.5] * len(ys))
    return dict(zip(ks, zip(map(float, xnorm), map(float, ynorm))))