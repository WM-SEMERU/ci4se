def result_dataframe(count, x, width, xmin=None, xmax=None):
    if xmin is None:
        xmin = x - width / 2
    if xmax is None:
        xmax = x + width / 2
    xmin[1:] = xmax[:-1]
    density = count / width / np.sum(np.abs(count))
    out = pd.DataFrame({'count': count, 'x': x, 'xmin': xmin, 'xmax': xmax,
        'width': width, 'density': density, 'ncount': count / np.max(np.abs
        (count)), 'ndensity': count / np.max(np.abs(density))})
    return out