def rectangle(code, bits_per_char=6):
    lng, lat, lng_err, lat_err = decode_exactly(code, bits_per_char)
    return {'type': 'Feature', 'properties': {'code': code, 'lng': lng,
        'lat': lat, 'lng_err': lng_err, 'lat_err': lat_err, 'bits_per_char':
        bits_per_char}, 'bbox': (lng - lng_err, lat - lat_err, lng +
        lng_err, lat + lat_err), 'geometry': {'type': 'Polygon',
        'coordinates': [[(lng - lng_err, lat - lat_err), (lng + lng_err, 
        lat - lat_err), (lng + lng_err, lat + lat_err), (lng - lng_err, lat +
        lat_err), (lng - lng_err, lat - lat_err)]]}}