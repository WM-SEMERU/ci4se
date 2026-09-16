def histogram_distance(arr1, arr2, bins=None):
    eps = 1e-06
    assert arr1.min() > 0 - eps
    assert arr1.max() < 1 + eps
    assert arr2.min() > 0 - eps
    assert arr2.max() < 1 + eps
    if not bins:
        bins = [(x / 10) for x in range(11)]
    hist1 = np.histogram(arr1, bins=bins)[0] / arr1.size
    hist2 = np.histogram(arr2, bins=bins)[0] / arr2.size
    assert abs(hist1.sum() - 1.0) < eps
    assert abs(hist2.sum() - 1.0) < eps
    sqerr = (hist1 - hist2) ** 2
    return sqerr.sum()