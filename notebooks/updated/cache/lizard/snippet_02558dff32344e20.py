def search(geo_coords, mode=2, verbose=True):
    if not isinstance(geo_coords, tuple) and not isinstance(geo_coords, list):
        raise TypeError('Expecting a tuple or a tuple/list of tuples')
    elif not isinstance(geo_coords[0], tuple):
        geo_coords = [geo_coords]
    _rg = RGeocoder(mode=mode, verbose=verbose)
    return _rg.query(geo_coords)