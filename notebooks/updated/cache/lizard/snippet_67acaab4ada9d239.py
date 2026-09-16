def ra_dec_to_cartesian(self, ra, dec):
    self.log.info('starting the ``ra_dec_to_cartesian`` method')
    ra = self.ra_sexegesimal_to_decimal(ra=ra)
    dec = self.dec_sexegesimal_to_decimal(dec=dec)
    ra = math.radians(ra)
    dec = math.radians(dec)
    cos_dec = math.cos(dec)
    cx = math.cos(ra) * cos_dec
    cy = math.sin(ra) * cos_dec
    cz = math.sin(dec)
    cartesians = cx, cy, cz
    self.log.info('completed the ``ra_dec_to_cartesian`` method')
    return cartesians