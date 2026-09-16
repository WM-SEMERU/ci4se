def strictly_increasing(values):
    return all(x < y for x, y in zip(values, values[1:]))