def ToOBMag(self, wave, flux, area=None):
    area = area if area else refs.PRIMARY_AREA
    bin_widths = binning.calculate_bin_widths(binning.calculate_bin_edges(wave)
        )
    arg = flux * bin_widths * area
    return -1.085736 * N.log(arg)