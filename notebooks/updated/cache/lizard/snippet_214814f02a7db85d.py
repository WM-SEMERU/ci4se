def _polygon_from_coords(coords, fix_geom=False, swap=True, dims=2):
    assert len(coords) % dims == 0
    number_of_points = len(coords) / dims
    coords_as_array = np.array(coords)
    reshaped = coords_as_array.reshape(number_of_points, dims)
    points = [((float(i[1]), float(i[0])) if swap else (float(i[0]), float(
        i[1]))) for i in reshaped.tolist()]
    polygon = Polygon(points).buffer(0)
    try:
        assert polygon.is_valid
        return polygon
    except AssertionError:
        if fix_geom:
            return polygon.buffer(0)
        else:
            raise RuntimeError('Geometry is not valid.')