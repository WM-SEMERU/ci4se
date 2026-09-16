def get_region_mask(z, delta, xy=None):
    if xy is None:
        ix, iy = np.unravel_index(np.argmax(z), z.shape)
    else:
        ix, iy = xy
    mz = z > z[ix, iy] - delta
    labels = label(mz)[0]
    mz &= labels == labels[ix, iy]
    return mz