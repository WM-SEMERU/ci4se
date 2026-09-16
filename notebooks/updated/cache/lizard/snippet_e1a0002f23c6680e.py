def _check_valid_rotation(self, rotation):
    if not isinstance(rotation, np.ndarray) or not np.issubdtype(rotation.
        dtype, np.number):
        raise ValueError('Rotation must be specified as numeric numpy array')
    if len(rotation.shape) != 2 or rotation.shape[0] != 3 or rotation.shape[1
        ] != 3:
        raise ValueError('Rotation must be specified as a 3x3 ndarray')
    if np.abs(np.linalg.det(rotation) - 1.0) > 0.001:
        raise ValueError('Illegal rotation. Must have determinant == 1.0')