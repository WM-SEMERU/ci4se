def prepareToRemove(self):
    for node in (self._outputNode, self._inputNode):
        self.disconnectSignals(node)
    self._inputNode = None
    self._outputNode = None
    return True