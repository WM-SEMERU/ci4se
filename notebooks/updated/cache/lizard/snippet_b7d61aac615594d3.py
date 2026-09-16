def figure(self):
    if not hasattr(self, '_figure'):
        self._figure = matplotlib.pyplot.figure()
    return self._figure