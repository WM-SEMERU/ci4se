def gridscan(xi, yi, xf, yf, stepx=1, stepy=1):
    if stepx <= 0:
        raise ValueError('X-step must be positive')
    if stepy <= 0:
        raise ValueError('Y-step must be positive')
    dx = stepx if xf >= xi else -stepx
    dy = stepy if yf >= yi else -stepy
    for y in range(yi, yf + dy, dy):
        for x in range(xi, xf + dx, dx):
            yield x, y