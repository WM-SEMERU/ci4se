def scale_axes_from_data(self):
    if self.args.xmin is None:
        self.args.xmin = min(ts.xspan[0] for ts in self.timeseries)
    if self.args.xmax is None:
        self.args.xmax = max(ts.xspan[1] for ts in self.timeseries)
    cropped = [ts.crop(self.args.xmin, self.args.xmax) for ts in self.
        timeseries]
    ymin = min(ts.value.min() for ts in cropped)
    ymax = max(ts.value.max() for ts in cropped)
    self.plot.gca().yaxis.set_data_interval(ymin, ymax, ignore=True)
    self.plot.gca().autoscale_view(scalex=False)