def detach(self, filt, view=None):
    if view is None:
        self._vshare.filters.remove(filt)
        for view in self._vshare.views.keys():
            filt._detach(view)
    else:
        view._filters.remove(filt)
        filt._detach(view)