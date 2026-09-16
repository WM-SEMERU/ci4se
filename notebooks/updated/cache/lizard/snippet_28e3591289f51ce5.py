def get_hypo_location(self, mesh_spacing, hypo_loc=None):
    mesh = self.mesh
    centroid = mesh.get_middle_point()
    if hypo_loc is None:
        return centroid
    total_len_y = (len(mesh.depths) - 1) * mesh_spacing
    y_distance = hypo_loc[1] * total_len_y
    y_node = int(numpy.round(y_distance / mesh_spacing))
    total_len_x = (len(mesh.lons[y_node]) - 1) * mesh_spacing
    x_distance = hypo_loc[0] * total_len_x
    x_node = int(numpy.round(x_distance / mesh_spacing))
    hypocentre = Point(mesh.lons[y_node][x_node], mesh.lats[y_node][x_node],
        mesh.depths[y_node][x_node])
    return hypocentre