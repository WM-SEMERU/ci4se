def range(self, dim, data_range=True, dimension_range=True):
    didx = self.get_dimension_index(dim)
    dim = self.get_dimension(dim)
    if didx == 1 and data_range and len(self):
        mean = self.dimension_values(1)
        neg_error = self.dimension_values(2)
        if len(self.dimensions()) > 3:
            pos_error = self.dimension_values(3)
        else:
            pos_error = neg_error
        lower = np.nanmin(mean - neg_error)
        upper = np.nanmax(mean + pos_error)
        if not dimension_range:
            return lower, upper
        return util.dimension_range(lower, upper, dim.range, dim.soft_range)
    return super(ErrorBars, self).range(dim, data_range)