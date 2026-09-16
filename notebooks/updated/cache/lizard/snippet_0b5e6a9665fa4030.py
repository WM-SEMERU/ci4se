def plot_latent_inducing(self, which_indices=None, legend=False,
    plot_limits=None, marker=None, projection='2d', **kwargs):
    canvas, projection, kwargs, sig_dims = _new_canvas(self, projection,
        kwargs, which_indices)
    if legend:
        label = 'inducing'
    else:
        label = None
    if marker is not None:
        kwargs['marker'] = marker
    update_not_existing_kwargs(kwargs, pl().defaults.inducing_2d)
    from .data_plots import _plot_inducing
    scatters = _plot_inducing(self, canvas, sig_dims[:2], projection, label,
        **kwargs)
    return pl().add_to_canvas(canvas, dict(scatter=scatters), legend=legend)