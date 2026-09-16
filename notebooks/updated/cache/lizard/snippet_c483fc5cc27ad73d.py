def plot2D_samples_mat(xs, xt, G, thr=1e-08, **kwargs):
    if 'color' not in kwargs and 'c' not in kwargs:
        kwargs['color'] = 'k'
    mx = G.max()
    for i in range(xs.shape[0]):
        for j in range(xt.shape[0]):
            if G[i, j] / mx > thr:
                pl.plot([xs[i, 0], xt[j, 0]], [xs[i, 1], xt[j, 1]], alpha=G
                    [i, j] / mx, **kwargs)