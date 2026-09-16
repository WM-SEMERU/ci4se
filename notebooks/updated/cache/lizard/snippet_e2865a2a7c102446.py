def percentile(self, percentile):
    out = scipy.percentile(self.value, percentile, axis=0)
    if self.name is not None:
        name = '{}: {} percentile'.format(self.name, _ordinal(percentile))
    else:
        name = None
    return FrequencySeries(out, epoch=self.epoch, channel=self.channel,
        name=name, f0=self.f0, df=self.df, frequencies=hasattr(self,
        '_frequencies') and self.frequencies or None)