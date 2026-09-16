def write_fits(self, fitsfile):
    tab = self.create_table()
    hdu_data = fits.table_to_hdu(tab)
    hdus = [fits.PrimaryHDU(), hdu_data]
    fits_utils.write_hdus(hdus, fitsfile)