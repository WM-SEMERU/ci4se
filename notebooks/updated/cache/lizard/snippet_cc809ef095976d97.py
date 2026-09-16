def gadf(y, method='Quantiles', maxk=15, pct=0.8):
    y = np.array(y)
    adam = np.abs(y - np.median(y)).sum()
    for k in range(2, maxk + 1):
        cl = kmethods[method](y, k)
        gadf = 1 - cl.adcm / adam
        if gadf > pct:
            break
    return k, cl, gadf