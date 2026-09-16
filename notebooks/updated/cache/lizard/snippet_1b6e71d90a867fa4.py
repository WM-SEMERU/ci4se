def radial_sort(points, origin, normal):
    axis0 = [normal[0], normal[2], -normal[1]]
    axis1 = np.cross(normal, axis0)
    ptVec = points - origin
    pr0 = np.dot(ptVec, axis0)
    pr1 = np.dot(ptVec, axis1)
    angles = np.arctan2(pr0, pr1)
    return points[[np.argsort(angles)]]