def get_input_geo(geo):
    try:
        if geo.SUBCLASS_OF_ID == 70308389:
            return geo
    except AttributeError:
        _raise_cast_fail(geo, 'InputGeoPoint')
    if isinstance(geo, types.GeoPoint):
        return types.InputGeoPoint(lat=geo.lat, long=geo.long)
    if isinstance(geo, types.GeoPointEmpty):
        return types.InputGeoPointEmpty()
    if isinstance(geo, types.MessageMediaGeo):
        return get_input_geo(geo.geo)
    if isinstance(geo, types.Message):
        return get_input_geo(geo.media)
    _raise_cast_fail(geo, 'InputGeoPoint')