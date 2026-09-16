def _fontsize(self, key, label='fontsize', common=True):
    size = super(BokehPlot, self)._fontsize(key, label, common)
    return {k: (v if isinstance(v, basestring) else '%spt' % v) for k, v in
        size.items()}