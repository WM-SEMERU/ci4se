def geometry(self):
    if self.coord is None:
        return None
    ra = self.coord.ra.degree
    dec = self.coord.dec.degree
    ccds = []
    for geo in self._geometry[self.camera]:
        ycen = geo['dec'] + dec
        xcen = geo['ra'] / math.cos(math.radians(ycen)) + ra
        try:
            dy = geo['ddec']
            dx = geo['dra'] / math.cos(math.radians(ycen))
            ccds.append([xcen - dx / 2.0, ycen - dy / 2.0, xcen + dx / 2.0,
                ycen + dy / 2.0])
        except:
            rad = geo['rad']
            ccds.append([xcen, ycen, rad])
    return ccds