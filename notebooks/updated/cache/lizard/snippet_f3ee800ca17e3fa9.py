def lower(self):
    if self._reaction in self._view._flipped:
        return -super(FlipableFluxBounds, self).upper
    return super(FlipableFluxBounds, self).lower