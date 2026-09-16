def create_from_fits(cls, fitsfile, norm_type='eflux', hdu_scan='SCANDATA',
    hdu_energies='EBOUNDS', irow=None):
    if irow is not None:
        tab_s = Table.read(fitsfile, hdu=hdu_scan)[irow]
    else:
        tab_s = Table.read(fitsfile, hdu=hdu_scan)
    tab_e = Table.read(fitsfile, hdu=hdu_energies)
    tab_s = convert_sed_cols(tab_s)
    tab_e = convert_sed_cols(tab_e)
    return cls.create_from_tables(norm_type, tab_s, tab_e)