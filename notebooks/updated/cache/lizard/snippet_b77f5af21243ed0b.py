def readcols(infile, cols=None):
    if _is_str_none(infile) is None:
        return None
    if infile.endswith('.fits'):
        outarr = read_FITS_cols(infile, cols=cols)
    else:
        outarr = read_ASCII_cols(infile, cols=cols)
    return outarr