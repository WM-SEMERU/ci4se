def update_null_primary(hdu_in, hdu=None):
    if hdu is None:
        hdu = fits.PrimaryHDU(header=hdu_in.header)
    else:
        hdu = hdu_in
        hdu.header.remove('FILENAME')
    return hdu