def plot_all(self, fig=None, iabscissa=1, iteridx=None, foffset=1e-19,
    x_opt=None, fontsize=9):
    try:
        from matplotlib.pyplot import figure, subplot, gcf
    except ImportError:
        ImportError(
            'could not find matplotlib.pyplot module, function plot() is not available'
            )
        return
    if fig is None:
        fig = 426
    if iabscissa not in (0, 1):
        iabscissa = 1
    self.load()
    dat = self
    if iteridx is not None:
        self.select_data(iteridx)
    if len(dat.f) == 0:
        print('nothing to plot')
        return
    figure(fig)
    self._enter_plotting(fontsize)
    self.fighandle = gcf()
    if 1 < 3:
        subplot(2, 3, 1)
        self.plot_divers(iabscissa, foffset)
        pyplot.xlabel('')
        subplot(2, 3, 4)
        self.plot_stds(iabscissa)
        subplot(2, 3, 2)
        self.plot_axes_scaling(iabscissa)
        pyplot.xlabel('')
        subplot(2, 3, 5)
        self.plot_correlations(iabscissa)
        subplot(2, 3, 3)
        self.plot_xrecent(iabscissa, x_opt)
        pyplot.xlabel('')
        subplot(2, 3, 6)
        self.plot_mean(iabscissa, x_opt)
    self._finalize_plotting()
    return self