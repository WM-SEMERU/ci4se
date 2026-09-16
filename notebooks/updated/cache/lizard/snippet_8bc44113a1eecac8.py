def plot_vzy(self, colorbar=True, cb_orientation='vertical', cb_label=None,
    ax=None, show=True, fname=None, **kwargs):
    if cb_label is None:
        cb_label = self._vzy_label
    if ax is None:
        fig, axes = self.vzy.plot(colorbar=colorbar, cb_orientation=
            cb_orientation, cb_label=cb_label, show=False, **kwargs)
        if show:
            fig.show()
        if fname is not None:
            fig.savefig(fname)
        return fig, axes
    else:
        self.vzy.plot(colorbar=colorbar, cb_orientation=cb_orientation,
            cb_label=cb_label, ax=ax, **kwargs)