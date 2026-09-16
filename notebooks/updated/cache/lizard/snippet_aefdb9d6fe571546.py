def setShowAttachments(self, state):
    self._showAttachments = state
    self._attachAction.setVisible(state)