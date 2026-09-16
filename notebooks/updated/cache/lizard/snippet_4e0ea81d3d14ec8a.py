def add_clock(self, timezone, color='lightgreen', show_seconds=None):
    if show_seconds is None:
        show_seconds = self.options.show_seconds
    clock = Clock(self.app, self.logger, timezone, color=color, font=self.
        options.font, show_seconds=show_seconds)
    clock.widget.cfg_expand(7, 7)
    num_clocks = len(self.clocks)
    cols = self.settings.get('columns')
    row = num_clocks // cols
    col = num_clocks % cols
    self.clocks[timezone] = clock
    self.grid.add_widget(clock.widget, row, col, stretch=1)