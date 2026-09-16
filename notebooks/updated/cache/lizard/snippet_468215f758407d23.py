def formatPoint(point, affine):
    if affine:
        fmt = '\tx:{}\n\ty:{}'
        coords = [point.x, point.y]
    else:
        fmt = '\tx:{}\n\ty:{}\n\tz:{}'
        coords = [point.x, point.y, point.z]
    coordText = map(hexString, coords)
    return fmt.format(*coordText)