def poof(self, outpath=None, clear_figure=False, **kwargs):
    if self._ax is None:
        warn_message = (
            '{} does not have a reference to a matplotlib.Axes the figure may not render as expected!'
            )
        warnings.warn(warn_message.format(self.__class__.__name__),
            YellowbrickWarning)
    self.finalize()
    if outpath is not None:
        plt.savefig(outpath, **kwargs)
    else:
        plt.show()
    if clear_figure:
        plt.gcf().clear()