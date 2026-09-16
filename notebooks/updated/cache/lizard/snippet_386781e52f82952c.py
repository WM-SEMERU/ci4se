def get_pixel_skydirs(self):
    sky_coords = self._hpx.get_sky_coords()
    if self.hpx.coordsys == 'GAL':
        return SkyCoord(l=sky_coords.T[0], b=sky_coords.T[1], unit='deg',
            frame='galactic')
    else:
        return SkyCoord(ra=sky_coords.T[0], dec=sky_coords.T[1], unit='deg',
            frame='icrs')