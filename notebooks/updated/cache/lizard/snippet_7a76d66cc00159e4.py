def grayspec(k):
    ll = 0.5
    ul = 0.8
    delta = (ul - ll) / k
    return [GrayScale(t) for t in np.arange(ll, ul, delta)]