def setShowGridColumns(self, state):
    delegate = self.itemDelegate()
    if isinstance(delegate, XTreeWidgetDelegate):
        delegate.setShowGridColumns(state)