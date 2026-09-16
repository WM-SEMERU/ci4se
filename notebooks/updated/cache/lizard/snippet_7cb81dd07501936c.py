def write(filename, data, extname=None, extver=None, units=None, compress=
    None, table_type='binary', header=None, clobber=False, **keys):
    with FITS(filename, 'rw', clobber=clobber, **keys) as fits:
        fits.write(data, table_type=table_type, units=units, extname=
            extname, extver=extver, compress=compress, header=header, **keys)