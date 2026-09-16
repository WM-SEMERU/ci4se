def add_angles(self, indexes, deg=False, cossin=False, periodic=True):
    from .angles import AngleFeature
    indexes = self._check_indices(indexes, pair_n=3)
    f = AngleFeature(self.topology, indexes, deg=deg, cossin=cossin,
        periodic=periodic)
    self.__add_feature(f)