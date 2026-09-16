def plot_rad(self, colorbar=True, cb_orientation='vertical', cb_label=
    '$g_r$, m s$^{-2}$', ax=None, show=True, fname=None, **kwargs):
    if ax is None:
        fig, axes = self.rad.plot(colorbar=colorbar, cb_orientation=
            cb_orientation, cb_label=cb_label, show=False, **kwargs)
        if show:
            fig.show()
        if fname is not None:
            fig.savefig(fname)
        return fig, axes
    else:
        self.rad.plot(colorbar=colorbar, cb_orientation=cb_orientation,
            cb_label=cb_label, ax=ax, **kwargs)