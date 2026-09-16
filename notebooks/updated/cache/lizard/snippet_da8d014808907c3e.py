def make_regular_points_with_no_res(bounds, nb_points=10000):
    minlon, minlat, maxlon, maxlat = bounds
    minlon, minlat, maxlon, maxlat = bounds
    offset_lon = (maxlon - minlon) / 8
    offset_lat = (maxlat - minlat) / 8
    minlon -= offset_lon
    maxlon += offset_lon
    minlat -= offset_lat
    maxlat += offset_lat
    nb_x = int(nb_points ** 0.5)
    nb_y = int(nb_points ** 0.5)
    return np.linspace(minlon, maxlon, nb_x), np.linspace(minlat, maxlat, nb_y
        ), (nb_y, nb_x)