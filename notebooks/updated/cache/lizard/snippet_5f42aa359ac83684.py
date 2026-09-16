def get_sites_in_sphere(self, pt, r):
    neighbors = []
    for site in self._sites:
        dist = site.distance_from_point(pt)
        if dist <= r:
            neighbors.append((site, dist))
    return neighbors