def count_extensions(img, extname='SCI'):
    if isinstance(img, str):
        img = fits.open(img, memmap=False)
        img.close()
    elif not isinstance(img, fits.HDUList):
        raise TypeError(
            "Argument 'img' must be either a file name (string) or a `astropy.io.fits.HDUList` object."
            )
    if extname is None:
        return len(img)
    if not isinstance(extname, str):
        raise TypeError(
            "Argument 'extname' must be either a string indicating the value of the 'EXTNAME' keyword of the extensions to be counted or None to return the count of all HDUs in the 'img' FITS file."
            )
    extname = extname.upper()
    n = 0
    for e in img:
        if 'EXTNAME' in list(map(str.upper, list(e.header.keys()))
            ) and e.header['extname'].upper() == extname:
            n += 1
    return n