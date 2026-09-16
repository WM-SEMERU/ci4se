def get_point_index(point, all_points, eps=0.0001):
    inds = np.where(np.linalg.norm(point - all_points, axis=1) < eps)
    if inds[0].shape[0] == 0:
        return -1
    return inds[0][0]