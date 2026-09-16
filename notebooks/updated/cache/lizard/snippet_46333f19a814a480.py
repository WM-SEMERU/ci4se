def interpolate_to_points(points, values, xi, interp_type='linear',
    minimum_neighbors=3, gamma=0.25, kappa_star=5.052, search_radius=None,
    rbf_func='linear', rbf_smooth=0):
    r
    if interp_type in ['linear', 'nearest', 'cubic']:
        return griddata(points, values, xi, method=interp_type)
    elif interp_type == 'natural_neighbor':
        return natural_neighbor_to_points(points, values, xi)
    elif interp_type in ['cressman', 'barnes']:
        ave_spacing = cdist(points, points).mean()
        if search_radius is None:
            search_radius = ave_spacing
        if interp_type == 'cressman':
            return inverse_distance_to_points(points, values, xi,
                search_radius, min_neighbors=minimum_neighbors, kind=
                interp_type)
        else:
            kappa = tools.calc_kappa(ave_spacing, kappa_star)
            return inverse_distance_to_points(points, values, xi,
                search_radius, gamma, kappa, min_neighbors=
                minimum_neighbors, kind=interp_type)
    elif interp_type == 'rbf':
        points_transposed = np.array(points).transpose()
        xi_transposed = np.array(xi).transpose()
        rbfi = Rbf(points_transposed[0], points_transposed[1], values,
            function=rbf_func, smooth=rbf_smooth)
        return rbfi(xi_transposed[0], xi_transposed[1])
    else:
        raise ValueError(
            'Interpolation option not available. Try: linear, nearest, cubic, natural_neighbor, barnes, cressman, rbf'
            )