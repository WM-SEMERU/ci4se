def get_bestfit_line(self, x_min=None, x_max=None, resolution=None):
    x = self.args['x']
    if x_min is None:
        x_min = min(x)
    if x_max is None:
        x_max = max(x)
    if resolution is None:
        resolution = self.args.get('resolution', 1000)
    bestfit_x = np.linspace(x_min, x_max, resolution)
    return [bestfit_x, self.bestfit_func(bestfit_x)]