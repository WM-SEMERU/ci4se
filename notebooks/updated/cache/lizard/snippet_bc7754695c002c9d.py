def drawFrom(self, cumsum, r):
    a = cumsum.rsplit()
    if len(a) > 1:
        b = eval(a[0])[int(a[1])]
    else:
        b = eval(a[0])
    return np.nonzero(b >= r)[0][0]