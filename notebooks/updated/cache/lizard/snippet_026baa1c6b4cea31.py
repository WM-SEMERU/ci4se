def wheelEvent(self, ev, axis=None):
    state = None
    if ev.modifiers() == QtCore.Qt.ControlModifier:
        state = self.mouseEnabled()
        self.setMouseEnabled(not state[0], not state[1])
    if self._zeroWheel:
        ev.pos = lambda : self.mapViewToScene(QtCore.QPoint(0, 0))
    super(SpikeyViewBox, self).wheelEvent(ev, axis)
    if state is not None:
        self.setMouseEnabled(*state)