def _iter_subplots(self):
    for i in range(self.n_cols):
        for j in range(self.n_cols):
            if i > j:
                continue
            dim = self.grid_dim[i][j]
            dim_x, dim_y = dim.split(',')
            yield i, j, dim_x, dim_y