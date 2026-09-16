def hmtk_histogram_2D(xvalues, yvalues, bins, x_offset=1e-10, y_offset=1e-10):
    xbins, ybins = bins[0] - x_offset, bins[1] - y_offset
    n_x = len(xbins) - 1
    n_y = len(ybins) - 1
    counter = np.zeros([n_y, n_x], dtype=float)
    for j in range(n_y):
        y_idx = np.logical_and(yvalues >= ybins[j], yvalues < ybins[j + 1])
        x_vals = xvalues[y_idx]
        for i in range(n_x):
            idx = np.logical_and(x_vals >= xbins[i], x_vals < xbins[i + 1])
            counter[j, i] += float(np.sum(idx))
    return counter.T