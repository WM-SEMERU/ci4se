def partial(f, x, i):
    result = f(*[AdFloat(x_j, j == i) for j, x_j in enumerate(x)])
    return result.dx