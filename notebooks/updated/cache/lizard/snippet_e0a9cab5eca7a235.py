def gridSnap(point, grid=1.0):

    def snapFunc(value):
        value += 1e-06
        remainder = value % grid
        value -= remainder
        newAdd = round(remainder / grid) * grid
        return value + newAdd
    return MapPoint(snapFunc(point.x), snapFunc(point.y))