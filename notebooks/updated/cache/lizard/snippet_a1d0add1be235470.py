def grow_mask(anat, aseg, ants_segs=None, ww=7, zval=2.0, bw=4):
    selem = sim.ball(bw)
    if ants_segs is None:
        ants_segs = np.zeros_like(aseg, dtype=np.uint8)
    aseg[aseg == 42] = 3
    gm = anat.copy()
    gm[aseg != 3] = 0
    refined = refine_aseg(aseg)
    newrefmask = sim.binary_dilation(refined, selem) - refined
    indices = np.argwhere(newrefmask > 0)
    for pixel in indices:
        if ants_segs[tuple(pixel)] == 2:
            refined[tuple(pixel)] = 1
            continue
        window = gm[pixel[0] - ww:pixel[0] + ww, pixel[1] - ww:pixel[1] +
            ww, pixel[2] - ww:pixel[2] + ww]
        if np.any(window > 0):
            mu = window[window > 0].mean()
            sigma = max(window[window > 0].std(), 1e-05)
            zstat = abs(anat[tuple(pixel)] - mu) / sigma
            refined[tuple(pixel)] = int(zstat < zval)
    refined = sim.binary_opening(refined, selem)
    return refined