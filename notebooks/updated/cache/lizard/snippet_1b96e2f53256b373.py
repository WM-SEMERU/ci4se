def histogram(self, column='r', filename=None, log10=False, **kwargs):
    return_dict = HS.plot_histograms(self.data, column)
    if filename is not None:
        return_dict['all'].savefig(filename, dpi=300)
    return return_dict