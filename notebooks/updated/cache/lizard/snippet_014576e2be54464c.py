def intersects_location(self, ray_origins, ray_directions, multiple_hits=True):
    index_tri, index_ray, locations = self.intersects_id(ray_origins=
        ray_origins, ray_directions=ray_directions, multiple_hits=
        multiple_hits, return_locations=True)
    return locations, index_ray, index_tri