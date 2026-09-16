def wcs_to_axes(w, npix):
    npix = npix[::-1]
    x = np.linspace(-npix[0] / 2.0, npix[0] / 2.0, npix[0] + 1) * np.abs(w.
        wcs.cdelt[0])
    y = np.linspace(-npix[1] / 2.0, npix[1] / 2.0, npix[1] + 1) * np.abs(w.
        wcs.cdelt[1])
    if w.wcs.naxis == 2:
        return x, y
    cdelt2 = np.log10((w.wcs.cdelt[2] + w.wcs.crval[2]) / w.wcs.crval[2])
    z = np.linspace(0, npix[2], npix[2] + 1) * cdelt2
    z += np.log10(w.wcs.crval[2])
    return x, y, z