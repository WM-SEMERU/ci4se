def clear(self):
    self._srcs = []
    self._diffuse_srcs = []
    self._src_dict = collections.defaultdict(list)
    self._src_radius = []