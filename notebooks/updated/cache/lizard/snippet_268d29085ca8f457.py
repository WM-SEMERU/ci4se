def make_plots(self, prefix, mcube_map=None, **kwargs):
    if mcube_map is None:
        mcube_map = self.model_counts_map()
    plotter = plotting.AnalysisPlotter(self.config['plotting'], fileio=self
        .config['fileio'], logging=self.config['logging'])
    plotter.run(self, mcube_map, prefix=prefix, **kwargs)