def from_polygon_skycoord(cls, skycoord, inside=None, max_depth=10):
    return MOC.from_polygon(lon=skycoord.icrs.ra, lat=skycoord.icrs.dec,
        inside=inside, max_depth=max_depth)