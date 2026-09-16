def calc_surface_intensity(self, factor=10):
    pixels = self.roi.pixels_interior
    nside_in = self.config['coords']['nside_pixel']
    surface_intensity = self.kernel.pdf(pixels.lon, pixels.lat)
    for i in np.arange(1, 5):
        nside_out = 2 ** i * nside_in
        radius = factor * np.degrees(hp.max_pixrad(nside_out))
        pix = ang2disc(nside_in, self.kernel.lon, self.kernel.lat, radius,
            inclusive=True)
        idx = ugali.utils.healpix.index_pix_in_pixels(pix, pixels)
        pix = pix[idx >= 0]
        idx = idx[idx >= 0]
        subpix = ugali.utils.healpix.ud_grade_ipix(pix, nside_in, nside_out)
        pix_lon, pix_lat = pix2ang(nside_out, subpix)
        surface_intensity[idx] = np.mean(self.kernel.pdf(pix_lon, pix_lat),
            axis=1)
    return surface_intensity