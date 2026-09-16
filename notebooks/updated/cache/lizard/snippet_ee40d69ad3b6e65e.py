def plot(self):
    fig = plotting.create_empty_figure()
    ax = fig.gca()
    xlabel = self.kwargs.get('xlabel', 'Dose')
    ylabel = self.kwargs.get('ylabel', 'Response')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.errorbar(self.doses, self.means, yerr=self.errorbars, label=
        'Mean ± 95% CI', **plotting.DATASET_POINT_FORMAT)
    ax.margins(plotting.PLOT_MARGINS)
    ax.set_title(self._get_dataset_name())
    ax.legend(**settings.LEGEND_OPTS)
    return fig