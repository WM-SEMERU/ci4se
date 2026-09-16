def setCurrentMode(self, mode):
    if mode == self._currentMode:
        return
    self._currentMode = mode
    ajax = mode == XLoaderWidget.Mode.Spinner
    self._movieLabel.setVisible(ajax)
    self._primaryProgressBar.setVisible(not ajax)
    self._subProgressBar.setVisible(not ajax and self._showSubProgress)