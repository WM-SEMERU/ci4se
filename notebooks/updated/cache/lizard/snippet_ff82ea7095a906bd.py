def GetAnalysisStatusUpdateCallback(self):
    if self._mode == self.MODE_LINEAR:
        return self._PrintAnalysisStatusUpdateLinear
    if self._mode == self.MODE_WINDOW:
        return self._PrintAnalysisStatusUpdateWindow
    return None