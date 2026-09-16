def ScaleSmaller(self):
    newfactor = self._zoomfactor - 0.1
    if float(newfactor) > 0 and float(newfactor) < self._MAX_ZOOM:
        self._zoomfactor = newfactor