def boundary_polygon(self, time):
    ti = np.where(time == self.times)[0][0]
    com_x, com_y = self.center_of_mass(time)
    padded_mask = np.pad(self.masks[ti], 1, 'constant', constant_values=0)
    chull = convex_hull_image(padded_mask)
    boundary_image = find_boundaries(chull, mode='inner', background=0)
    boundary_image = boundary_image[1:-1, 1:-1]
    boundary_x = self.x[ti].ravel()[boundary_image.ravel()]
    boundary_y = self.y[ti].ravel()[boundary_image.ravel()]
    r = np.sqrt((boundary_x - com_x) ** 2 + (boundary_y - com_y) ** 2)
    theta = np.arctan2(boundary_y - com_y, boundary_x - com_x
        ) * 180.0 / np.pi + 360
    polar_coords = np.array([(r[x], theta[x]) for x in range(r.size)],
        dtype=[('r', 'f4'), ('theta', 'f4')])
    coord_order = np.argsort(polar_coords, order=['theta', 'r'])
    ordered_coords = np.vstack([boundary_x[coord_order], boundary_y[
        coord_order]])
    return ordered_coords