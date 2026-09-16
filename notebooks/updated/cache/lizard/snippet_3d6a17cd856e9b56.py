def configure(self, event=None):
    if self.win_config is not None:
        try:
            self.win_config.Raise()
        except:
            self.win_config = None
    if self.win_config is None:
        self.win_config = PlotConfigFrame(parent=self, config=self.conf,
            trace_color_callback=self.trace_color_callback)
        self.win_config.Raise()