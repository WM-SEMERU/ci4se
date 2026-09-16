def plothist(self, fig=None, **kwargs):
    setfig(fig)
    plt.hist(self.samples, bins=self.bins, **kwargs)