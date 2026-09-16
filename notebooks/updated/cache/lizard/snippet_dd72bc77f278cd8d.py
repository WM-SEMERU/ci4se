def quick_stewart(input_geojson_points, variable_name, span, beta=2,
    typefct='exponential', nb_class=None, nb_pts=10000, resolution=None,
    mask=None, user_defined_breaks=None, variable_name2=None, output=
    'GeoJSON', **kwargs):
    return SmoothStewart(input_geojson_points, variable_name, span, beta,
        typefct, nb_pts, resolution, variable_name2, mask, **kwargs).render(
        nb_class=nb_class, user_defined_breaks=user_defined_breaks, output=
        output)