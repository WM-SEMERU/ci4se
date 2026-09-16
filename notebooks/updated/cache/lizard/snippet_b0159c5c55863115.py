def _moments_central(data, center=None, order=1):
    data = np.asarray(data).astype(float)
    if data.ndim != 2:
        raise ValueError('data must be a 2D array.')
    if center is None:
        from ..centroids import centroid_com
        center = centroid_com(data)
    indices = np.ogrid[[slice(0, i) for i in data.shape]]
    ypowers = (indices[0] - center[1]) ** np.arange(order + 1)
    xpowers = np.transpose(indices[1] - center[0]) ** np.arange(order + 1)
    return np.dot(np.dot(np.transpose(ypowers), data), xpowers)