def plot_series(self, xres, varied_data, varied_idx, **kwargs):
    for attr in 'names latex_names'.split():
        if kwargs.get(attr, None) is None:
            kwargs[attr] = getattr(self, attr)
    ax = plot_series(xres, varied_data, **kwargs)
    if self.par_by_name and isinstance(varied_idx, str):
        varied_idx = self.param_names.index(varied_idx)
    if self.latex_param_names:
        ax.set_xlabel('$%s$' % self.latex_param_names[varied_idx])
    elif self.param_names:
        ax.set_xlabel(self.param_names[varied_idx])
    return ax