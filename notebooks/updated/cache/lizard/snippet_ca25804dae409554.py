def _apply_uncertainty_to_mfd(self, mfd, value):
    if self.uncertainty_type == 'abGRAbsolute':
        a, b = value
        mfd.modify('set_ab', dict(a_val=a, b_val=b))
    elif self.uncertainty_type == 'bGRRelative':
        mfd.modify('increment_b', dict(value=value))
    elif self.uncertainty_type == 'maxMagGRRelative':
        mfd.modify('increment_max_mag', dict(value=value))
    elif self.uncertainty_type == 'maxMagGRAbsolute':
        mfd.modify('set_max_mag', dict(value=value))
    elif self.uncertainty_type == 'incrementalMFDAbsolute':
        min_mag, bin_width, occur_rates = value
        mfd.modify('set_mfd', dict(min_mag=min_mag, bin_width=bin_width,
            occurrence_rates=occur_rates))