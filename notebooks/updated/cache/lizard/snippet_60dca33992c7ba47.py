def scrollParts(self, amount):
    change = self._scrollAmount - amount
    self._partsWidget.scroll(change, 0)
    self._scrollAmount = amount