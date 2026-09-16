def intersects_id(self, ray_origins, ray_directions, return_locations=False,
    multiple_hits=True, **kwargs):
    index_tri, index_ray, locations = ray_triangle_id(triangles=self.mesh.
        triangles, ray_origins=ray_origins, ray_directions=ray_directions,
        tree=self.mesh.triangles_tree, multiple_hits=multiple_hits,
        triangles_normal=self.mesh.face_normals)
    if return_locations:
        if len(index_tri) == 0:
            return index_tri, index_ray, locations
        unique = grouping.unique_rows(np.column_stack((locations, index_ray)))[
            0]
        return index_tri[unique], index_ray[unique], locations[unique]
    return index_tri, index_ray