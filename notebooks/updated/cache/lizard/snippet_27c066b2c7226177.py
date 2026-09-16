def add_legend(self):
    cuts = [tag for tag in self.tags if tag is not self._new_cut]
    self.cuts_plot.ax.legend(cuts, loc='best', shadow=True, fancybox=True,
        prop={'size': 8}, labelspacing=0.2)