def fit_overlays(self, text, start=None, end=None, **kw):
    for ovl in text.overlays:
        if ovl.match(props=self.props_match, rng=(start, end)):
            yield ovl