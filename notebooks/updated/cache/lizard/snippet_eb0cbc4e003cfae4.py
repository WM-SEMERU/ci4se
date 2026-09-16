def _check_valid_data(self, data):
    if data.dtype.type != np.float32 and data.dtype.type != np.float64:
        raise ValueError(
            'Must initialize normals clouds with a numpy float ndarray')
    if data.shape[0] != 3:
        raise ValueError(
            'Illegal data array passed to normal cloud. Must have 3 coordinates'
            )
    if len(data.shape) > 2:
        raise ValueError(
            'Illegal data array passed to normal cloud. Must have 1 or 2 dimensions'
            )
    if np.any((np.abs(np.linalg.norm(data, axis=0) - 1) > 0.0001) & (np.
        linalg.norm(data, axis=0) != 0)):
        raise ValueError(
            'Illegal data array passed to normal cloud. Must have norm=1.0 or norm=0.0'
            )