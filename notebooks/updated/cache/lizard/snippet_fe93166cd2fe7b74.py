def gini(values, weights=None, bin_size=None):
    if weights is None:
        weights = ones(len(values))
    df = pd.DataFrame({'x': values, 'w': weights})
    df = df.sort_values(by='x')
    x = df['x']
    w = df['w']
    wx = w * x
    cdf = cumsum(wx) - 0.5 * wx
    numerator = (w * cdf).sum()
    denominator = wx.sum() * w.sum()
    gini = 1 - 2 * (numerator / denominator)
    return gini