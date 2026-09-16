def unregisterViewType(self, cls, window=None):
    if cls in self._viewTypes:
        self._viewTypes.remove(cls)
        if window:
            cls.unregisterFromWindow(window)
        return True
    return False