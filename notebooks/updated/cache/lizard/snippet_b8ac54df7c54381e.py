def sort_points(self, points):
    new_points = []
    z_lookup = {}
    for z, x, Q in points:
        z_lookup[z] = z, x, Q
    z_keys = z_lookup.keys()
    z_keys.sort()
    for key in z_keys:
        new_points.append(z_lookup[key])
    return new_points