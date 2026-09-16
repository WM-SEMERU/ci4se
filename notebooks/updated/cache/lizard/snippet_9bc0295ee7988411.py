def hist(self, dimension=None, num_bins=20, bin_range=None, adjoin=True,
    index=0, **kwargs):
    valid_ind = isinstance(index, int) and 0 <= index < len(self)
    valid_label = index in [el.label for el in self]
    if not any([valid_ind, valid_label]):
        raise TypeError(
            'Please supply a suitable index or label for the histogram data')
    hists = self.get(index).hist(adjoin=False, dimension=dimension,
        bin_range=bin_range, num_bins=num_bins, **kwargs)
    if not isinstance(hists, Layout):
        hists = [hists]
    if not isinstance(dimension, list):
        dimension = ['Default']
    if adjoin:
        layout = self
        for hist in hists:
            layout = layout << hist
        layout.main_layer = index
    elif len(dimension) > 1:
        layout = hists
    else:
        layout = hists[0]
    return layout