def create_table_from_fits(fitsfile, hduname, colnames=None):
    if colnames is None:
        return Table.read(fitsfile, hduname)
    cols = []
    with fits.open(fitsfile, memmap=True) as h:
        for k in colnames:
            data = h[hduname].data.field(k)
            cols += [Column(name=k, data=data)]
    return Table(cols)