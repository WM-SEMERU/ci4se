def frommatrix(cls, apart, dpart, det_radius, init_matrix, **kwargs):
    init_matrix = np.asarray(init_matrix, dtype=float)
    if init_matrix.shape not in ((3, 3), (3, 4)):
        raise ValueError(
            '`matrix` must have shape (3, 3) or (3, 4), got array with shape {}'
            .format(init_matrix.shape))
    trafo_matrix = init_matrix[:, :3]
    translation = init_matrix[:, 3:].squeeze()
    default_axis = cls._default_config['axis']
    default_orig_to_det_init = np.array(cls._default_config['det_pos_init'],
        dtype=float) / np.linalg.norm(cls._default_config['det_pos_init'])
    default_det_axes_init = cls._default_config['det_axes_init']
    vecs_to_transform = (default_orig_to_det_init,) + default_det_axes_init
    transformed_vecs = transform_system(default_axis, None,
        vecs_to_transform, matrix=trafo_matrix)
    axis, orig_to_det, det_axis_0, det_axis_1 = transformed_vecs
    if translation.size != 0:
        kwargs['translation'] = translation
    return cls(apart, dpart, det_radius, axis, orig_to_det_init=orig_to_det,
        det_axes_init=[det_axis_0, det_axis_1], **kwargs)