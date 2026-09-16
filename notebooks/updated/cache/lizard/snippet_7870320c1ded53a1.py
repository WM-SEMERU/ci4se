def get_next_sample(x, y, min_limit=-np.inf, max_limit=np.inf):
    z = np.array(list(zip(x, y)), dtype=np.dtype([('x', float), ('y', float)]))
    z = np.sort(z, order='y')
    n = y.shape[0]
    g = int(np.round(np.ceil(0.15 * n)))
    ldata = z[0:g]
    gdata = z[g:n]
    lymin = ldata['y'].min()
    lymax = ldata['y'].max()
    weights = (lymax - ldata['y']) / (lymax - lymin)
    lx = gmm_1d_distribution(ldata['x'], min_limit=min_limit, max_limit=
        max_limit, weights=weights)
    gx = gmm_1d_distribution(gdata['x'], min_limit=min_limit, max_limit=
        max_limit)
    samples = lx.get_samples(n=1000)
    ei = lx(samples) / gx(samples)
    h = (x.max() - x.min()) / (10 * x.size)
    s = 0
    while np.abs(x - samples[ei.argmax()]).min() < h:
        ei[ei.argmax()] = 0
        s = s + 1
        if s == samples.size:
            break
    xnext = samples[ei.argmax()]
    return xnext