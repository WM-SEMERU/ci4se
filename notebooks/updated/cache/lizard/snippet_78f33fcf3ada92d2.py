def get_connectivity(self, measure_name, plot=False):
    if self.connectivity_ is None:
        raise RuntimeError(
            'Connectivity requires a VAR model (run do_mvarica or fit_var first)'
            )
    cm = getattr(self.connectivity_, measure_name)()
    cm = np.abs(cm) if np.any(np.iscomplex(cm)) else cm
    if plot is None or plot:
        fig = plot
        if self.plot_diagonal == 'fill':
            diagonal = 0
        elif self.plot_diagonal == 'S':
            diagonal = -1
            sm = np.abs(self.connectivity_.S())
            sm /= np.max(sm)
            fig = self.plotting.plot_connectivity_spectrum(sm, fs=self.fs_,
                freq_range=self.plot_f_range, diagonal=1, border=self.
                plot_outside_topo, fig=fig)
        else:
            diagonal = -1
        fig = self.plotting.plot_connectivity_spectrum(cm, fs=self.fs_,
            freq_range=self.plot_f_range, diagonal=diagonal, border=self.
            plot_outside_topo, fig=fig)
        return cm, fig
    return cm