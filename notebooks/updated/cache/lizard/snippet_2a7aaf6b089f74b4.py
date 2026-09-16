def deserialize_skycoord(d):
    if 'distance' in d:
        args = d['lon'], d['lat'], d['distance']
    else:
        args = d['lon'], d['lat']
    return coords.SkyCoord(*args, frame=d['frame'], representation='spherical')