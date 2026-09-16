def add_material(self, x_min, x_max, n, angle=0):
    self._mat_params.append([x_min, x_max, n, angle])
    if not callable(n):
        n_mat = lambda wl: n
    else:
        n_mat = n
    Structure._add_material(self, x_min, self.y_min, x_max, self.y_max,
        n_mat(self._wl), angle)
    return self.n