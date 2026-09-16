def classify_sources(catalog, sources=None):
    moments = catalog.moments_central
    if sources is None:
        sources = 0, len(moments)
    num_sources = sources[1] - sources[0]
    srctype = np.zeros((num_sources,), np.int32)
    for src in range(sources[0], sources[1]):
        src_x = catalog[src].xcentroid
        src_y = catalog[src].ycentroid
        if np.isnan(src_x) or np.isnan(src_y):
            continue
        x, y = np.where(moments[src] == moments[src].max())
        if x[0] > 1 and y[0] > 1:
            srctype[src] = 1
    return srctype