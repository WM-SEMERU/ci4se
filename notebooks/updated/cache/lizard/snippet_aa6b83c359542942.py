def write(self, outfile):
    hdu_pri = fits.PrimaryHDU()
    hdu_exp = self._create_exp_hdu(self.data)
    hdu_exp.name = 'EXPOSURE'
    hdu_exp_wt = self._create_exp_hdu(self._data_wt)
    hdu_exp_wt.name = 'WEIGHTED_EXPOSURE'
    cols = [Column(name='CTHETA_MIN', dtype='f4', data=self.costh_edges[:-1
        ][::-1]), Column(name='CTHETA_MAX', dtype='f4', data=self.
        costh_edges[1:][::-1])]
    hdu_bnds = fits.table_to_hdu(Table(cols))
    hdu_bnds.name = 'CTHETABOUNDS'
    hdu_gti = fits.table_to_hdu(self._tab_gti)
    hdu_gti.name = 'GTI'
    hdus = [hdu_pri, hdu_exp, hdu_exp_wt, hdu_bnds, hdu_gti]
    for hdu in hdus:
        hdu.header['TSTART'] = self.tstart
        hdu.header['TSTOP'] = self.tstop
    with fits.HDUList(hdus) as hdulist:
        hdulist.writeto(outfile, clobber=True)