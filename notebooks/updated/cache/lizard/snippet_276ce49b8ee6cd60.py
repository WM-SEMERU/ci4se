def addMargin(self, margin, index=None):
    if index is None:
        self._margins.append(margin)
    else:
        self._margins.insert(index, margin)
    if margin.isVisible():
        self.updateViewport()