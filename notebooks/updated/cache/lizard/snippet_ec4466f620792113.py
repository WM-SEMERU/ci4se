def scatter_plot(self, ax, topic_dims, t=None, ms_limits=True, **kwargs_plot):
    plot_specs = {'marker': 'o', 'linestyle': 'None'}
    plot_specs.update(kwargs_plot)
    data = self.data_t(topic_dims, t)
    ax.plot(*data.T, **plot_specs)
    if ms_limits:
        ax.axis(self.axes_limits(topic_dims))