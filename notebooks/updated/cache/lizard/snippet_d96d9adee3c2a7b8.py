def is_separating(direction, polygon1, polygon2):
    norm_squared = direction[0] * direction[0] + direction[1] * direction[1]
    params = []
    vertex = np.empty((2,), order='F')
    for polygon in (polygon1, polygon2):
        _, polygon_size = polygon.shape
        min_param = np.inf
        max_param = -np.inf
        for index in six.moves.xrange(polygon_size):
            vertex[:] = polygon[:, (index)]
            param = cross_product(direction, vertex) / norm_squared
            min_param = min(min_param, param)
            max_param = max(max_param, param)
        params.append((min_param, max_param))
    return params[0][0] > params[1][1] or params[0][1] < params[1][0]