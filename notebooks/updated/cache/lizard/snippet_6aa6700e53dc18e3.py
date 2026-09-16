def decode_polyline(polyline):
    points = []
    index = lat = lng = 0
    while index < len(polyline):
        result = 1
        shift = 0
        while True:
            b = ord(polyline[index]) - 63 - 1
            index += 1
            result += b << shift
            shift += 5
            if b < 31:
                break
        lat += ~result >> 1 if result & 1 != 0 else result >> 1
        result = 1
        shift = 0
        while True:
            b = ord(polyline[index]) - 63 - 1
            index += 1
            result += b << shift
            shift += 5
            if b < 31:
                break
        lng += ~(result >> 1) if result & 1 != 0 else result >> 1
        points.append({'lat': lat * 1e-05, 'lng': lng * 1e-05})
    return points