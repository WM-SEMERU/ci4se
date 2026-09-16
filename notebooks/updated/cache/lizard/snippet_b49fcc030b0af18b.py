def merge_all_gti_data(datalist_in, nrows, first):
    max_row = nrows.cumsum()
    min_row = max_row - nrows
    out_hdu = fits.BinTableHDU.from_columns(first.columns, header=first.
        header, nrows=nrows.sum())
    for imin, imax, data_in in zip(min_row, max_row, datalist_in):
        for col in first.columns:
            out_hdu.data[col.name][imin:imax] = data_in[col.name]
    return out_hdu