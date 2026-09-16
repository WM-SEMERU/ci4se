def radintpix(data, dataerr, bcx, bcy, mask=None, pix=None, returnavgpix=
    False, phi0=0, dphi=0, returnmask=False, symmetric_sector=False,
    doslice=False, errorpropagation=2, autoqrange_linear=True):
    if isinstance(data, np.ndarray):
        data = data.astype(np.double)
    if isinstance(dataerr, np.ndarray):
        dataerr = dataerr.astype(np.double)
    if isinstance(mask, np.ndarray):
        mask = mask.astype(np.uint8)
    return radint(data, dataerr, -1, -1, -1, 1.0 * bcx, 1.0 * bcy, mask,
        pix, returnavgpix, phi0, dphi, returnmask, symmetric_sector,
        doslice, False, errorpropagation, autoqrange_linear)