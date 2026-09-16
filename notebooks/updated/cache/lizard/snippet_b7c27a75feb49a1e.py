def sample_grid(self, count=None, step=None):
    if count is not None and step is not None:
        raise ValueError('only step OR count can be specified!')
    bounds = np.array([-self.primitive.extents, self.primitive.extents]) * 0.5
    if step is not None:
        grid = util.grid_arange(bounds, step=step)
    elif count is not None:
        grid = util.grid_linspace(bounds, count=count)
    else:
        raise ValueError('either count or step must be specified!')
    transformed = transformations.transform_points(grid, matrix=self.
        primitive.transform)
    return transformed