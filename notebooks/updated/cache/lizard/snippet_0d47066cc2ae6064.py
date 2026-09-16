def series(self):
    if not self.pages:
        return []
    useframes = self.pages.useframes
    keyframe = self.pages.keyframe.index
    series = []
    for name in ('lsm', 'ome', 'imagej', 'shaped', 'fluoview', 'sis',
        'uniform', 'mdgel'):
        if getattr(self, 'is_' + name, False):
            series = getattr(self, '_series_' + name)()
            break
    self.pages.useframes = useframes
    self.pages.keyframe = keyframe
    if not series:
        series = self._series_generic()
    series = [s for s in series if product(s.shape) > 0]
    for i, s in enumerate(series):
        s.index = i
    return series