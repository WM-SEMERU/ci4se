def pickAChannelList(self, ra_deg, dec_deg):
    try:
        from astropy.coordinates import SkyCoord
        from astropy import units as u
    except ImportError:
        raise ImportError('AstroPy needs to be installed to use this feature.')
    cRa = self.currentRaDec[:, (3)]
    cDec = self.currentRaDec[:, (4)]
    catalog = SkyCoord(cRa * u.deg, cDec * u.deg)
    position = SkyCoord(ra_deg * u.deg, dec_deg * u.deg)
    idx, _, _ = position.match_to_catalog_sky(catalog)
    return self.currentRaDec[idx, 2]