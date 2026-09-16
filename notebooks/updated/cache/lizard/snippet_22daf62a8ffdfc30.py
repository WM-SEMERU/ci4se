def _collectAxisPoints(self):
    for l, (value, deltaName) in self.items():
        location = Location(l)
        name = location.isOnAxis()
        if name is not None and name is not False:
            if name not in self._axes:
                self._axes[name] = []
            if l not in self._axes[name]:
                self._axes[name].append(l)
    return self._axes