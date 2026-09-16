def colorgamut(self):
    try:
        light_spec = self.controlcapabilities
        gtup = tuple([XYPoint(*x) for x in light_spec['colorgamut']])
        color_gamut = GamutType(*gtup)
    except KeyError:
        color_gamut = None
    return color_gamut