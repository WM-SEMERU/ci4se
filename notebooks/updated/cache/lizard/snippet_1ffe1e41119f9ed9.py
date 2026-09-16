def _find_particle_image(self, query, match, all_particles):
    _, idxs = self.particle_kdtree.query(query.pos, k=10)
    neighbors = all_particles[idxs]
    for particle in neighbors:
        if particle.index == match.index:
            return particle
    raise MBuildError(
        'Unable to find matching particle image while stitching bonds.')