def get_sources_by_position(self, skydir, dist, min_dist=None, square=False,
    coordsys='CEL'):
    msk = get_skydir_distance_mask(self._src_skydir, skydir, dist, min_dist
        =min_dist, square=square, coordsys=coordsys)
    radius = self._src_skydir.separation(skydir).deg
    radius = radius[msk]
    srcs = [self._srcs[i] for i in np.nonzero(msk)[0]]
    isort = np.argsort(radius)
    radius = radius[isort]
    srcs = [srcs[i] for i in isort]
    return radius, srcs