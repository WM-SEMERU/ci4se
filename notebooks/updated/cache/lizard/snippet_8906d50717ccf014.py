def clearBreakpoints(self):
    self.markerDeleteAll(self._breakpointMarker)
    if not self.signalsBlocked():
        self.breakpointsChanged.emit()