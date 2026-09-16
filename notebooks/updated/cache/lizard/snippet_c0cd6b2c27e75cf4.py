def plot_eigh1(self, colorbar=True, cb_orientation='vertical', cb_label=
    None, ax=None, show=True, fname=None, **kwargs):
    if cb_label is None:
        cb_label = self._eigh1_label
    if self.eigh1 is None:
        self.compute_eigh()
    if ax is None:
        fig, axes = self.eigh1.plot(colorbar=colorbar, cb_orientation=
            cb_orientation, cb_label=cb_label, show=False, **kwargs)
        if show:
            fig.show()
        if fname is not None:
            fig.savefig(fname)
        return fig, axes
    else:
        self.eigh1.plot(colorbar=colorbar, cb_orientation=cb_orientation,
            cb_label=cb_label, ax=ax, **kwargs)