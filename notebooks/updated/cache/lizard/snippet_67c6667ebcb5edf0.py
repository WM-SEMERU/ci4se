def interpolate2dStructuredIDW(grid, mask, kernel=15, power=2, fx=1, fy=1):
    weights = np.empty(shape=(2 * kernel + 1, 2 * kernel + 1))
    for xi in range(-kernel, kernel + 1):
        for yi in range(-kernel, kernel + 1):
            dist = (fx * xi) ** 2 + (fy * yi) ** 2
            if dist:
                weights[xi + kernel, yi + kernel] = 1 / dist ** (0.5 * power)
    return _calc(grid, mask, kernel, weights)