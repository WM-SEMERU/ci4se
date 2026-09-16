def morphological_geodesic_active_contour(gimage, iterations,
    init_level_set='circle', smoothing=1, threshold='auto', balloon=0,
    iter_callback=lambda x: None):
    image = gimage
    init_level_set = _init_level_set(init_level_set, image.shape)
    _check_input(image, init_level_set)
    if threshold == 'auto':
        threshold = np.percentile(image, 40)
    structure = np.ones((3,) * len(image.shape), dtype=np.int8)
    dimage = np.gradient(image)
    if balloon != 0:
        threshold_mask_balloon = image > threshold / np.abs(balloon)
    u = np.int8(init_level_set > 0)
    iter_callback(u)
    for _ in range(iterations):
        if balloon > 0:
            aux = ndi.binary_dilation(u, structure)
        elif balloon < 0:
            aux = ndi.binary_erosion(u, structure)
        if balloon != 0:
            u[threshold_mask_balloon] = aux[threshold_mask_balloon]
        aux = np.zeros_like(image)
        du = np.gradient(u)
        for el1, el2 in zip(dimage, du):
            aux += el1 * el2
        u[aux > 0] = 1
        u[aux < 0] = 0
        for _ in range(smoothing):
            u = _curvop(u)
        iter_callback(u)
    return u