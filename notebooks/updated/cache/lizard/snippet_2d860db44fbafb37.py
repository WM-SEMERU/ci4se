def ray_spheres_intersection(origin, direction, centers, radii):
    b_v = 2.0 * ((origin - centers) * direction).sum(axis=1)
    c_v = ((origin - centers) ** 2).sum(axis=1) - radii ** 2
    det_v = b_v * b_v - 4.0 * c_v
    inters_mask = det_v >= 0
    intersections = inters_mask.nonzero()[0]
    distances = (-b_v[inters_mask] - np.sqrt(det_v[inters_mask])) / 2.0
    dist_mask = distances > 0.0
    distances = distances[dist_mask]
    intersections = intersections[dist_mask].tolist()
    if intersections:
        distances, intersections = zip(*sorted(zip(distances, intersections)))
        return list(intersections), list(distances)
    else:
        return [], []