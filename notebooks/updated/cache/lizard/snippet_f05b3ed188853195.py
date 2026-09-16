def fit_plane_to_points(points, return_meta=False):
    data = np.array(points)
    center = data.mean(axis=0)
    result = np.linalg.svd(data - center)
    normal = np.cross(result[2][0], result[2][1])
    plane = vtki.Plane(center=center, direction=normal)
    if return_meta:
        return plane, center, normal
    return plane