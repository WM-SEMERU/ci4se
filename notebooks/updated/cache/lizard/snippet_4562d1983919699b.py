def parse_fits(self, fit_name):
    fits = self.fits.loc[self.fits.specimen_comp_name == fit_name].loc[self
        .fits.specimen_tilt_correction == 0]
    fits.reset_index(inplace=True)
    means = self.means.loc[self.means.site_comp_name == fit_name].loc[self.
        means.site_tilt_correction == 0]
    means.reset_index(inplace=True)
    mean_name = str(fit_name) + '_mean'
    setattr(self, fit_name, fits)
    setattr(self, mean_name, means)