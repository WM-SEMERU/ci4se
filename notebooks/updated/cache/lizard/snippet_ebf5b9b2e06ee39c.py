def swapTabType(self, action):
    if not self._currentPanel.count():
        self.addView(action)
        return
    viewType = self._viewWidget.viewType(action.text())
    view = self._currentPanel.currentView()
    if type(view) == viewType:
        return
    self._viewWidget.setUpdatesEnabled(False)
    self._currentPanel.blockSignals(True)
    view.close()
    index = self._currentPanel.currentIndex()
    new_view = viewType.createInstance(self._viewWidget, self._viewWidget)
    self._currentPanel.insertTab(index, new_view, new_view.windowTitle())
    self._currentPanel.blockSignals(False)
    self._currentPanel.setCurrentIndex(index)
    self._viewWidget.setUpdatesEnabled(True)