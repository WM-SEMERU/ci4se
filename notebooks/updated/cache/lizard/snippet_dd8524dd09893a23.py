def plot(self, x, y, panel='top', xlabel=None, **kws):
    panel = self.get_panel(panel)
    panel.plot(x, y, **kws)
    if xlabel is not None:
        self.xlabel = xlabel
    if self.xlabel is not None:
        self.panel_bot.set_xlabel(self.xlabel)